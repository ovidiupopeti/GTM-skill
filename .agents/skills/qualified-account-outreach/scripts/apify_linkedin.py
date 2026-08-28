#!/usr/bin/env python3
"""Run approved HarvestAPI LinkedIn Actors without third-party Python packages."""

from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request


ACTORS = {
    "search": "harvestapi~linkedin-profile-search",
    "profile": "harvestapi~linkedin-profile-scraper",
}


def fail(message: str) -> None:
    raise SystemExit(message)


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        fail(f"Expected a JSON object in {path}")
    return value


def check_permission() -> None:
    permission_path = os.environ.get("APIFY_PERMISSION_FILE")
    if not permission_path:
        fail("APIFY_PERMISSION_FILE is required")
    permission = load_json(permission_path)
    if permission.get("linkedin_processing_authorized") is not True:
        fail("Authorization record does not permit LinkedIn processing")
    expiry = permission.get("expires")
    if not expiry:
        fail("Authorization record must include an expiry date")
    if dt.date.fromisoformat(expiry) < dt.date.today():
        fail("Authorization record has expired")


def validate_input(mode: str, payload: dict) -> dict:
    if mode == "search":
        if payload.get("profileScraperMode") == "Full + email search":
            fail("Email discovery is disabled")
        payload["profileScraperMode"] = "Full"
        maximum = int(payload.get("maxItems", 10))
        if maximum < 1 or maximum > 10:
            fail("search maxItems must be between 1 and 10")
        payload["maxItems"] = maximum
    else:
        if payload.get("profileScraperMode") == "Profile details + email search ($10 per 1k)":
            fail("Email discovery is disabled")
        payload["profileScraperMode"] = "Profile details no email ($4 per 1k)"
        queries = payload.get("queries") or payload.get("urls") or []
        if not isinstance(queries, list) or not 1 <= len(queries) <= 5:
            fail("profile mode requires 1–5 profile queries or URLs")
    return payload


def main() -> None:
    if len(sys.argv) != 4 or sys.argv[1] not in ACTORS:
        fail("Usage: apify_linkedin.py <search|profile> <input.json> <output.json>")
    mode, input_path, output_path = sys.argv[1:]
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        fail("APIFY_TOKEN is required")
    check_permission()
    payload = validate_input(mode, load_json(input_path))
    actor = ACTORS[mode]
    url = f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items?clean=true"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        fail(f"Apify request failed with HTTP {exc.code}")
    destination = pathlib.Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(result) if isinstance(result, list) else 1} result(s) to {destination}")


if __name__ == "__main__":
    main()
