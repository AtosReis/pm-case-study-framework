# PRODUCT DECISIONS LOG

## Purpose

This document captures the product decisions required before engineering tickets are written.

A Product Manager should not pass unresolved ambiguity to engineering as open-ended implementation work.

Bad handoff:

"If we use an LLM, maybe it should only use client files."

Better handoff:

"For MVP, newsletter generation will be LLM-assisted and restricted to selected approved ComplianceBrief content. The generated draft must display source references before approval."

The PM does not need to make every decision alone.

But the PM must identify which decisions are required, propose a direction, and document what needs product, engineering, legal, or client approval.

## Decision Principles

### 1. Do not write tickets before key product assumptions are explicit

Engineering tickets should not start from vague statements like:

- integrate the platforms;
- automate the workflow;
- use AI somehow;
- connect the CRM;
- make it seamless.

They should start from defined product decisions.

### 2. Separate product decisions from technical implementation

Product decision:

PartnerCRM users should access ComplianceBrief through SSO.

Technical implementation:

The CTO/engineering team decides the exact SSO protocol, provider configuration, token handling, and security architecture.

### 3. Mark unresolved decisions clearly

A decision can have one of three statuses:

- Decided for MVP
- Needs validation
- Out of scope for MVP

### 4. Avoid hidden decisions inside tickets

Every ticket should be traceable to one or more product decisions.

## MVP Product Decisions

## Decision 1 — User Starting Point

### Decision

The user starts inside PartnerCRM.

### Rationale

PartnerCRM is the larger partner platform and owns the user workflow, CRM contacts, and customer context.

### MVP Implication

ComplianceBrief functionality should appear as an embedded module or partner feature inside PartnerCRM.

### Status

Decided for MVP.

## Decision 2 — Authentication

### Decision

For MVP planning, assume SSO is required.

PartnerCRM is the identity provider.

### Rationale

The partner user should not need a separate ComplianceBrief login. A separate login would create friction and weaken the unified experience.

### MVP Implication

Engineering needs a story for SSO access and identity mapping.

### Status

Decided for MVP, technical feasibility to be validated.

## Decision 3 — Permission Model

### Decision

For MVP, permissions are partner-account based.

If a PartnerCRM account is enabled for ComplianceBrief, authorized users in that account can access approved ComplianceBrief content.

### Rationale

User-level and role-level permissions may be needed later, but account-level permissions are simpler for MVP.

### MVP Implication

Engineering needs a story for checking account access before rendering content.

### Status

Decided for MVP.

## Decision 4 — Content Source of Truth

### Decision

ComplianceBrief is the source of truth for research content.

### Rationale

ComplianceBrief owns proprietary compliance research, content approval, metadata, and content restrictions.

### MVP Implication

PartnerCRM should render approved content from ComplianceBrief, not duplicate or manually recreate it.

### Status

Decided for MVP.

## Decision 5 — Content Eligibility

### Decision

Only approved ComplianceBrief content can be used in newsletter generation.

### Rationale

The system must avoid using draft, expired, restricted, or unapproved content.

### MVP Implication

Content must have an approval status and availability flag.

### Status

Decided for MVP.

## Decision 6 — Branding

### Decision

For MVP, the newsletter is co-branded as PartnerCRM powered by ComplianceBrief.

### Rationale

This preserves the partner platform experience while still giving ComplianceBrief attribution.

### MVP Implication

The newsletter preview should show both partner and client branding.

### Status

Needs validation with business stakeholders.

## Decision 7 — Newsletter Generation Method

### Decision

For MVP, newsletter generation is LLM-assisted but constrained to selected approved content.

### Rationale

The value proposition includes faster newsletter creation, but the system must not invent unsupported claims.

### MVP Implication

The generation ticket must specify:

- input is selected approved content only;
- output must show source references;
- unsupported claims are not allowed;
- user review is mandatory before export.

### Status

Decided for MVP, technical and policy feasibility to be validated.

## Decision 8 — Human Review

### Decision

Human approval is required before export or sending.

### Rationale

Compliance and professional communication require user review before external distribution.

### MVP Implication

Engineering needs a story for review, edit, preview, and final approval.

### Status

Decided for MVP.

## Decision 9 — Recipient Data Ownership

### Decision

PartnerCRM owns recipient selection and customer/contact data.

ComplianceBrief should not store recipient-level personal data in MVP.

### Rationale

PartnerCRM already owns CRM contacts, segmentation, consent, and customer records.

### MVP Implication

The MVP should reference selected audience metadata but avoid storing raw contact data on the ComplianceBrief side.

### Status

Decided for MVP.

## Decision 10 — Distribution

### Decision

Real email sending is out of scope for MVP.

The MVP prepares an export-ready newsletter draft.

### Rationale

Distribution introduces additional complexity:

- deliverability;
- unsubscribe;
- consent;
- tracking;
- failure handling;
- email provider integration.

For MVP, export is enough to validate the workflow.

### MVP Implication

Engineering should build export/preview, not sending infrastructure.

### Status

Out of scope for MVP.

## Decision 11 — Analytics

### Decision

For MVP, log core workflow events only.

Events:

- module opened;
- content selected;
- draft generated;
- draft approved;
- export created.

### Rationale

Detailed analytics are useful but not necessary for the first build.

### MVP Implication

Engineering needs lightweight event logging.

### Status

Decided for MVP.

## Decision 12 — Audit and Compliance

### Decision

For MVP, store basic audit events but do not build a full compliance dashboard.

### Rationale

The workflow needs traceability, but a full audit console belongs in a later version.

### MVP Implication

Generated drafts and approvals should be traceable by user, timestamp, and content sources.

### Status

Decided for MVP.

## Decision 13 — Newsletter Editing

### Decision

Users can edit generated newsletter drafts before approval.

### Rationale

The generated draft should accelerate work, not remove user control.

### MVP Implication

Engineering needs editable draft sections and a final preview before export.

### Status

Decided for MVP.

## Decision 14 — Source References

### Decision

Generated newsletters must display which source content blocks were used.

### Rationale

This supports trust, review, and compliance.

### MVP Implication

Each generated draft should include a source summary visible before approval.

### Status

Decided for MVP.

## Decision 15 — MVP Scope Boundary

### Decision

MVP includes:

- embedded PartnerCRM entry point;
- simulated SSO assumption;
- content permission check;
- approved content library;
- content selection;
- constrained draft generation;
- review/edit;
- recipient segment selection;
- final approval;
- export-ready newsletter;
- basic event logging.

MVP excludes:

- real SSO implementation;
- real CRM API;
- real LLM API;
- real email sending;
- advanced analytics;
- billing;
- marketplace listing;
- multi-partner configuration;
- legal approval workflow.

### Status

Decided for MVP.

## Open Questions

These questions must be answered before production implementation:

1. Which SSO standard does PartnerCRM support?
2. Does PartnerCRM allow embedded partner modules?
3. What APIs are available for contacts and segments?
4. Can PartnerCRM provide audience metadata without exposing raw contacts?
5. What content metadata does ComplianceBrief already store?
6. Who approves content for partner use?
7. Are there legal restrictions on modifying ComplianceBrief content?
8. Which LLM or generation service is allowed?
9. Are generated drafts stored by ComplianceBrief, PartnerCRM, or both?
10. Who owns unsubscribe and email consent?
11. Does the partner require white-label branding?
12. What analytics are required for the first client demo?

## PM Lesson

The PM's job is not to guess everything perfectly.

The PM's job is to make ambiguity visible and manageable.

A strong PM says:

- this is decided;
- this needs validation;
- this is out of scope;
- this belongs to product;
- this belongs to engineering;
- this belongs to legal or business stakeholders.

Then engineering can build with clarity.
