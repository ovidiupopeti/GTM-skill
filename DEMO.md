# Run sheet

The organizer presents this repository in 2 minutes without having seen it before.

## Say this — 20 seconds

**Team:** OutThink GTM

**Track:** Personalized growth engines

**Who has the problem:** A B2B salesperson who needs to prioritize target accounts and earn a relevant first reply.

**The job this skill does:** Applies any seller's supplied ICP and proof to public target-company evidence, producing a reproducible fit decision and role-based two-touch outreach hypothesis.

**Boundary — what it never does:** It never scrapes or profiles people, infers personality, handles contact data, sends messages, or guesses when evidence is missing.

## Run this — 60 seconds

1. Codex is open at the repository root.
2. Paste [`demo/seed-prompt.md`](demo/seed-prompt.md).
3. Watch for: a fit decision, the top three cited signals, and the written output path.
4. If nothing is visible after 60 seconds, open [`demo/output/schneider-electric-account-fit.md`](demo/output/schneider-electric-account-fit.md).

## Show this — 25 seconds

**Result:** A 9/10 priority-account hypothesis with counterevidence, unknowns, buyer roles, and two short draft touches. A GTM user reviews it before deciding whether to contact the account.

**Evidence:** The output contains a reproducible five-dimension scorecard and a claim/source/date/confidence table based on Schneider Electric's public pages.

**Fallback output was produced:** 2026-08-28 at 19:32 Europe/Bucharest by running the generic skill workflow in Codex against the seller-to-target representative input and its listed first-party URLs.

## Evals — 10 seconds

| Case | Result | Where |
| --- | --- | --- |
| Intended | Pass — sourced score and draft produced | [`demo/evals.md`](demo/evals.md) |
| Insufficient evidence | Pass — abstained without a URL | [`demo/evals.md`](demo/evals.md) |
| Failure / exclusion | Pass — refused personal profiling | [`demo/evals.md`](demo/evals.md) |

## Close — 5 seconds

**Reusable on:** Any B2B seller and target-company input using the same seller/offer/ICP/target contract.

**Material limitation:** Public relevance signals cannot prove buying intent, incumbent dissatisfaction, or likely reply behavior.
