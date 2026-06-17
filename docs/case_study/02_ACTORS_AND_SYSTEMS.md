# ACTORS AND SYSTEMS MAP

## Purpose

This document maps the people, roles, systems, and ownership boundaries involved in the fictional case study.

A Product Manager should not start by writing tickets or proposing automation.

A Product Manager should first understand:

- who is using the product;
- where the user starts;
- which system owns authentication;
- which system owns the data;
- which system owns permissions;
- which system owns the final output;
- who approves, sends, receives, or audits the workflow.

## Case Study Context

ComplianceBrief produces weekly compliance research.

PartnerCRM is a larger CRM platform used by sales and customer-success teams.

The business request is:

"Integrate ComplianceBrief's newsletter product with PartnerCRM so PartnerCRM users can create newsletters using ComplianceBrief content."

## Primary Actors

### 1. PartnerCRM User

This is the main user of the integrated workflow.

Example:

A customer-success manager working inside PartnerCRM who wants to send a compliance update to selected customers.

Primary goals:

- access ComplianceBrief content without leaving PartnerCRM;
- select approved research content;
- create a newsletter draft;
- select CRM contacts;
- prepare or send the newsletter.

Key questions:

- Does this user need a separate ComplianceBrief login?
- What ComplianceBrief content can this user access?
- Can this user edit generated newsletter content?
- Can this user send directly, or only prepare a draft?

## 2. ComplianceBrief Admin

This user manages the ComplianceBrief side.

Primary goals:

- upload or approve weekly research content;
- define which content is available to partners;
- control branding and content usage rules;
- monitor usage.

Key questions:

- Who approves content before it becomes available?
- Can content be partner-specific?
- Can access be revoked?
- Is content branded as ComplianceBrief, PartnerCRM, or white-label?

## 3. PartnerCRM Admin

This user manages the PartnerCRM side.

Primary goals:

- enable or disable the ComplianceBrief integration;
- manage which internal users can access the feature;
- define CRM data access rules;
- ensure the integration respects partner platform permissions.

Key questions:

- Which PartnerCRM accounts get access?
- Which users inside those accounts get access?
- Are permissions inherited from PartnerCRM roles?
- Can an admin disable the integration?

## 4. End Recipient

This is the final person who receives the newsletter.

Example:

A client or prospect in the PartnerCRM contact database.

Primary expectations:

- receive relevant, approved, professional content;
- not receive unauthorized or incorrect information;
- have unsubscribe/privacy expectations respected.

Key questions:

- Does PartnerCRM already handle email consent?
- Does the newsletter use PartnerCRM's email infrastructure?
- Who is responsible for unsubscribe and compliance?

## 5. Internal Product / Engineering Team

This is the team building or coordinating the integration.

Primary goals:

- understand the required user flow;
- build the integration safely;
- avoid ambiguous requirements;
- validate permissions, data ownership, and user experience.

Key questions:

- What is MVP?
- What is out of scope?
- Which APIs are available?
- What decisions are already made?
- What needs product/technical approval before implementation?

## Systems Involved

### 1. PartnerCRM

Role:

The user's starting point.

Likely responsibilities:

- user login;
- CRM contacts;
- customer segmentation;
- possibly email distribution;
- partner-side permissions;
- user interface container for the integration.

Important PM questions:

- Does the workflow live fully inside PartnerCRM?
- Is the integration embedded, linked, or API-based?
- Does PartnerCRM own the contact list?
- Does PartnerCRM own distribution?

## 2. ComplianceBrief Content Platform

Role:

The source of proprietary compliance research content.

Likely responsibilities:

- storing approved content;
- tagging content by topic, sector, region, or partner;
- controlling content availability;
- possibly exposing content via API.

Important PM questions:

- What content is eligible for partner use?
- Are images included?
- Are there content restrictions?
- Is content versioned?
- Can old content expire?

## 3. Authentication / SSO Layer

Role:

Controls whether a PartnerCRM user can access ComplianceBrief functionality without separate login.

Likely responsibilities:

- single sign-on;
- identity mapping;
- session handling;
- permission inheritance.

Important PM questions:

- Is SSO required for MVP?
- Which system is identity provider?
- How does PartnerCRM user identity map to ComplianceBrief access?
- What happens when a user loses access?

## 4. Newsletter Generation Service

Role:

Transforms selected content into a newsletter draft.

Could be:

- rules-based template generation;
- LLM-assisted generation;
- a client-owned generation service;
- a partner-owned generation service.

Important PM questions:

- Is generation automated in MVP?
- Which system owns generation?
- Is the LLM allowed to use only approved content?
- Is human approval required before sending?
- How do we prevent unsupported claims?

## 5. Distribution / Email Service

Role:

Sends, schedules, exports, or prepares the final newsletter.

Could be owned by:

- PartnerCRM;
- ComplianceBrief;
- a third-party email provider;
- manual export in MVP.

Important PM questions:

- Does MVP send emails or only export a draft?
- Who owns unsubscribe/compliance?
- Are send events tracked?
- Are open/click metrics required?

## 6. Analytics / Audit Layer

Role:

Tracks usage, generation, approval, and distribution.

Important PM questions:

- What should be logged?
- Who can view analytics?
- What is needed for MVP?
- What is needed for compliance or audit?
- Are generated newsletters stored?

## Core Product Ownership Questions

Before writing tickets, the PM must clarify:

1. Who owns login?
2. Who owns content?
3. Who owns contacts?
4. Who owns generation?
5. Who owns approval?
6. Who owns sending?
7. Who owns analytics?
8. Who owns compliance and audit responsibility?

## Simple Analogy

Imagine a restaurant partnership.

ComplianceBrief is the chef with the recipes.

PartnerCRM is the restaurant where customers already sit.

The integration is not simply "automate cooking."

The PM must define:

- who is allowed into the kitchen;
- which recipes can be used;
- whose logo appears on the menu;
- who chooses the dish;
- who approves the final plate;
- who serves it to the customer;
- who handles complaints or allergies.

Only after that can the kitchen team build the process.

## PM Lesson

A weak PM jumps to solution.

A stronger PM first maps:

- actors;
- systems;
- ownership;
- permissions;
- decisions;
- risks.

Then the PM writes tickets.
