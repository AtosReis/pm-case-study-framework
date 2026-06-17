# PM QUESTION BANK

## Purpose

This is a reusable question bank for Product Manager work.

The goal is to prevent premature solutioning.

Before writing tickets, proposing automation, or discussing implementation, the PM should ask enough questions to understand:

- business goal;
- user actors;
- systems involved;
- permissions;
- data ownership;
- workflow;
- product decisions;
- risks;
- MVP scope;
- engineering dependencies.

## The Core PM Rule

Do not jump from request to solution.

Move through this sequence:

1. Understand the business goal.
2. Identify users and actors.
3. Map systems and ownership.
4. Clarify the user journey.
5. Identify product decisions.
6. Define use cases.
7. Write engineering-ready tickets.

---

# 1. Business Goal Questions

## Main Questions

- What business outcome are we trying to create?
- Why does this need to exist now?
- Who asked for this?
- Who benefits if this works?
- What problem are we solving?
- What happens if we do nothing?
- Is this about revenue, retention, efficiency, compliance, user experience, or strategic partnership?

## Success Questions

- What does success look like?
- How will we measure success?
- What is the primary KPI?
- What is the secondary KPI?
- Is there a deadline or external dependency?
- Is this a proof of concept, MVP, production feature, or client demo?

## PM Warning Signs

- The request is framed as a solution instead of a problem.
- The stakeholder says "just automate it."
- The stakeholder says "integrate everything" without defining workflow.
- The stakeholder wants engineering tickets before the product flow is clear.

---

# 2. User and Actor Questions

## Primary User

- Who is the primary user?
- What job is this user trying to complete?
- Where does this user start?
- What system does this user already use?
- What does this user know or not know?
- What decision does this user need to make?

## Secondary Users

- Who else interacts with the workflow?
- Who approves the output?
- Who configures access?
- Who receives the output?
- Who supports or audits the workflow?

## Risk Users

- Who can be harmed by a bad implementation?
- Who loses time if the workflow fails?
- Who is accountable if the output is wrong?
- Who owns compliance responsibility?

---

# 3. Systems and Ownership Questions

## System Map

- Which systems are involved?
- Where does the user start?
- Which system owns authentication?
- Which system owns user identity?
- Which system owns data?
- Which system owns permissions?
- Which system owns the final output?
- Which system owns analytics?

## Integration Questions

- Is this embedded, API-based, export-based, or manual for MVP?
- Does the partner system allow embedding?
- Are APIs available?
- Is SSO required?
- Is data copied, referenced, or transformed?
- What is the source of truth?

## Ownership Questions

- Who owns the content?
- Who owns customer/contact data?
- Who owns generated output?
- Who owns sending or publishing?
- Who owns logs and audit data?
- Who owns failure handling?

---

# 4. Permission and Access Questions

## Access

- Who can access the feature?
- Is access account-level, user-level, role-level, or organization-level?
- How is access granted?
- How is access revoked?
- What happens when a user is unauthorized?

## Content / Data Permissions

- Who can see which content?
- Who can select content?
- Who can edit content?
- Who can generate output?
- Who can approve output?
- Who can export, send, or publish?

## Failure States

- What happens if permissions fail?
- What happens if a session expires?
- What happens if a user changes roles?
- What happens if access is revoked mid-workflow?

---

# 5. User Journey Questions

## Journey Mapping

- What is the first user action?
- What is the final user outcome?
- What are the steps in between?
- Where can the user get blocked?
- What must the system show at each step?
- What decisions does the user make?

## Workflow Questions

- Is there a review step?
- Is there an approval step?
- Can the user go back?
- Can the user save progress?
- Can the user edit after approval?
- Can the user abandon the workflow?

## Output Questions

- What output is created?
- Who receives or consumes it?
- Is the output draft, final, exported, sent, or published?
- Does the output need metadata?
- Does the output need traceability?

---

# 6. Product Decision Questions

## Decision Identification

- What must be decided before engineering starts?
- What is already decided?
- What still needs validation?
- What is explicitly out of scope?
- Who owns each decision?

## Common Product Decisions

- Is SSO required?
- Is the feature embedded or standalone?
- Is the experience branded, co-branded, or white-label?
- Is approval required before output?
- Which system is the source of truth?
- Which system owns distribution?
- Is AI used in MVP?
- Which data can AI use?
- What is the fallback if AI fails?

## PM Rule

Never send an unresolved product decision to engineering as an "if."

Bad:

"If we use an LLM, make sure it does not hallucinate."

Better:

"For MVP, generation is LLM-assisted and constrained to selected approved content. The generated draft must show source references and require user approval before export."

---

# 7. MVP Scope Questions

## In Scope

- What is the smallest useful version?
- What must be included for the workflow to make sense?
- What must be included for stakeholders to validate the concept?
- What must be included for engineering to test end-to-end?

## Out of Scope

- What should not be built now?
- What is too risky for MVP?
- What depends on external systems?
- What belongs to V2?
- What can be simulated for demo?

## MVP Quality Bar

- Does the MVP show the core user journey?
- Does the MVP test the riskiest assumption?
- Does the MVP avoid unnecessary complexity?
- Does the MVP protect users from obvious failure states?

---

# 8. Engineering Ticket Questions

## Before Writing a Ticket

- Which use case does this ticket support?
- Which product decision does this ticket depend on?
- Who is the user?
- What action should the user or system perform?
- What should engineering build?
- What should engineering not build?
- How will we know it is done?

## Ticket Components

- Objective
- User story
- Product context
- Functional requirements
- Acceptance criteria
- Dependencies
- Edge cases
- Out of scope

## Acceptance Criteria Questions

- Can QA test this?
- Can engineering verify completion?
- Are success states covered?
- Are failure states covered?
- Are permission cases covered?
- Are empty states covered?
- Are edge cases documented?

---

# 9. Risk Questions

## Product Risk

- Are we solving the right problem?
- Does the user actually need this?
- Is the workflow too complex?
- Is the MVP too broad?
- Are we assuming behavior that has not been validated?

## Technical Risk

- Are required APIs available?
- Are there authentication constraints?
- Are there data ownership constraints?
- Are there performance constraints?
- Are there security constraints?

## Business / Client Risk

- Is the client expecting production when we are building MVP?
- Are stakeholders aligned on scope?
- Is there a critical deadline?
- Is the client already confused internally?
- Are we adding ambiguity instead of reducing it?

## AI Risk

- Is AI actually needed?
- What data can AI use?
- What data is prohibited?
- Can the model invent unsupported claims?
- Is human approval required?
- Is there auditability?

---

# 10. PM Self-Check Before Handoff

Before handing work to engineering, ask:

1. Can I explain the user journey in plain English?
2. Can I name the primary actor?
3. Can I name the systems involved?
4. Can I explain what is in scope?
5. Can I explain what is out of scope?
6. Can I identify unresolved decisions?
7. Can I defend why each ticket exists?
8. Can engineering start without guessing the product intent?
9. Can QA test the acceptance criteria?
10. Can stakeholders review the workflow and give feedback?

## Final PM Lesson

A Product Manager is not valuable because they know every answer immediately.

A Product Manager is valuable because they know how to structure uncertainty.

The job is to turn:

"Can we integrate this with the partner platform?"

into:

- actors;
- systems;
- journey;
- decisions;
- use cases;
- tickets;
- acceptance criteria;
- risks;
- validation plan.
