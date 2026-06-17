# Executive Summary

## PM Case Study Framework

### From Interview Failure to Product Operating System

This project is a portfolio case study about turning a weak interview moment into a structured Product Manager learning system.

During a Product Manager interview, I was given a live product scenario involving a B2B partnership: a client product that generates newsletters from proprietary research content, and a larger partner platform with CRM/customer contacts.

My mistake was moving too quickly toward AI, automation, and implementation before properly decomposing the product problem.

This repository is my structured response to that lesson.

It shows how I rebuilt the scenario using a stronger Product Manager process:

1. Clarify the business goal.
2. Identify actors and systems.
3. Map the user journey.
4. Make product decisions explicit.
5. Define use cases.
6. Write a PRD.
7. Translate requirements into engineering-ready tickets.
8. Demonstrate the final user-facing output.

---

## Applied Scenario

The fictional case study is:

ComplianceBrief x PartnerCRM — Newsletter Partnership Integration

ComplianceBrief produces weekly compliance research.

PartnerCRM is a larger CRM platform used by sales and customer-success teams.

The ambiguous business request is:

"Integrate our newsletter product with a larger partner CRM so their users can create newsletters using our content."

The PM interpretation is that this is not simply a newsletter generator.

It is a product integration problem involving:

- authentication;
- content permissions;
- CRM data ownership;
- user journey;
- newsletter generation;
- human approval;
- export boundaries;
- audit logging;
- engineering handoff.

---

## What the Project Demonstrates

This project demonstrates the ability to turn ambiguity into structured execution.

It includes:

- a reusable PM operating framework;
- a PM question bank;
- actors and systems mapping;
- user journey mapping;
- product decision logging;
- use cases;
- a PRD;
- engineering tickets;
- reusable PM templates;
- workflow and architecture map;
- sample newsletter output.

---

## Core PM Lesson

A Product Manager should not pass vague ambiguity directly to engineering.

A vague request like:

"Integrate the newsletter product with the partner CRM."

is not enough.

The PM must clarify:

- Who is the user?
- Where does the user start?
- Which system owns login?
- Which system owns content?
- Which system owns contacts?
- Which system owns permissions?
- Is the experience embedded, exported, or API-based?
- Is SSO required?
- Is AI used?
- Which content can AI use?
- Is human approval required?
- What is MVP?
- What is out of scope?

Only after that should the PM write engineering tickets.

---

## Final Product Flow

The MVP flow is:

1. PartnerCRM user opens the ComplianceBrief module.
2. System validates access through SSO and account-level permissions.
3. User browses approved ComplianceBrief content.
4. User selects up to three content blocks.
5. System generates a newsletter draft.
6. Draft shows source references.
7. User reviews and edits the draft.
8. User selects a CRM audience segment.
9. User approves the final draft.
10. System exports the approved newsletter.
11. System logs key workflow events.

---

## Engineering Handoff

The case study produces eight engineering ticket themes:

1. PartnerCRM SSO access.
2. Account-level content permissions.
3. Approved content library and selection flow.
4. Newsletter draft generation from selected content.
5. Review, edit, and approval workflow.
6. CRM audience segment selection.
7. Export of approved newsletter draft.
8. Core workflow event logging.

Each ticket includes:

- objective;
- user story;
- product decisions;
- functional requirements;
- acceptance criteria;
- dependencies;
- edge cases;
- out-of-scope notes.

---

## Why This Matters

This project is not about pretending that one case study creates seniority overnight.

It is about showing:

- self-awareness;
- coachability;
- structured thinking;
- ability to learn from feedback;
- product judgment;
- engineering handoff discipline;
- ability to convert ambiguity into execution.

The project turns a failed interview moment into a reusable PM operating framework.

---

## Portfolio Value

This repository can be used as:

- a Product Manager portfolio artifact;
- a reusable PM checklist;
- a case study for product interviews;
- a framework for client discovery;
- a reference for writing better engineering tickets;
- evidence of fast learning and practical execution.

## Repository

https://github.com/AtosReis/pm-case-study-framework
