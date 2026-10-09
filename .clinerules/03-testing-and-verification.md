# Testing and Verification

## 1. Authorization

- Follow the permissions defined in `00-agent-boundaries.md`.
- Do not run tests, builds, linters, or application code unless the current task authorizes execution.
- When implementation is authorized but testing is not, complete only the authorized changes and state that verification was not run.
- Do not modify code, tests, dependencies, or configuration merely to make a failed check pass unless those modifications are within the authorized task.

## 2. Test Strategy

When testing is authorized:

- Inspect the existing test setup and follow the project's established test framework and conventions.
- Identify which tests are relevant to the change before running them.
- Prefer targeted tests first, followed by broader tests when appropriate.
- Do not create a new testing framework or introduce dependencies simply because the existing test setup is unfamiliar.
- Do not assume tests exist, are complete, or are meaningful without inspecting them.

## 3. Test Meaningful Behavior

Tests should verify observable requirements and behavior rather than merely repeat implementation details.

Consider, where applicable:

- Typical valid inputs.
- Empty and boundary inputs.
- Invalid inputs and expected error handling.
- Edge cases specific to the problem domain.
- Regression cases for previously discovered defects.
- Interactions between affected components.

For algorithms, verify the relevant invariants and correctness properties. A passing example alone does not establish correctness or optimality.

## 4. Diagnose Failures

When a check fails:

1. Read the actual error and identify what failed.
2. Determine whether the cause is application code, a test, a missing dependency, configuration, the environment, or the command itself.
3. Choose the next action based on that evidence.
4. Do not blindly repeat the command, switch frameworks, install packages, or rewrite code without a justified reason.
5. If resolving the failure would exceed the authorized scope, stop and report what is needed.

A failing test is evidence to investigate, not automatic permission to change unrelated files.

## 5. Report Verification Accurately

Distinguish between:

- Tests that passed.
- Tests that failed.
- Tests that were not run.
- Checks that could not run because of an environmental or tooling limitation.
- Behavior that has been reasoned about but not verified.

Never claim the project is fully tested or correct based only on a successful command or a small number of examples.

Summarize the checks performed and any significant remaining uncertainty.
