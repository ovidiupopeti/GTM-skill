---
name: outthink-account-fit
description: Qualifies a target company for OutThink and produces sourced two-touch outreach drafts from public company evidence, with optional permissioned LinkedIn professional-data enrichment through Apify. Use for evidence-grounded account fit and personalized outreach that must stop before sending.
---

# OutThink account fit

## Input

Read the company and public company URLs from the path named in the prompt. If no resolvable company URL is present, write an insufficient-evidence result and stop.

Before analysis, read `references/outthink-icp.md` for the rubric, buyer roles, messaging pillars, and boundaries.

If the input requests LinkedIn enrichment, also read `references/apify-linkedin.md`. Require a local authorization record before processing any profile. Keep the authorization record, Apify token, raw results, and person-level output under `.private/`, which is gitignored. Only write person-level data elsewhere when the authorization explicitly permits public redistribution under the repository's MIT publication terms.

## Workflow

1. Fetch the supplied public company URLs. Optionally fetch at most two additional first-party company pages that materially clarify workforce scale, operating complexity, cybersecurity priorities, or current human-risk practices.
2. Record every used URL and the retrieval date. Treat search snippets as discovery only; cite the underlying page. Never describe committed or cached data as live.
3. Extract only company-level facts. For each fact record the claim, source, date, and confidence (`high`, `medium`, or `low`) with a short reason.
4. Score the five ICP dimensions in the reference from 0–2. Award points only when a cited fact supports them. Label the account `priority` at 8–10, `nurture` at 5–7, or `insufficient fit evidence` at 0–4. State that customer/vendor status is unverified unless a source proves it.
5. Identify one likely buying role and one supporting role from the reference; never name or research an individual.
6. Describe the company's public communications tone with at most three observable descriptors. Support each with wording or themes from company-owned pages; do not infer personality, emotions, private intent, or psychological traits.
7. Map up to three verified account signals to OutThink capabilities. Separate evidence from hypotheses and state the strongest reason not to pursue the account.
8. Draft a two-touch sequence addressed to the buying role, not a person:
   - Touch 1: 70–100 words, one verified observation, one relevant problem hypothesis, one question, and a low-friction invitation to a 20-minute HRM conversation.
   - Touch 2: 45–75 words, add a different evidence-based angle and offer an easy reply choice.
   - Use plain professional language. No manufactured urgency, flattery, surveillance language, outcome guarantees, or invented familiarity.
9. Write the output path requested by the prompt with: decision, scorecard, evidence table, buyer roles, tone evidence, signal-to-capability map, two-touch draft, counterevidence, unknowns, and sources.
10. Print the decision, top three signals, and output path.

## Optional authorized-person mode

1. Confirm the named authorization record covers the specific people, LinkedIn collection, outreach analysis, retention period, and intended recipients. If any scope is unclear, stop and ask.
2. Require `APIFY_TOKEN` and `APIFY_PERMISSION_FILE` in the local environment. Run `scripts/apify_linkedin.py` only with the documented search or profile modes; do not enable email discovery.
3. Use the smallest result set: target-company filter, relevant security titles, at most 10 search results, and at most 5 full profiles selected for likely buying relevance.
4. For each permitted profile, distinguish verified professional facts from hypotheses. Describe observable professional communication themes only when supplied text supports them. Do not infer personality, emotions, vulnerabilities, or private intent from profile fields, posts, reactions, or sparse engagement.
5. Produce one two-touch sequence per permitted person. Connect one verified account signal and one verified professional-role signal to a plausible OutThink problem; do not mention monitoring, scraping, reactions, or private-seeming familiarity.
6. Keep raw results and person-level drafts in `.private/` by default. Never stage or commit them.

## Safety and failure behavior

- Never process LinkedIn profiles without documented permission covering the specific use. Never collect emails or phone numbers through this skill.
- Never infer personality, emotions, vulnerabilities, or private intent. With permission, use only verifiable professional facts and observable communication themes relevant to the role.
- Never include personal data or secrets in output. Never call an authenticated service or require an API key for the judged path.
- Stop at reviewable drafts. Never send messages, modify a CRM, buy data, or contact anyone.
- If fewer than two medium- or high-confidence fit signals exist, label the result insufficient and do not draft personalized claims.
- Never claim the sequence will cause a reply; present it as a testable hypothesis.

## Done when

The output exists, every material factual claim has a URL and retrieval date, the score is reproducible, counterevidence and unknowns are visible, and the sequence remains a role-based draft.
