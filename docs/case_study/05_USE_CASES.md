# USE CASES

## Purpose

This document converts the product journey and product decisions into concrete use cases.

A use case describes:

- who the user is;
- what the user wants to do;
- why it matters;
- what system behavior is expected;
- what decisions or dependencies affect implementation.

Use cases are the bridge between product thinking and engineering tickets.

## Case Study

ComplianceBrief x PartnerCRM — Newsletter Partnership Integration

## Use Case Summary

| ID | Use Case | Primary Actor | MVP Priority |
|---|---|---|---|
| UC-01 | Access ComplianceBrief through PartnerCRM | PartnerCRM User | Must Have |
| UC-02 | Check account-level content permissions | System / PartnerCRM User | Must Have |
| UC-03 | Browse and select approved content | PartnerCRM User | Must Have |
| UC-04 | Generate newsletter draft from selected content | PartnerCRM User | Must Have |
| UC-05 | Review, edit, and approve newsletter draft | PartnerCRM User | Must Have |
| UC-06 | Select CRM audience segment | PartnerCRM User | Should Have |
| UC-07 | Export newsletter draft | PartnerCRM User | Must Have |
| UC-08 | Log workflow events | System / Admin | Should Have |

---

# UC-01 — Access ComplianceBrief through PartnerCRM

## Primary Actor

PartnerCRM User

## Goal

Access the ComplianceBrief newsletter feature from inside PartnerCRM without a separate login.

## User Story

As a PartnerCRM user, I want to access the ComplianceBrief newsletter module through PartnerCRM, so that I can create newsletters without leaving my existing workflow.

## Trigger

The user clicks the ComplianceBrief feature inside PartnerCRM.

## Main Flow

1. User is logged into PartnerCRM.
2. User opens the ComplianceBrief module.
3. System checks whether the user's PartnerCRM account has the integration enabled.
4. System starts an SSO-based access flow.
5. User lands inside the ComplianceBrief newsletter experience.

## Product Decisions

- PartnerCRM is the user starting point.
- SSO is assumed for MVP planning.
- PartnerCRM is the identity provider.

## Acceptance Signals

- User can open the ComplianceBrief module from PartnerCRM.
- User does not need to create a separate ComplianceBrief login.
- Unauthorized users cannot access the module.
- The system shows a clear error or access message if access fails.

## Risks / Open Questions

- Which SSO standard is supported?
- Can PartnerCRM embed the module?
- How are users mapped between PartnerCRM and ComplianceBrief?

---

# UC-02 — Check Account-Level Content Permissions

## Primary Actor

System / PartnerCRM User

## Goal

Ensure the user only sees ComplianceBrief content approved for their partner account.

## User Story

As a PartnerCRM user, I want to see only the ComplianceBrief content my account is allowed to use, so that content access rules and partner restrictions are respected.

## Trigger

The user enters the ComplianceBrief module.

## Main Flow

1. System identifies the user's PartnerCRM account.
2. System checks whether the account has ComplianceBrief access.
3. System retrieves content approved for that account.
4. System hides restricted, draft, expired, or unavailable content.
5. User sees only approved content.

## Product Decisions

- Permissions are partner-account based for MVP.
- ComplianceBrief is the source of truth for approved content.
- Only approved content can be used in newsletters.

## Acceptance Signals

- Enabled accounts see approved content.
- Disabled accounts do not see content.
- Draft, expired, or restricted content is hidden.
- The user cannot generate a newsletter from unauthorized content.

## Risks / Open Questions

- Are permissions account-level enough for MVP?
- Will some partners need custom content?
- How is content expiration handled?

---

# UC-03 — Browse and Select Approved Content

## Primary Actor

PartnerCRM User

## Goal

Select approved ComplianceBrief content blocks to include in a newsletter.

## User Story

As a PartnerCRM user, I want to browse approved research content and select the most relevant blocks, so that I can create a newsletter for my customer audience.

## Trigger

The user enters the content library.

## Main Flow

1. User views a list of approved ComplianceBrief content.
2. User filters or scans content by date, topic, or summary.
3. User selects up to three content blocks.
4. System shows selected content in a draft input area.
5. User proceeds to newsletter generation.

## Product Decisions

- MVP allows up to three selected content blocks.
- Content should include metadata such as title, date, topic, and summary.
- Selected content becomes the only allowed input for generation.

## Acceptance Signals

- User can view approved content.
- User can select and deselect content blocks.
- User cannot select more than the MVP limit.
- Selected content is clearly visible before generation.

## Risks / Open Questions

- Is three content blocks the right MVP limit?
- Are images included?
- Does content need region or industry tags?

---

# UC-04 — Generate Newsletter Draft from Selected Content

## Primary Actor

PartnerCRM User

## Goal

Generate a newsletter draft using selected approved ComplianceBrief content.

## User Story

As a PartnerCRM user, I want the system to generate a newsletter draft from selected approved content, so that I can prepare customer communication faster.

## Trigger

The user clicks "Generate newsletter draft."

## Main Flow

1. User selects approved content blocks.
2. User clicks generate.
3. System generates a structured newsletter draft.
4. Draft includes title, introduction, sections, and call-to-action.
5. System displays source references used in the draft.

## Product Decisions

- Generation is LLM-assisted for MVP planning.
- Generation must be constrained to selected approved content.
- Unsupported claims are not allowed.
- Source references must be visible.

## Acceptance Signals

- Draft is generated only from selected content.
- Draft shows source content references.
- Draft does not use unauthorized content.
- User can review the draft before approval.

## Risks / Open Questions

- Which LLM or generation service is allowed?
- How do we technically restrict generation to approved content?
- How should unsupported claims be detected or prevented?
- Does legal/compliance need to approve generated text?

---

# UC-05 — Review, Edit, and Approve Newsletter Draft

## Primary Actor

PartnerCRM User

## Goal

Review and approve the newsletter before export or distribution.

## User Story

As a PartnerCRM user, I want to review, edit, and approve the newsletter draft, so that I keep control over customer-facing communication.

## Trigger

A draft has been generated.

## Main Flow

1. User reviews the generated draft.
2. User edits title, introduction, sections, or call-to-action.
3. System keeps source references visible.
4. User previews the final newsletter.
5. User explicitly approves the draft.

## Product Decisions

- Human approval is required before export.
- Users can edit generated drafts.
- Source summary must remain visible before approval.

## Acceptance Signals

- User can edit draft sections.
- User can preview the final draft.
- User cannot export without approval.
- System records approval timestamp and user.

## Risks / Open Questions

- Should any sections be locked?
- Do edits need to be logged?
- Does editing affect compliance traceability?

---

# UC-06 — Select CRM Audience Segment

## Primary Actor

PartnerCRM User

## Goal

Select which CRM contacts or segments should receive the newsletter.

## User Story

As a PartnerCRM user, I want to select a CRM audience segment, so that the newsletter is prepared for the right customer group.

## Trigger

The user has an approved newsletter draft.

## Main Flow

1. User opens audience selection.
2. System shows available PartnerCRM segments.
3. User selects one segment.
4. System displays audience metadata, such as segment name and estimated recipient count.
5. System does not expose or store raw recipient data inside ComplianceBrief.

## Product Decisions

- PartnerCRM owns recipient data.
- ComplianceBrief does not store recipient-level personal data in MVP.
- Real email sending is out of scope for MVP.

## Acceptance Signals

- User can select a CRM segment.
- System displays selected segment metadata.
- ComplianceBrief does not store raw contact data.
- User can proceed to export after audience selection.

## Risks / Open Questions

- Does PartnerCRM expose segment metadata through API?
- Is audience selection required for MVP export?
- Who owns consent and unsubscribe rules?

---

# UC-07 — Export Newsletter Draft

## Primary Actor

PartnerCRM User

## Goal

Export an approved newsletter draft for use in the partner workflow.

## User Story

As a PartnerCRM user, I want to export the approved newsletter draft, so that it can be used in the PartnerCRM communication workflow.

## Trigger

The user has approved the final draft.

## Main Flow

1. User clicks export.
2. System confirms the draft has been approved.
3. System creates an export-ready version.
4. User receives an export format such as HTML, markdown, or structured content.
5. System records the export event.

## Product Decisions

- Real sending is out of scope for MVP.
- MVP supports export-ready output.
- PartnerCRM owns final distribution.

## Acceptance Signals

- User cannot export an unapproved draft.
- Export includes final newsletter content.
- Export includes metadata needed by PartnerCRM.
- Export event is logged.

## Risks / Open Questions

- What export format does PartnerCRM require?
- Should export include images?
- Should export preserve source references?

---

# UC-08 — Log Workflow Events

## Primary Actor

System / Admin

## Goal

Record key workflow events for traceability and future analytics.

## User Story

As a ComplianceBrief admin, I want key newsletter workflow events to be logged, so that usage and approvals can be traced later.

## Trigger

User performs key actions in the workflow.

## Main Flow

1. System logs module open.
2. System logs content selection.
3. System logs draft generation.
4. System logs draft approval.
5. System logs export event.
6. Admin or internal team can inspect basic event records.

## Product Decisions

- MVP includes lightweight event logging.
- Full analytics dashboard is out of scope.
- Basic audit traceability is required.

## Acceptance Signals

- Key workflow events are logged.
- Logs include user, account, timestamp, and event type.
- Approval and export events are traceable.
- No unnecessary personal recipient data is stored.

## Risks / Open Questions

- Who can access logs?
- How long should logs be retained?
- Which events are legally or commercially required?

---

# Use Cases to Engineering Ticket Mapping

| Use Case | Future Engineering Ticket |
|---|---|
| UC-01 | Implement PartnerCRM SSO access |
| UC-02 | Implement account-level content permissions |
| UC-03 | Build approved content library and selection flow |
| UC-04 | Generate newsletter draft from selected content |
| UC-05 | Build review, edit, and approval workflow |
| UC-06 | Add CRM audience segment selection |
| UC-07 | Export approved newsletter draft |
| UC-08 | Log workflow events |

## PM Lesson

A use case is not yet a ticket.

A use case explains the product behavior.

A ticket tells engineering what to build.

The PM should first clarify use cases, then translate them into engineering-ready tickets with requirements, acceptance criteria, dependencies, and edge cases.
