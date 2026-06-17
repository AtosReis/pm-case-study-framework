# USER JOURNEY MAP

## Purpose

This document maps the end-to-end user journey for the fictional partnership integration.

The goal is to show how a Product Manager moves from an ambiguous request to a clear product flow before writing engineering tickets.

## Ambiguous Request

"Integrate ComplianceBrief's newsletter product with PartnerCRM so PartnerCRM users can create newsletters using ComplianceBrief content."

## PM Translation

The request is not simply:

"Build a newsletter generator."

The real product journey is:

A PartnerCRM user should be able to access approved ComplianceBrief content, create a newsletter draft, review it, select CRM recipients, and prepare the newsletter for distribution without leaving the PartnerCRM workflow.

## Primary User Journey

### Step 1 — User starts inside PartnerCRM

The user is already logged into PartnerCRM.

User intent:

"I want to send a useful compliance update to a segment of my customers."

PM questions:

- Is PartnerCRM the starting point?
- Does the user already have the right role?
- Where does the ComplianceBrief feature appear in the UI?
- Is this a sidebar, embedded module, marketplace app, or separate page?

Product decision needed:

For MVP, the user starts inside PartnerCRM and accesses ComplianceBrief through an embedded partner module.

## Step 2 — User accesses ComplianceBrief through SSO

The user clicks the ComplianceBrief newsletter feature.

Expected behavior:

The user should not need to create a separate ComplianceBrief login.

PM questions:

- Is SSO required for MVP?
- Which system owns identity?
- How are PartnerCRM users mapped to ComplianceBrief permissions?
- What happens if the user is not authorized?

Product decision needed:

For MVP, assume SSO is required and PartnerCRM is the identity provider.

## Step 3 — System checks permissions

Before showing content, the system checks whether the user has access.

Expected behavior:

The user only sees content approved for their organization, role, or partner account.

PM questions:

- Are permissions account-level, user-level, or role-level?
- Can content be partner-specific?
- Can access be revoked?
- Should unauthorized users see an error, empty state, or upgrade/contact-admin message?

Product decision needed:

For MVP, access is partner-account based. If the account is enabled, authorized users can view approved content.

## Step 4 — User browses approved ComplianceBrief content

The user sees a content library inside the PartnerCRM workflow.

Content may include:

- weekly compliance research;
- topic tags;
- short summaries;
- publication date;
- recommended audience;
- region or industry tags.

PM questions:

- What metadata is required?
- Are images included?
- Can users search/filter content?
- Can users select multiple content blocks?
- Is expired content hidden?

Product decision needed:

For MVP, users can browse and select approved content blocks using topic and date filters.

## Step 5 — User selects content for the newsletter

The user chooses one or more content blocks to include.

Expected behavior:

Selected content becomes the input for the newsletter draft.

PM questions:

- Is there a maximum number of content blocks?
- Can content be reordered?
- Can users preview selected content?
- Should the system warn about conflicting or outdated content?

Product decision needed:

For MVP, users can select up to three content blocks for one newsletter draft.

## Step 6 — System generates a newsletter draft

The system creates a draft newsletter from the selected content.

Expected behavior:

The draft should use only approved selected content.

PM questions:

- Is generation template-based, LLM-assisted, or both?
- Which generation service owns the output?
- Can the model add new claims?
- Does the output need citations or source references?
- Should the user see which content blocks were used?

Product decision needed:

For MVP, generation is LLM-assisted but restricted to selected approved content. The output must show source content references.

## Step 7 — User reviews and edits the draft

The user reviews the generated newsletter before sending or exporting.

Expected behavior:

The user can edit the title, introduction, sections, and call-to-action.

PM questions:

- Can the user freely edit all generated text?
- Are some sections locked?
- Is there an approval workflow?
- Does editing remove source traceability?
- Are changes saved as drafts?

Product decision needed:

For MVP, users can edit the draft, but must review a source-content summary before final approval.

## Step 8 — User selects CRM recipients

The user selects recipients from PartnerCRM contacts.

Expected behavior:

The user can choose a CRM segment or manually select contacts.

PM questions:

- Does PartnerCRM own contact segmentation?
- Can ComplianceBrief see recipient data?
- Are email consent and unsubscribe handled by PartnerCRM?
- Can the newsletter be sent to prospects, customers, or both?

Product decision needed:

For MVP, PartnerCRM owns recipient selection and consent rules. ComplianceBrief does not store recipient-level personal data.

## Step 9 — User approves newsletter for distribution

Before sending or exporting, the user confirms the newsletter.

Expected behavior:

The system shows a final preview, selected content, selected audience, and sending/export option.

PM questions:

- Who can approve?
- Is approval mandatory?
- Is there an audit log?
- Can a newsletter be scheduled?
- Can the user go back and edit?

Product decision needed:

For MVP, explicit user approval is required before export or send preparation.

## Step 10 — Newsletter is prepared for distribution

The MVP can either send, schedule, or export the newsletter.

PM questions:

- Does MVP include real sending?
- Is the email sent by PartnerCRM?
- Is the output exported as HTML?
- Are open/click metrics required?
- Who owns failure handling?

Product decision needed:

For MVP, the system prepares an export-ready newsletter draft. Real sending is out of scope.

## Step 11 — System logs usage and audit data

The system records key events.

Events may include:

- content viewed;
- content selected;
- draft generated;
- draft edited;
- approval completed;
- export created.

PM questions:

- What events are required for audit?
- Who can view logs?
- How long are logs stored?
- Are generated drafts stored?
- Are user edits stored?

Product decision needed:

For MVP, log generation, approval, and export events. Detailed analytics are V2.

## MVP Journey Summary

1. PartnerCRM user opens the ComplianceBrief module.
2. SSO authenticates the user.
3. Permissions are checked.
4. User browses approved content.
5. User selects up to three content blocks.
6. System generates a newsletter draft.
7. User reviews and edits the draft.
8. User selects CRM recipients or segment.
9. User approves the final draft.
10. System exports the newsletter draft.
11. System logs key events.

## Out of Scope for MVP

- Real email sending.
- Real CRM API integration.
- Real SSO implementation.
- Real LLM API.
- Advanced analytics.
- Multi-step legal approval.
- Billing.
- Partner marketplace packaging.
- Multiple partner support.

## PM Lesson

A user journey prevents premature solutioning.

Without the journey, the PM may jump directly to:

- automation;
- AI;
- LLM;
- hallucination prevention;
- code.

Those topics matter, but they come after the PM has clarified:

- who the user is;
- where the user starts;
- what the user needs to accomplish;
- which systems are involved;
- what decisions must be made;
- what is MVP and what is not.
