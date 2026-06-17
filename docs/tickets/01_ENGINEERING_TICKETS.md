# ENGINEERING TICKETS

## Purpose

This document translates the product use cases into engineering-ready tickets.

Each ticket should give engineering enough clarity to start implementation discussions without having to reinterpret the product idea from scratch.

A good ticket includes:

- objective;
- user story;
- functional requirements;
- acceptance criteria;
- dependencies;
- edge cases;
- out-of-scope notes.

## Case Study

ComplianceBrief x PartnerCRM — Newsletter Partnership Integration

## MVP Ticket List

| Ticket ID | Title | Priority |
|---|---|---|
| ENG-01 | Implement PartnerCRM SSO Access Flow | Must Have |
| ENG-02 | Implement Account-Level Content Permission Check | Must Have |
| ENG-03 | Build Approved Content Library and Selection Flow | Must Have |
| ENG-04 | Generate Newsletter Draft from Selected Approved Content | Must Have |
| ENG-05 | Build Review, Edit, and Approval Workflow | Must Have |
| ENG-06 | Add CRM Audience Segment Selection | Should Have |
| ENG-07 | Export Approved Newsletter Draft | Must Have |
| ENG-08 | Log Core Workflow Events | Should Have |

---

# ENG-01 — Implement PartnerCRM SSO Access Flow

## Objective

Allow a PartnerCRM user to access the ComplianceBrief newsletter module without creating a separate ComplianceBrief login.

## Related Use Case

UC-01 — Access ComplianceBrief through PartnerCRM

## User Story

As a PartnerCRM user, I want to open the ComplianceBrief newsletter module through PartnerCRM, so that I can create newsletters without leaving my existing workflow.

## Product Decisions

- PartnerCRM is the user starting point.
- SSO is assumed for MVP planning.
- PartnerCRM is the identity provider.
- Unauthorized users should not access the module.

## Functional Requirements

1. Display the ComplianceBrief module entry point inside PartnerCRM.
2. Trigger an SSO-based access flow when the module is opened.
3. Identify the PartnerCRM account associated with the user.
4. Confirm whether the account has ComplianceBrief access enabled.
5. Allow authorized users to enter the ComplianceBrief module.
6. Show a clear access-denied state for unauthorized users.

## Acceptance Criteria

- Given an authorized PartnerCRM user, when they open the ComplianceBrief module, then they can access the module without a separate login.
- Given an unauthorized PartnerCRM user, when they open the module, then they see an access-denied message.
- Given an expired or invalid session, when the user opens the module, then the system asks the user to re-authenticate through PartnerCRM.
- The user experience should not require manual ComplianceBrief credential creation.

## Dependencies

- PartnerCRM identity provider details.
- SSO protocol decision.
- Account mapping between PartnerCRM and ComplianceBrief.
- Product confirmation of access-denied copy.

## Edge Cases

- User belongs to multiple PartnerCRM accounts.
- Account has integration enabled, but user role is restricted.
- SSO token is valid but account mapping fails.
- PartnerCRM session expires during workflow.

## Out of Scope

- Production-grade SSO implementation details.
- Multi-partner marketplace installation flow.
- User-level role management beyond MVP access check.

---

# ENG-02 — Implement Account-Level Content Permission Check

## Objective

Ensure that PartnerCRM users can only view ComplianceBrief content approved for their partner account.

## Related Use Case

UC-02 — Check Account-Level Content Permissions

## User Story

As a PartnerCRM user, I want to see only the ComplianceBrief content my account is allowed to use, so that content restrictions and partner agreements are respected.

## Product Decisions

- Permissions are partner-account based for MVP.
- ComplianceBrief is the source of truth for approved content.
- Draft, expired, restricted, or unavailable content must not be shown.

## Functional Requirements

1. Identify the user's PartnerCRM account after access.
2. Retrieve the list of approved ComplianceBrief content available to that account.
3. Exclude content that is draft, expired, restricted, or unavailable.
4. Return only content blocks eligible for newsletter generation.
5. Prevent unauthorized content from being used as generation input.

## Acceptance Criteria

- Given an enabled partner account, when content is loaded, then only approved content is displayed.
- Given content marked as draft, when content is loaded, then the draft content is not displayed.
- Given content marked as expired, when content is loaded, then expired content is not displayed.
- Given restricted content, when the account is not authorized, then the content is not displayed and cannot be selected.
- Generation input must only include selected content that passed the permission check.

## Dependencies

- Content metadata model.
- Account-content permission rules.
- Content approval status.
- Content expiration rules.

## Edge Cases

- Account has no approved content.
- Content expires after being selected but before generation.
- Account access is revoked during an active session.
- Content metadata is missing or inconsistent.

## Out of Scope

- User-level content personalization.
- Advanced role-based access control.
- Partner-specific content pricing.

---

# ENG-03 — Build Approved Content Library and Selection Flow

## Objective

Allow users to browse approved ComplianceBrief content and select up to three content blocks for newsletter generation.

## Related Use Case

UC-03 — Browse and Select Approved Content

## User Story

As a PartnerCRM user, I want to browse approved research content and select the most relevant content blocks, so that I can create a newsletter for my customer audience.

## Product Decisions

- Users can select up to three content blocks for MVP.
- Content should show title, date, topic, and summary.
- Selected content becomes the only allowed input for generation.

## Functional Requirements

1. Display approved content in a content library view.
2. Show title, summary, topic, and publication date for each content block.
3. Allow users to select and deselect content blocks.
4. Limit selection to three content blocks.
5. Show selected content in a visible selection panel.
6. Disable or warn when the user tries to exceed the selection limit.
7. Allow the user to proceed to generation only after selecting at least one content block.

## Acceptance Criteria

- User can view a list of approved content blocks.
- User can select one, two, or three content blocks.
- User cannot select more than three content blocks.
- Selected content is visible before generation.
- User cannot generate a newsletter with zero selected content.
- Deselected content is removed from the generation input.

## Dependencies

- Content permission service from ENG-02.
- Content metadata fields.
- UX copy for empty state and selection limit.

## Edge Cases

- No content available.
- Content list loads slowly or fails.
- User selects content, then content becomes unavailable.
- User refreshes page after selection.

## Out of Scope

- Advanced search.
- Personalized recommendations.
- Multi-language content.
- Content image editing.

---

# ENG-04 — Generate Newsletter Draft from Selected Approved Content

## Objective

Generate a structured newsletter draft from selected approved ComplianceBrief content.

## Related Use Case

UC-04 — Generate Newsletter Draft from Selected Content

## User Story

As a PartnerCRM user, I want the system to generate a newsletter draft from selected approved content, so that I can prepare customer communication faster.

## Product Decisions

- Generation is LLM-assisted for MVP planning.
- Generation must be constrained to selected approved content.
- Source references must be visible.
- Unsupported claims are not allowed.
- User review is mandatory before export.

## Functional Requirements

1. Accept selected approved content blocks as generation input.
2. Generate a newsletter draft with:
   - title;
   - introduction;
   - content sections;
   - call-to-action.
3. Display source references used in the generated draft.
4. Prevent generation from unapproved or unauthorized content.
5. Show a clear error if generation fails.
6. Store draft state for review and editing.

## Acceptance Criteria

- Given selected approved content, when the user clicks generate, then the system creates a structured newsletter draft.
- The generated draft includes title, introduction, sections, and call-to-action.
- The generated draft displays which source content blocks were used.
- The system does not generate from unauthorized content.
- The user can proceed to review after generation.
- If generation fails, the user sees a clear retry or error state.

## Dependencies

- Approved content selection from ENG-03.
- Generation service decision.
- Source reference format.
- Product/legal policy on unsupported claims.

## Edge Cases

- Generation service unavailable.
- Selected content is too short.
- Selected content has conflicting topics.
- Selected content becomes unavailable during generation.
- Generated draft is empty or malformed.

## Out of Scope

- Real production LLM integration.
- Automated legal approval.
- Sending newsletter directly.
- Advanced personalization by recipient.

---

# ENG-05 — Build Review, Edit, and Approval Workflow

## Objective

Allow users to review, edit, preview, and approve a generated newsletter draft before export.

## Related Use Case

UC-05 — Review, Edit, and Approve Newsletter Draft

## User Story

As a PartnerCRM user, I want to review, edit, and approve the generated newsletter draft, so that I keep control over customer-facing communication.

## Product Decisions

- Human approval is required before export.
- Users can edit generated drafts.
- Source references remain visible before approval.
- Approval event must be recorded.

## Functional Requirements

1. Display the generated newsletter draft in an editable view.
2. Allow editing of title, introduction, sections, and call-to-action.
3. Display source content summary near the draft.
4. Provide preview mode before approval.
5. Require explicit approval before export.
6. Record approval timestamp and approving user.
7. Prevent export until approval is completed.

## Acceptance Criteria

- User can edit draft sections.
- User can preview the final newsletter.
- User can approve the draft.
- User cannot export an unapproved draft.
- Approval event includes user, timestamp, and draft identifier.
- Source references remain visible before approval.

## Dependencies

- Draft generation from ENG-04.
- Event logging from ENG-08.
- UX decision on edit and preview layout.

## Edge Cases

- User edits draft and then regenerates content.
- User abandons draft before approval.
- User approves draft, then tries to edit again.
- Approval fails due to session timeout.

## Out of Scope

- Multi-user approval workflow.
- Legal review queue.
- Version comparison between draft edits.
- Commenting and collaboration.

---

# ENG-06 — Add CRM Audience Segment Selection

## Objective

Allow the user to select a CRM audience segment without storing raw recipient-level personal data in ComplianceBrief.

## Related Use Case

UC-06 — Select CRM Audience Segment

## User Story

As a PartnerCRM user, I want to select a CRM audience segment, so that the newsletter is prepared for the right customer group.

## Product Decisions

- PartnerCRM owns recipient data.
- ComplianceBrief does not store raw contact data in MVP.
- MVP uses segment metadata only.
- Real sending is out of scope.

## Functional Requirements

1. Display available CRM audience segments.
2. Allow user to select one segment.
3. Show segment name and estimated recipient count.
4. Store selected segment reference or metadata only.
5. Do not store raw recipient-level personal data in ComplianceBrief.
6. Allow the user to proceed to export after segment selection.

## Acceptance Criteria

- User can select one CRM segment.
- Selected segment metadata is visible before export.
- Raw recipient data is not stored in ComplianceBrief.
- If no segments are available, user sees an empty state.
- User can change selected segment before export.

## Dependencies

- PartnerCRM segment API or simulated segment data.
- Data ownership confirmation.
- Privacy requirements.

## Edge Cases

- Segment is deleted after selection.
- Segment has zero recipients.
- User lacks permission to view segments.
- Segment metadata fails to load.

## Out of Scope

- Manual recipient selection.
- Real email consent management.
- Unsubscribe handling.
- Sending and deliverability.

---

# ENG-07 — Export Approved Newsletter Draft

## Objective

Allow users to export an approved newsletter draft in a format that can be used by PartnerCRM.

## Related Use Case

UC-07 — Export Newsletter Draft

## User Story

As a PartnerCRM user, I want to export the approved newsletter draft, so that it can be used in the PartnerCRM communication workflow.

## Product Decisions

- Real email sending is out of scope for MVP.
- MVP supports export-ready output.
- PartnerCRM owns final distribution.
- Export is only allowed after approval.

## Functional Requirements

1. Check that the draft has been approved.
2. Generate an export-ready version of the newsletter.
3. Include newsletter title, body sections, call-to-action, and metadata.
4. Include selected audience segment metadata.
5. Provide export format suitable for PartnerCRM handoff.
6. Log the export event.
7. Block export if approval is missing.

## Acceptance Criteria

- Approved draft can be exported.
- Unapproved draft cannot be exported.
- Export includes final edited newsletter content.
- Export includes relevant metadata.
- Export event is logged.
- User receives clear success or failure feedback.

## Dependencies

- Approved draft from ENG-05.
- Audience segment selection from ENG-06.
- Event logging from ENG-08.
- Export format decision.

## Edge Cases

- Draft approval is revoked or invalid.
- Export fails.
- Selected audience segment is no longer available.
- User edits after approval and needs to re-approve.

## Out of Scope

- Real email sending.
- Scheduling.
- Deliverability monitoring.
- Open/click analytics.

---

# ENG-08 — Log Core Workflow Events

## Objective

Record key workflow events for traceability, debugging, and future analytics.

## Related Use Case

UC-08 — Log Workflow Events

## User Story

As a ComplianceBrief admin, I want key newsletter workflow events to be logged, so that usage and approvals can be traced later.

## Product Decisions

- MVP includes lightweight event logging.
- Full analytics dashboard is out of scope.
- Approval and export events must be traceable.
- Raw recipient-level personal data should not be logged.

## Functional Requirements

1. Log module open event.
2. Log content selection event.
3. Log draft generation event.
4. Log draft approval event.
5. Log export event.
6. Include user ID, account ID, timestamp, event type, and relevant object ID.
7. Exclude raw recipient-level personal data.
8. Provide internal access to basic event records.

## Acceptance Criteria

- Each core workflow event is logged.
- Logs include user, account, timestamp, and event type.
- Approval and export events are traceable.
- Logs do not include raw recipient-level personal data.
- Failed events are recorded where relevant.

## Dependencies

- User/account identity from ENG-01.
- Draft and export object IDs.
- Privacy and audit requirements.

## Edge Cases

- Event logging fails.
- User session expires during event.
- Duplicate events are triggered.
- Export succeeds but event logging fails.

## Out of Scope

- Full analytics dashboard.
- Admin reporting interface.
- Advanced compliance audit console.
- Long-term retention policy implementation.

---

# Handoff Notes for Engineering

## Product Decisions Already Made for MVP

1. User starts inside PartnerCRM.
2. SSO is assumed for MVP planning.
3. PartnerCRM is the identity provider.
4. Permissions are partner-account based.
5. ComplianceBrief owns content.
6. Only approved content can be used.
7. Newsletter generation is LLM-assisted but constrained to selected content.
8. Human approval is required before export.
9. PartnerCRM owns recipient data.
10. Real sending is out of scope.
11. MVP exports newsletter draft.
12. Core workflow events are logged.

## Open Product / Technical Questions

1. Which SSO protocol does PartnerCRM support?
2. Can PartnerCRM embed the ComplianceBrief module?
3. What CRM segment metadata is available?
4. What export format does PartnerCRM need?
5. Which generation service is allowed?
6. What source reference format is required?
7. What audit data must be retained?
8. What branding model should be used?

## PM Lesson

Engineering tickets should not be vague instructions like:

"Integrate newsletter product with CRM."

They should be specific, testable units of work.

A strong PM does not eliminate all uncertainty.

A strong PM separates:

- what is already decided;
- what engineering should build;
- what requires technical validation;
- what is out of scope;
- what stakeholders still need to decide.
