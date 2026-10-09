# Development Workflow

## 1. Understand the Request

- Identify the requested outcome, constraints, and acceptance criteria.
- Determine the applicable task mode and permissions using `00-agent-boundaries.md`.
- Inspect the relevant existing code and project documentation before planning changes.
- Do not start implementing until the requirements are sufficiently clear.

## 2. Plan Proportionately

- For a small, straightforward change, use a brief internal plan and proceed.
- For a change spanning multiple components, affecting public interfaces, or involving significant algorithmic or architectural decisions, establish an explicit implementation plan before editing.
- Identify the likely files affected, important dependencies, risks, and verification approach.
- Prefer the smallest design that satisfies the requirements.
- Ask the user about decisions that materially affect scope or correctness and cannot be resolved from the existing requirements.

## 3. Implement

When implementation is authorized:

- Follow the applicable engineering standards and project requirements.
- Make changes in small, coherent steps.
- Reuse existing components and conventions where appropriate.
- Preserve unrelated behavior and existing user work.
- Do not add speculative features, dependencies, or abstractions.
- Do not broaden the task just because an improvement is discovered.

## 4. Verify

- Follow `03-testing-and-verification.md` and the permissions granted for the task.
- Run relevant checks only when authorized.
- Compare the result with the original requirements and acceptance criteria.
- Investigate failures using the available evidence.
- Do not hide failures, weaken tests, or claim success without verification.

## 5. Review the Result

When reviewing is within the authorized scope:

- Inspect the changes for correctness, unintended side effects, unnecessary complexity, and consistency with the requirements.
- Check for accidental edits to unrelated files.
- Confirm that relevant interfaces and expected behavior remain consistent.
- Correct defects only within the authorized scope.
- If a material issue requires broader changes or additional permission, stop and report it.

## 6. Finish

Provide a concise report containing:

- What was implemented.
- Which important files were changed.
- Which checks were actually run and their outcomes.
- Any known limitations, unresolved issues, or unverified behavior.

Stop when the requested outcome is achieved. Do not continue into unrelated improvements or additional tasks.
