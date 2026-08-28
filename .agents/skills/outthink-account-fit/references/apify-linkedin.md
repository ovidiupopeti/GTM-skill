# Permissioned Apify LinkedIn enrichment

Read this only when the user requests LinkedIn person-level enrichment and supplies documented permission.

## Verified actors and API

Verified 2026-08-28 from Apify's API docs and Actor input schemas:

- Search Actor: `harvestapi/linkedin-profile-search`
  - Inputs used here: `profileScraperMode`, `searchQuery`, `maxItems`, `locations`, `currentCompanies`, `currentJobTitles`.
  - Safe mode for this skill: `Full`, with `maxItems` at most 10. Never use `Full + email search`.
- Profile Actor: `harvestapi/linkedin-profile-scraper`
  - Inputs used here: `profileScraperMode` and `queries` containing profile URLs or public identifiers.
  - Safe mode for this skill: `Profile details no email ($4 per 1k)`, with at most 5 queries.
- Synchronous REST pattern: `POST https://api.apify.com/v2/acts/<actor-id-with-~>/run-sync-get-dataset-items`, JSON body, `Authorization: Bearer <APIFY_TOKEN>`.

Sources:

- https://docs.apify.com/api
- https://apify.com/harvestapi/linkedin-profile-search/input-schema
- https://apify.com/harvestapi/linkedin-profile-scraper/input-schema

## Authorization record

Set `APIFY_PERMISSION_FILE` to a local JSON file outside the tracked tree or under `.private/`. It must contain:

```json
{
  "linkedin_processing_authorized": true,
  "covered_people_or_selection_rule": "...",
  "allowed_purpose": "B2B qualification and outreach drafting",
  "expires": "YYYY-MM-DD",
  "public_redistribution_authorized": false
}
```

The helper checks the authorization flag and expiry. The operator remains responsible for ensuring the named scope covers the people and intended use. Do not print or commit the record.

## Local workflow

1. Store Actor input under `.private/`.
2. Export `APIFY_TOKEN` and `APIFY_PERMISSION_FILE` locally; never place either in a prompt, repository file, shell history, or output.
3. Run one of:

   `python3 .agents/skills/outthink-account-fit/scripts/apify_linkedin.py search .private/search.json .private/search-results.json`

   `python3 .agents/skills/outthink-account-fit/scripts/apify_linkedin.py profile .private/profiles.json .private/profile-results.json`

4. Analyze only fields needed for role relevance and observable professional communication. Keep raw and derived person-level files private unless the authorization explicitly permits public redistribution under MIT.

## Interpretation boundary

Profile fields can support role, seniority, experience, stated interests, and self-authored professional themes. They do not establish personality, emotional state, private motivation, purchasing intent, or how a person will react. Posts and reactions, when separately authorized and supplied, support only a description of observable topics and communication patterns—not psychological profiling.
