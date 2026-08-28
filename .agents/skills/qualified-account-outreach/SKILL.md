---
name: qualified-account-outreach
description: Helps a B2B seller identify best-fit target companies, qualify a selected account, and produce sourced two-touch outreach drafts from public evidence, with optional permissioned LinkedIn enrichment through Apify. Use when a salesperson wants a guided target-account research and outreach workflow that stops before sending.
---

# Qualified account outreach

## Guided start

When invoked without a complete seller-and-target input, begin as an interactive assistant. Do not research yet.

1. Briefly explain that this skill can:
   - understand the seller's product and derive a provisional ICP from its website;
   - turn a plain-language target request into a sourced, ranked account shortlist;
   - qualify a selected company and draft an evidence-based two-touch outreach sequence;
   - optionally enrich permitted professional profiles through Apify; and
   - stop before any message is sent.
2. Ask only: **What is the website of the company whose products or services you want to sell?**
3. After the user supplies the seller website, fetch enough seller-owned material to understand the offer. Summarize the seller, product, likely buyer, and provisional ICP in no more than five bullets. Mark all inferred ICP elements as provisional.
4. Then ask only: **Which customers do you want to target today?** Explain that a plain-language request is enough, for example: `the top 10 German companies`, `UK fintechs with 500–5,000 employees`, or `European manufacturers expanding in the US`.
5. If the request says `top` without defining the ranking, interpret it as **strongest apparent fit for the seller's offer**, not largest by revenue or headcount. State that interpretation before proceeding. Ask a clarifying question only if geography, company type, or another constraint needed to identify a coherent market is missing.

If the prompt already supplies both the seller and target request, skip answered questions and proceed. If it names one target company and an output path, use the single-account workflow directly.

## Target discovery

For a multi-company request such as `top 10 German companies`:

1. Use the seller-owned evidence and the requested market constraints to define a short, provisional fit rubric. Never present an inferred ICP as the seller's confirmed strategy.
2. Discover candidates from public sources. Use first-party company pages for material fit claims; use reputable directories, filings, or rankings to build the candidate set. Search snippets are discovery only.
3. Rank no more than the requested number of companies. For each, show company, website, fit rationale, one or two dated source links, confidence, and the largest unknown or disqualifier. Do not manufacture exact scores when evidence is too thin.
4. Write or display the sourced shortlist, then ask which account or accounts the user wants to qualify and personalize. Do not silently begin person-level collection.
5. If the user chooses an account, collect or resolve its official website and continue with the company qualification workflow. If multiple accounts are chosen, produce separate evidence and drafts for each and clearly report any that lack sufficient evidence.

## Complete input

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
   - Use warm, plain language that connects the seller's value to the human work at stake: protecting people, helping customers, reducing unnecessary burden, or making responsible work easier. Lead with a specific verified observation, then make the human consequence relevant to the role.
   - Acknowledge the effort behind the target's existing program without flattery. Never presume that a recipient is stressed, failing, worried, or personally affected; frame those as possibilities or questions.
   - No manufactured urgency, surveillance language, fear-based pressure, outcome guarantees, or invented familiarity.
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
