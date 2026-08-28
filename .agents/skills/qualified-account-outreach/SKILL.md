---
name: qualified-account-outreach
description: Qualifies a target company for any B2B seller and produces sourced two-touch outreach drafts from public company evidence, with optional permissioned LinkedIn enrichment through Apify. Use when salespeople need a repeatable account-research, fit, and message-drafting SOP that stops before sending.
---

# Qualified account outreach

## Input

Read the seller profile, target company, public URLs, and requested output path from the file named in the prompt. If the seller offer or target company URL cannot be resolved, write an insufficient-evidence result and stop.

Read `references/qualification-sop.md` for the input contract, scoring rubric, output schema, and outreach quality bar.

If LinkedIn enrichment is requested, also read `references/apify-linkedin.md`. Require a local authorization record before processing profiles. Keep that record, the token, raw results, and person-level output under `.private/`. Only write person-level data elsewhere when authorization explicitly permits public redistribution under the repository licence.

## Company qualification workflow

1. Fetch the supplied seller and target URLs. Optionally fetch at most two additional first-party pages for each company when they materially clarify the offer, proof, ICP, scale, priorities, or buying trigger.
2. Record every used URL and retrieval date. Treat search snippets as discovery only. Never describe cached data as live.
3. Turn the seller material into a provisional sales brief: product, problem solved, best-fit signals, buying roles, proof points, disqualifiers, desired next step, and prohibited claims. Mark anything not explicitly supplied as an assumption.
4. Extract target-company facts only. Record each as `claim / source / date / confidence and reason`. Absence of public evidence is unknown, not negative evidence.
5. Score the five generic dimensions in the SOP from 0–2. Award points only from cited evidence. Label the account `priority` at 8–10, `nurture` at 5–7, or `insufficient fit evidence` at 0–4. State that customer, vendor, incumbent, budget, and buying-intent status are unverified unless sourced.
6. Identify one likely buying role and one supporting role from the seller brief and target evidence. Do not invent an org chart.
7. Describe the target company's public communications tone with at most three observable descriptors supported by company-owned wording. Do not infer personality, emotions, vulnerabilities, or private intent.
8. Map up to three verified target signals to seller capabilities. Separate evidence from hypotheses and state the strongest reason not to pursue.
9. Draft a role-based sequence:
   - Touch 1: 70–100 words; one verified observation, one problem hypothesis, one diagnostic question, and the seller's low-friction next step.
   - Touch 2: 45–75 words; a different evidence-based angle and an easy reply choice.
   - Use plain professional language. No flattery, manufactured urgency, surveillance language, outcome guarantees, or invented familiarity.
10. Write the requested output with the sections defined in the SOP, then print the decision, top three signals, and output path.

## Optional authorized-person mode

1. Confirm authorization covers the named or selected people, LinkedIn collection, outreach analysis, retention period, recipients, and any redistribution. Stop if scope is unclear.
2. Require `APIFY_TOKEN` and `APIFY_PERMISSION_FILE`. Run `scripts/apify_linkedin.py`; never enable email discovery.
3. Minimize collection: target-company and relevant-role filters, at most 10 search results, and at most 5 selected profiles.
4. Use verified professional facts and observable self-authored communication themes only. Never infer psychological traits or likely emotional reactions.
5. Draft one two-touch sequence per permitted person by combining one verified account signal with one verified role-relevance signal. Never mention scraping or private-seeming familiarity.
6. Keep raw results and person-level drafts in `.private/` by default. Never stage or commit them.

## Safety and failure behavior

- Never process LinkedIn data without documented permission. Never collect emails or phone numbers through this skill.
- Stop at reviewable drafts. Never send, publish, modify a CRM, buy data, or contact anyone.
- If fewer than two medium- or high-confidence fit signals exist, abstain from personalized claims.
- Never claim a message will cause a reply; treat it as a testable hypothesis.

## Done when

The output exists, every material claim has a URL and date, the score is reproducible, assumptions and counterevidence are visible, and all messages remain unsent drafts.
