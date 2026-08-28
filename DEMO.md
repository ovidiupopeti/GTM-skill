# Run sheet

The organizer presents this repository in 2 minutes without having seen it before.

## Say this — 20 seconds

**Team:** OutThink GTM

**Track:** Personalized growth engines

**Who has the problem:** An enterprise cybersecurity GTM professional who needs to prioritize accounts and earn a relevant first reply.

**The job this skill does:** Turns public company evidence into a reproducible OutThink fit decision and a role-based two-touch outreach hypothesis.

**Boundary — what it never does:** It never scrapes or profiles people, infers personality, handles contact data, sends messages, or guesses when evidence is missing.

## Run this — 60 seconds

1. Codex is open at the repository root.
2. Paste [`demo/seed-prompt.md`](demo/seed-prompt.md).
3. Watch for: a fit decision, the top three cited signals, and the written output path.
4. If nothing is visible after 60 seconds, open [`demo/output/schneider-electric-account-fit.md`](demo/output/schneider-electric-account-fit.md).

## Show this — 25 seconds

**Result:** A 9/10 priority-account hypothesis with counterevidence, unknowns, buyer roles, and two short draft touches. A GTM user reviews it before deciding whether to contact the account.

**Evidence:** The output contains a reproducible five-dimension scorecard and a claim/source/date/confidence table based on Schneider Electric's public pages.

**Fallback output was produced:** 2026-08-28 at 19:09 Europe/Bucharest by running the skill workflow in Codex against the representative input and fetching the listed first-party URLs.

## Evals — 10 seconds

| Case | Result | Where |
| --- | --- | --- |
| Intended | Pass — sourced score and draft produced | [`demo/evals.md`](demo/evals.md) |
| Insufficient evidence | Pass — abstained without a URL | [`demo/evals.md`](demo/evals.md) |
| Failure / exclusion | Pass — refused personal profiling | [`demo/evals.md`](demo/evals.md) |

## Close — 5 seconds

**Reusable on:** Any target-company input containing public first-party company URLs.

**Material limitation:** Public relevance signals cannot prove buying intent, incumbent dissatisfaction, or likely reply behavior.
