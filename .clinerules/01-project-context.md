# Project Context: Festival Schedule Generator

## Purpose

This project schedules festival shows across stages while minimizing the number of stages required.

The implementation should be correct, understandable, maintainable, efficient, and appropriately scoped to the DEMCON challenge.

## Assignment Requirements

- The challenge permits Python, C++, or MATLAB. This repository uses Python.
- Each show has a name, a start time, and an end time.
- Times are expressed as integer hours from the start of the festival.
- The program must produce a clear schedule showing every show's assigned stage, start time, and end time.
- The input format and output format are implementation choices, provided they are clearly documented and satisfy the challenge.
- The program must handle arbitrary valid schedules, not just the supplied example.
- Provide a README explaining how to run the program and supply input.
- The solution should demonstrate efficiency, inventiveness, and good coding practices.

The primary optimization objective is to minimize the number of stages while scheduling every show without overlap.

## Technology

- Language: Python.
- Development environment currently uses Python 3.14.
- Follow the existing repository structure, conventions, and tooling unless a requested change justifies modifying them.
- Do not introduce dependencies without a clear need and the necessary authorization.

## Repository Discovery

The current repository is the source of truth for its file structure and implementation.

- Inspect relevant files and their relationships before making changes.
- Discover the actual entry point, models, services, tests, and configuration from the repository rather than assuming their locations.
- Do not enumerate the entire repository when targeted inspection is sufficient.
- Update this context file when stable project requirements, technology choices, or architectural decisions change—not for routine code changes or file movements.

## Scheduling Requirements

- Every show must be assigned to exactly one stage.
- A show occupies every integer hour from its start time through its end time, inclusive.
- For example, a show running from hour 36 through hour 39 occupies hours 36, 37, 38, and 39.
- Two shows overlap if they occupy at least one common hour. Therefore, a show ending at hour 36 conflicts with another show starting at hour 36.
- Shows assigned to the same stage must not overlap.
- A stage can be reused only when its previous show ends strictly before the next show starts.
- Every input show must appear exactly once in the output, with its identity and timing preserved.
- The schedule must be valid regardless of the order in which shows are supplied.
- The number of stages used must be minimal for the given schedule.
- Do not invent additional scheduling constraints that are not required by the challenge or specified by the user.

## Algorithmic Correctness

A suitable baseline for this interval-scheduling problem is to process shows in ascending start-time order and assign each show to a compatible stage whose previous show ends earliest.

A min-heap keyed by stage availability can efficiently identify the stage that becomes available first.

Because the intervals are inclusive, a stage whose previous show ends at time `t` cannot be reused by a show starting at time `t`. Reuse is permitted only when `previous_end < next_start`.

If no existing stage is compatible, create another stage.

This approach should achieve the minimum number of stages for the stated problem when implemented correctly. However, the algorithm's suitability does not prove that the implementation is correct. Verify the implementation, explain the relevant correctness argument, and test important edge cases before claiming optimality.

## Scope and Design Priorities

- Prefer a straightforward, correct solution over unnecessary abstraction.
- Separate input parsing, data models, scheduling logic, and presentation where doing so improves clarity and maintainability.
- Preserve existing public interfaces unless changing them is necessary for the requested task.
- Avoid unrelated refactoring, speculative features, and premature generalization.
- If requirements conflict or an important constraint is unclear, ask for clarification rather than inventing behavior.
