# LLM Assistant Layer Design

## Purpose

This document defines how an LLM assistant should be added to the PM Case Study Generator.

The goal is not to use AI as a shortcut for Product Management thinking.

The goal is to use AI inside a structured PM operating framework.

The LLM should help the PM:

- identify ambiguity;
- improve wording;
- suggest missing questions;
- classify decisions;
- strengthen PRDs;
- strengthen engineering tickets;
- detect weak acceptance criteria;
- expose risks and open questions.

The LLM should not replace product judgment.

---

## Core Principle

The PM owns the product reasoning.

The LLM supports the reasoning process.

A weak implementation would be:

"User enters a business request and the LLM invents a full PRD."

A stronger implementation is:

"User enters structured discovery inputs. The app applies the PM framework. The LLM reviews the structured output, identifies ambiguity, and suggests improvements."

---

## Why This Matters

The original learning moment behind this project was moving too quickly from business request to AI/automation.

The correct sequence is:

1. Understand the business goal.
2. Identify actors.
3. Map systems.
4. Clarify ownership.
5. Map the user journey.
6. Make product decisions explicit.
7. Define use cases.
8. Write requirements.
9. Create engineering-ready tickets.
10. Validate risks and open questions.

The LLM assistant must respect this sequence.

---

## LLM Responsibilities

## 1. Improve Generated Artifacts

The LLM can improve readability and structure of generated artifacts.

Allowed behavior:

- rewrite unclear sentences;
- improve section transitions;
- make PRD language more professional;
- make tickets more testable;
- improve executive summaries;
- remove repetition.

Not allowed:

- invent facts;
- invent APIs;
- invent confirmed stakeholder decisions;
- hide uncertainty;
- convert open questions into decisions without user confirmation.

---

## 2. Detect Missing PM Decisions

The LLM can inspect generated artifacts and identify missing decisions.

Examples:

- Authentication ownership is unclear.
- Data ownership is unclear.
- Approval flow is missing.
- Scope boundary is weak.
- MVP includes too much.
- Out-of-scope items are not explicit.
- User journey has a gap.
- Engineering tickets depend on unstated assumptions.

The LLM should classify each issue as:

- Missing decision;
- Needs validation;
- Scope risk;
- Technical dependency;
- Legal or compliance question;
- Stakeholder alignment issue.

---

## 3. Generate Follow-Up Discovery Questions

The LLM can suggest questions the PM should ask stakeholders.

Question categories:

- Business goal;
- Users and actors;
- Systems and ownership;
- Permissions;
- Data ownership;
- Workflow;
- MVP scope;
- Risks;
- Success metrics;
- Engineering dependencies;
- Legal/compliance.

The output should be practical and interview-ready.

---

## 4. Strengthen Engineering Tickets

The LLM can review generated tickets and suggest improvements.

Checks:

- Is the objective clear?
- Is the user story clear?
- Are acceptance criteria testable?
- Are dependencies explicit?
- Are edge cases covered?
- Are out-of-scope items clear?
- Does the ticket depend on unresolved product decisions?

The LLM should not silently rewrite tickets as if decisions were confirmed.

It should separate:

- suggested rewrite;
- unresolved assumptions;
- questions for PM;
- questions for engineering.

---

## 5. Classify Decisions

The LLM can classify product decisions into:

- Decided for MVP;
- Needs validation;
- Out of scope for MVP.

This is useful because PM work often fails when assumptions are hidden.

The LLM should flag weak decision wording.

Example weak wording:

"Maybe we use SSO if needed."

Better wording:

"For MVP planning, assume SSO is required. PartnerCRM is the identity provider. Technical feasibility still needs engineering validation."

---

## Non-Goals

The LLM assistant should not:

- replace discovery;
- replace stakeholder interviews;
- replace engineering validation;
- replace legal review;
- make business decisions alone;
- generate production requirements from one vague sentence;
- create false certainty;
- pretend unresolved questions are solved.

---

## Product Modes

## Mode 1 — Template Generator

Current Phase 1.1.

The app uses structured user inputs and deterministic templates.

No LLM is used.

## Mode 2 — LLM Review

The app generates artifacts first.

Then the LLM reviews them and returns:

- ambiguity warnings;
- missing decisions;
- weak acceptance criteria;
- follow-up questions;
- suggested improvements.

## Mode 3 — LLM Rewrite

The user can ask the LLM to improve selected sections.

Examples:

- improve PRD wording;
- improve executive summary;
- improve engineering tickets;
- improve acceptance criteria.

The user remains responsible for accepting or rejecting changes.

## Mode 4 — LLM Discovery Coach

The LLM interviews the user before generation.

It asks follow-up questions based on missing or weak inputs.

This mode should come after Mode 2 and Mode 3.

---

## Proposed Phase 2 Implementation

## Phase 2.1 — Add LLM Configuration

Add optional environment-based configuration:

- OPENAI_API_KEY;
- model name;
- enable/disable LLM features.

If no API key exists, the app should continue working in template-only mode.

## Phase 2.2 — Add Review Button

Add a button:

"Review generated artifacts with LLM"

The app sends the generated Markdown to the LLM and asks for:

- missing PM decisions;
- unclear assumptions;
- weak acceptance criteria;
- scope risks;
- suggested follow-up questions.

## Phase 2.3 — Add Rewrite Button

Add a button:

"Improve wording with LLM"

The app returns a polished version of the generated artifact while preserving all user-provided facts and open questions.

## Phase 2.4 — Add Discovery Questions Button

Add a button:

"Generate follow-up discovery questions"

The app returns questions grouped by PM category.

---

## Prompt Design Principles

The system prompt should tell the LLM:

- You are a PM assistant, not the product decision owner.
- Do not invent facts.
- Do not convert uncertainty into certainty.
- Separate decisions from assumptions.
- Flag missing information.
- Preserve out-of-scope boundaries.
- Make acceptance criteria testable.
- Prefer clear product language over vague implementation language.

---

## Example LLM Review Output

## Missing Decisions

1. Authentication ownership is assumed but not validated.
2. Data ownership is not explicit enough.
3. Approval responsibility is unclear.
4. Export format is not defined.
5. Success metrics are too generic.

## Follow-Up Questions

1. Which system owns authentication?
2. Which system owns customer/contact data?
3. Who approves the final output?
4. Is the MVP expected to export, send, or publish?
5. What is the smallest demo that proves value?

## Scope Risks

1. Stakeholders may expect production integration instead of MVP.
2. Email sending may introduce deliverability and consent complexity.
3. LLM generation may create compliance risk if not constrained.

---

## Success Criteria for the LLM Layer

The LLM layer is successful if it helps the PM produce better work without hiding ambiguity.

Success means:

- the PM sees missing decisions earlier;
- tickets become more testable;
- acceptance criteria become clearer;
- open questions are explicit;
- scope boundaries improve;
- stakeholders can review the output faster;
- engineering receives less ambiguous handoff.

Failure means:

- the LLM invents details;
- the LLM creates false confidence;
- the LLM hides unresolved decisions;
- the app becomes a generic PRD generator without PM discipline.

---

## Final Positioning

This project should not be positioned as:

"AI writes PRDs."

It should be positioned as:

"A PM operating framework with an AI assistant that helps structure ambiguity, identify missing decisions, and generate engineering-ready artifacts."

The value is not the LLM alone.

The value is the PM framework controlling how the LLM is used.
