import re
from datetime import datetime
from pathlib import Path

import streamlit as st


OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


PRESETS = {
    "Generic Integration Example": {
        "project_name": "Example Product Integration Case Study",
        "business_request": "Integrate our product with a partner platform so partner users can complete a key workflow using our capabilities.",
        "business_goal": "Validate whether the partnership workflow creates value for partner users and can support future commercial expansion.",
        "primary_user": "Partner platform user",
        "user_goal": "complete the target workflow without leaving the partner platform",
        "starting_system": "Partner platform",
        "actors": "Partner platform user\nClient admin\nPartner admin\nEnd customer\nInternal product and engineering team",
        "systems": "Partner platform\nClient product platform\nAuthentication or SSO layer\nWorkflow generation service\nAnalytics or audit layer",
        "journey_steps": "User starts inside the partner platform\nUser opens the client product module\nSystem checks access and permissions\nUser selects or inputs required information\nSystem generates or prepares the output\nUser reviews the output\nUser approves or confirms the result\nSystem exports or completes the workflow\nSystem logs key events",
        "product_decisions": "User starts inside the partner platform\nAuthentication is assumed for MVP planning\nThe partner platform owns user identity\nThe client product owns source content or capability\nHuman review is required before final output\nMVP exports or prepares output instead of performing irreversible production actions\nCore workflow events are logged",
        "in_scope": "User entry point from partner platform\nAccess and permission check\nCore workflow steps\nReview and confirmation step\nExport-ready output\nBasic event logging",
        "out_of_scope": "Production-grade SSO implementation\nReal external API integration\nAdvanced analytics\nBilling\nMulti-partner configuration\nFull compliance dashboard",
        "risks": "Partner workflow assumptions may be wrong\nRequired APIs may not exist\nUsers may expect production behavior in MVP\nData ownership may be unclear\nScope may expand before validation",
        "success_metrics": "User can complete the end-to-end workflow in a demo\nStakeholders understand the product flow\nEngineering can identify buildable tickets\nOpen questions are visible and assigned\nMVP scope is clear",
    },
    "ComplianceBrief x PartnerCRM": {
        "project_name": "ComplianceBrief x PartnerCRM Newsletter Partnership Integration",
        "business_request": "Integrate ComplianceBrief's newsletter product with PartnerCRM so PartnerCRM users can create newsletters using ComplianceBrief content.",
        "business_goal": "Validate whether a ComplianceBrief and PartnerCRM partnership can create a useful embedded newsletter workflow for partner users.",
        "primary_user": "PartnerCRM customer-success or sales user",
        "user_goal": "create a customer-facing compliance newsletter using approved ComplianceBrief content without leaving PartnerCRM",
        "starting_system": "PartnerCRM",
        "actors": "PartnerCRM user\nComplianceBrief admin\nPartnerCRM admin\nEnd recipient\nInternal product and engineering team",
        "systems": "PartnerCRM\nComplianceBrief content platform\nAuthentication or SSO layer\nNewsletter generation service\nDistribution or export service\nAnalytics or audit layer",
        "journey_steps": "PartnerCRM user starts inside PartnerCRM\nUser opens the ComplianceBrief newsletter module\nSystem validates SSO and account-level access\nSystem loads approved ComplianceBrief content\nUser selects up to three approved content blocks\nSystem generates a newsletter draft from selected content\nDraft displays source references\nUser reviews and edits the draft\nUser selects a CRM audience segment\nUser approves the final draft\nSystem exports the approved newsletter draft\nSystem logs key workflow events",
        "product_decisions": "User starts inside PartnerCRM\nSSO is assumed for MVP planning\nPartnerCRM is the identity provider\nPermissions are partner-account based\nComplianceBrief is the source of truth for research content\nOnly approved content can be used for generation\nNewsletter generation is LLM-assisted but constrained to selected approved content\nHuman approval is required before export\nPartnerCRM owns recipient data\nComplianceBrief does not store raw recipient-level personal data in MVP\nReal email sending is out of scope for MVP\nMVP produces an export-ready newsletter draft\nCore workflow events are logged",
        "in_scope": "PartnerCRM entry point\nSSO-based access assumption\nAccount-level content permission check\nApproved ComplianceBrief content library\nContent selection flow\nNewsletter draft generation from selected content\nSource references for generated draft\nReview and edit workflow\nExplicit approval before export\nCRM audience segment selection using metadata only\nExport-ready newsletter output\nBasic workflow event logging",
        "out_of_scope": "Real production SSO implementation\nReal CRM API integration\nReal LLM API\nReal email sending\nDeliverability management\nUnsubscribe handling\nAdvanced analytics dashboard\nBilling\nPartner marketplace listing\nMulti-partner configuration\nLegal approval queue\nFull audit console",
        "risks": "PartnerCRM may not support the required SSO or embedding model\nPartnerCRM may not expose audience segment metadata cleanly\nStakeholders may expect real email sending in MVP\nGenerated content may require stricter legal review than assumed\nRecipient data ownership must remain clear\nScope may expand into analytics, sending, billing, or marketplace packaging before validation",
        "success_metrics": "User can complete the end-to-end workflow in a demo environment\nUser understands which ComplianceBrief content is available and why\nUser can generate a draft from selected approved content\nUser can review and approve before export\nStakeholders can identify missing requirements after seeing the workflow\nEngineering can map requirements to buildable tickets\nMVP scope and out-of-scope boundaries are clear",
    },
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "pm-case-study"


def split_lines(value: str) -> list[str]:
    lines = []
    for line in value.splitlines():
        clean = line.strip()
        if clean:
            lines.append(clean)
    return lines


def bullet_list(items: list[str], fallback: str = "To be defined.") -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join([f"- {item}" for item in items])


def numbered_list(items: list[str], fallback: str = "To be defined.") -> str:
    if not items:
        return f"1. {fallback}"
    return "\n".join([f"{index + 1}. {item}" for index, item in enumerate(items)])


def generate_markdown(data: dict) -> str:
    project_name = data["project_name"]
    business_request = data["business_request"]
    business_goal = data["business_goal"]
    primary_user = data["primary_user"]
    user_goal = data["user_goal"]
    starting_system = data["starting_system"]
    systems = split_lines(data["systems"])
    actors = split_lines(data["actors"])
    journey_steps = split_lines(data["journey_steps"])
    product_decisions = split_lines(data["product_decisions"])
    in_scope = split_lines(data["in_scope"])
    out_of_scope = split_lines(data["out_of_scope"])
    risks = split_lines(data["risks"])
    success_metrics = split_lines(data["success_metrics"])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    return f"""# {project_name}

Generated by PM Case Study Generator v1.1.

Generation timestamp: {now}

---

# 1. Product Brief

## Business Request

{business_request}

## Business Goal

{business_goal}

## Primary User

{primary_user}

## User Goal

{user_goal}

## PM Interpretation

This request should not be passed directly to engineering as a vague implementation task.

The Product Manager should first clarify the business goal, users, systems, journey, product decisions, MVP scope, risks, and validation criteria.

---

# 2. Actors and Systems

## Actors

{bullet_list(actors)}

## Systems Involved

{bullet_list(systems)}

## Starting System

The user starts inside:

- {starting_system}

## Ownership Questions

Before engineering starts, the PM should clarify:

- Who owns authentication?
- Who owns user identity?
- Who owns source data or content?
- Who owns customer/contact data?
- Who owns permissions?
- Who owns approval?
- Who owns final output?
- Who owns audit logs?

---

# 3. User Journey

## Primary Journey

{numbered_list(journey_steps)}

## Journey Summary

The user starts inside {starting_system}, performs the core workflow, and reaches the final outcome defined by the business request.

The PM should validate whether this journey matches the real user context before implementation.

---

# 4. Product Decisions

## MVP Product Decisions

{bullet_list(product_decisions)}

## Decision Status

Each decision should be classified as one of:

- Decided for MVP
- Needs validation
- Out of scope for MVP

## PM Rule

Do not hide unresolved product decisions inside engineering tickets.

If the product direction is not decided, document the open question and assign an owner.

---

# 5. MVP Scope

## In Scope

{bullet_list(in_scope)}

## Out of Scope

{bullet_list(out_of_scope)}

---

# 6. Use Cases

## UC-01 — Access the workflow

As a {primary_user}, I want to access the workflow from {starting_system}, so that I can start the process without unnecessary friction.

## UC-02 — Complete the core task

As a {primary_user}, I want to complete the main workflow, so that I can achieve the user goal: {user_goal}

## UC-03 — Review and confirm output

As a {primary_user}, I want to review the final output before completion, so that I can confirm it is accurate and appropriate.

## UC-04 — Track key workflow events

As an internal team member, I want key workflow events to be logged, so that product, engineering, and stakeholders can understand what happened.

---

# 7. Product Requirements Document

## Problem Statement

{primary_user} needs a way to {user_goal} from inside {starting_system}.

The current request is ambiguous and requires clarification around users, systems, ownership, permissions, scope, and validation.

## Functional Requirements

### FR-01 — User Entry Point

The user must be able to start the workflow from {starting_system}.

### FR-02 — Actor and Permission Clarity

The system must respect the actors, systems, and ownership boundaries defined by the PM.

### FR-03 — Core Workflow

The system must support the primary user journey.

### FR-04 — Review Step

The user must be able to review the final output or result before completion when the workflow affects external users, customers, data, or business-critical actions.

### FR-05 — Event Logging

The system should log key workflow events needed for traceability and future analysis.

## Non-Functional Requirements

- The workflow should be understandable to a non-technical user.
- Error states should be clear.
- Out-of-scope items should not be silently implemented.
- Product decisions should be traceable to requirements and tickets.

---

# 8. Engineering Tickets

## ENG-01 — Build User Entry Point

### Objective

Allow the primary user to start the workflow from {starting_system}.

### User Story

As a {primary_user}, I want to open the workflow from {starting_system}, so that I can begin the task in my normal context.

### Acceptance Criteria

- Given an authorized user, when they open the workflow, then they can access the first step.
- Given an unauthorized user, when they attempt access, then the system shows a clear access message.
- Given the workflow is unavailable, when the user tries to open it, then the system shows a clear error state.

## ENG-02 — Build Core Workflow

### Objective

Support the main user journey.

### User Story

As a {primary_user}, I want to complete the core workflow, so that I can {user_goal}

### Acceptance Criteria

- Given valid inputs, when the user proceeds through the workflow, then each step is displayed in the expected order.
- Given missing required information, when the user tries to continue, then the system explains what is missing.
- Given the user reaches the final step, when they review the output, then the workflow is ready for confirmation or export.

## ENG-03 — Add Review and Confirmation Step

### Objective

Allow the user to review the final output before completion.

### Acceptance Criteria

- The user can review the final result before completion.
- The user can go back and correct inputs where applicable.
- The system prevents completion when required approval is missing.

## ENG-04 — Log Key Workflow Events

### Objective

Record key workflow events for traceability.

### Acceptance Criteria

- Workflow start is logged.
- Core step completion is logged.
- Final confirmation or export is logged.
- Logs do not include unnecessary sensitive data.

---

# 9. Risks

{bullet_list(risks)}

---

# 10. Success Metrics

{bullet_list(success_metrics)}

---

# 11. Executive Summary

This case study turns an ambiguous product request into structured product work.

It demonstrates:

- business goal clarification;
- actor and system mapping;
- user journey definition;
- product decision logging;
- MVP scoping;
- use case creation;
- PRD creation;
- engineering handoff.

The main PM lesson is simple:

A Product Manager should not pass ambiguity directly to engineering.

A Product Manager should structure uncertainty into decisions, requirements, tickets, risks, and validation criteria.
"""


st.set_page_config(
    page_title="PM Case Study Generator",
    page_icon="🧭",
    layout="wide",
)

st.title("PM Case Study Generator")
st.caption("Phase 1.1: template-based PM artifact generator with reusable presets. No LLM required.")

st.markdown(
    """
This tool converts an ambiguous product request into structured PM artifacts.

It follows the sequence:

business request → actors → systems → journey → decisions → scope → PRD → engineering tickets
"""
)

preset_name = st.selectbox(
    "Load a preset",
    options=list(PRESETS.keys()),
    index=1,
)

defaults = PRESETS[preset_name]

st.info(f"Loaded preset: {preset_name}")

with st.form("pm_generator_form"):
    st.subheader("1. Product Context")

    project_name = st.text_input("Project name", value=defaults["project_name"])
    business_request = st.text_area("Ambiguous business request", value=defaults["business_request"], height=100)
    business_goal = st.text_area("Business goal", value=defaults["business_goal"], height=80)

    st.subheader("2. Users and Systems")

    primary_user = st.text_input("Primary user", value=defaults["primary_user"])
    user_goal = st.text_area("User goal", value=defaults["user_goal"], height=80)
    starting_system = st.text_input("Where does the user start?", value=defaults["starting_system"])
    actors = st.text_area("Actors involved, one per line", value=defaults["actors"], height=130)
    systems = st.text_area("Systems involved, one per line", value=defaults["systems"], height=130)

    st.subheader("3. Journey and Decisions")

    journey_steps = st.text_area("User journey steps, one per line", value=defaults["journey_steps"], height=210)
    product_decisions = st.text_area("Product decisions, one per line", value=defaults["product_decisions"], height=220)

    st.subheader("4. Scope, Risks, and Metrics")

    in_scope = st.text_area("MVP in scope, one per line", value=defaults["in_scope"], height=180)
    out_of_scope = st.text_area("MVP out of scope, one per line", value=defaults["out_of_scope"], height=180)
    risks = st.text_area("Risks, one per line", value=defaults["risks"], height=160)
    success_metrics = st.text_area("Success metrics, one per line", value=defaults["success_metrics"], height=160)

    submitted = st.form_submit_button("Generate PM artifacts")

if submitted:
    data = {
        "project_name": project_name,
        "business_request": business_request,
        "business_goal": business_goal,
        "primary_user": primary_user,
        "user_goal": user_goal,
        "starting_system": starting_system,
        "actors": actors,
        "systems": systems,
        "journey_steps": journey_steps,
        "product_decisions": product_decisions,
        "in_scope": in_scope,
        "out_of_scope": out_of_scope,
        "risks": risks,
        "success_metrics": success_metrics,
    }

    markdown = generate_markdown(data)
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{slugify(project_name)}.md"
    output_path = OUTPUT_DIR / filename
    output_path.write_text(markdown, encoding="utf-8")

    st.success(f"Generated: app/outputs/{filename}")

    st.download_button(
        label="Download generated Markdown",
        data=markdown,
        file_name=filename,
        mime="text/markdown",
    )

    st.subheader("Generated Preview")
    st.markdown(markdown)
