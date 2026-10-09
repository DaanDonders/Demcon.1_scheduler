# Engineering Standards

## 1. Understand Before Changing

- Inspect the relevant implementation and its callers before making changes.
- Follow existing project conventions when they are reasonable and consistent.
- Understand the responsibility of each affected component before moving logic between components.
- Do not assume that a file, class, function, or dependency is unnecessary without investigating its role.

## 2. Correctness First

- Satisfy the stated requirements before optimizing or refactoring.
- Identify relevant invariants, preconditions, postconditions, and edge cases.
- Consider normal inputs, boundary conditions, invalid inputs, and empty inputs where applicable.
- Do not claim an algorithm is optimal, code is correct, or behavior is guaranteed without sufficient reasoning or evidence.
- Prefer a simple solution whose correctness can be explained and verified.

## 3. Maintainable Design

- Give each module, class, and function a clear responsibility.
- Keep related behavior together and minimize unnecessary coupling.
- Avoid duplicated logic when a small, well-defined abstraction would improve maintainability.
- Avoid abstractions that add complexity without a clear benefit.
- Prefer explicit, readable code over clever or unnecessarily compact implementations.
- Use descriptive names that communicate intent.

## 4. Change Discipline

- Make the smallest coherent change that satisfies the request.
- Preserve existing behavior unless the task requires changing it.
- Avoid unrelated cleanup, broad rewrites, and speculative future-proofing.
- Do not change public interfaces or data contracts unnecessarily.
- When a broader change appears necessary, explain why before expanding the scope.

## 5. Dependencies and Configuration

- Prefer existing project capabilities over introducing new dependencies.
- Do not install packages or alter environment, configuration, or infrastructure merely for convenience.
- If a new dependency or configuration change is necessary, explain the reason and obtain authorization when it exceeds the scope of the task.
- Never hardcode credentials, secrets, or machine-specific paths.

## 6. Evidence-Based Decisions

- Base implementation decisions on the requirements, existing code, relevant documentation, and verifiable behavior.
- Separate confirmed facts from assumptions.
- When multiple approaches are viable, choose the simplest suitable option and explain meaningful trade-offs.
- If a key requirement or technical decision cannot be established, ask a focused question rather than inventing certainty.
