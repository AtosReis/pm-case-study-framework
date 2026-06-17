# ACCEPTANCE CRITERIA TEMPLATE

## Purpose

Acceptance criteria define what must be true for a ticket to be considered complete.

They protect engineering, product, QA, and stakeholders from vague interpretation.

## Good Acceptance Criteria

Good acceptance criteria are:

- observable;
- testable;
- specific;
- tied to user behavior or system behavior;
- not vague opinions.

## Bad Examples

- The integration should work well.
- The page should be user-friendly.
- The AI should generate good content.
- The system should be fast.

## Better Examples

- Given an authorized user, when they open the module, then they can access the newsletter workflow without a separate login.
- Given an unauthorized account, when the module is opened, then the system displays an access-denied message.
- Given zero selected content blocks, when the user clicks generate, then the system prevents generation and shows a clear message.

## Template

### Acceptance Criteria

1. Given [initial condition], when [user/system action], then [expected outcome].
2. Given [initial condition], when [user/system action], then [expected outcome].
3. Given [initial condition], when [user/system action], then [expected outcome].

### Validation Questions

- Can QA test this?
- Can engineering know when it is done?
- Can product confirm the behavior?
- Is the expected result unambiguous?
- Are failure states covered?
- Are permission cases covered?
- Are empty states covered?
