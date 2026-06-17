# WORKFLOW AND ARCHITECTURE MAP

## Purpose

This document translates the PRD into a visual product workflow and a high-level system responsibility map.

The goal is to make the case study easier to understand for:

- founders;
- product leaders;
- engineering leaders;
- recruiters;
- hiring managers;
- future clients.

## Product Scenario

ComplianceBrief produces approved compliance research content.

PartnerCRM owns the user workflow, CRM contacts, and customer segments.

The integration allows PartnerCRM users to generate newsletter drafts using approved ComplianceBrief content.

## Visual Workflow

![Workflow and system responsibility map](../../assets/diagrams/mermaid-diagram.png)

## PM Interpretation of the Workflow

This is not a production architecture.

It is a product architecture map.

Its purpose is to clarify:

- where the user starts;
- which system owns authentication;
- which system owns content;
- which system owns contacts;
- where generation happens;
- where approval happens;
- what should be logged.

## End-to-End Product Flow

1. PartnerCRM user starts inside PartnerCRM.
2. User opens the ComplianceBrief module.
3. System performs SSO and account access check.
4. If unauthorized, user sees an access-denied state.
5. If authorized, system loads approved ComplianceBrief content.
6. User selects up to three content blocks.
7. System generates a newsletter draft.
8. Draft is shown with source references.
9. User reviews and edits the draft.
10. User explicitly approves the draft.
11. User selects a PartnerCRM audience segment.
12. System exports the approved newsletter draft.
13. System logs approval and export events.

## Ownership Boundaries

| Capability | Owner for MVP |
|---|---|
| User login | PartnerCRM |
| Identity provider | PartnerCRM |
| CRM contacts | PartnerCRM |
| Audience segments | PartnerCRM |
| Research content | ComplianceBrief |
| Content approval | ComplianceBrief |
| Content permissions | ComplianceBrief |
| Newsletter generation | Generation service constrained by ComplianceBrief content |
| Review and approval | PartnerCRM user |
| Export | Integration workflow |
| Event logs | Shared/internal integration layer |

## MVP Workflow States

| State | Description |
|---|---|
| Access requested | User opens ComplianceBrief module |
| Access denied | User/account is not authorized |
| Content available | Approved content is loaded |
| Content selected | User selects eligible content blocks |
| Draft generated | Newsletter draft is created |
| Draft reviewed | User reviews and edits draft |
| Draft approved | User explicitly approves final draft |
| Audience selected | User selects CRM segment metadata |
| Export created | Approved newsletter is exported |
| Events logged | Key workflow events are recorded |

## Key Failure States

| Failure State | Product Behavior |
|---|---|
| Unauthorized account | Show access-denied state |
| No approved content | Show empty content library state |
| Too many content blocks selected | Block selection above MVP limit |
| Generation fails | Show retry/error state |
| Draft not approved | Block export |
| Segment unavailable | Ask user to select another segment |
| Export fails | Show export failure state |
| Logging fails | Record failure where possible without blocking user unnecessarily |

## Why This Matters for PM Work

The workflow map forces the PM to think before writing tickets.

Without this map, the requirement could easily become:

"Integrate newsletter product with CRM."

That is too vague for engineering.

With this map, the PM can create clear tickets for:

- access;
- permissioning;
- content library;
- generation;
- review and approval;
- audience selection;
- export;
- logging.

## PM Lesson

A strong Product Manager does not need to code the architecture.

But a strong Product Manager must understand enough of the system boundaries to avoid writing vague or misleading requirements.

The PM should be able to say:

- this system owns identity;
- this system owns content;
- this system owns contacts;
- this action requires approval;
- this event must be logged;
- this is MVP;
- this is out of scope.
