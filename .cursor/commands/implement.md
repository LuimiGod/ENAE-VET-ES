---
name: Implement
description: End-to-end implementation of a Jira ticket, from understanding and planning through coding, PR creation, and status transitions.
agent: .cursor/agents/veterinary-langchain-backend.mdc
---

You are running the **Implement** workflow to complete a **single Jira ticket** whose details and acceptance criteria (CAC) are available in the current context.

Always follow these phases in order, and keep your responses concise but complete.

## Phase 1 – Read the ticket

- Extract and restate:
  - Ticket key and title.
  - Business context and goal.
  - All acceptance criteria (CAC) and any explicit non-goals.
- Identify:
  - Impacted areas of the codebase (files, modules, services).
  - Any obvious dependencies (APIs, data models, external services).

## Phase 2 – Create a plan

- Propose a short, numbered implementation plan that:
  - Maps **directly** to the acceptance criteria.
  - Lists expected code changes (new/modified files, data models, endpoints, LangChain components).
  - Includes testing strategy (unit/integration tests, manual checks).
- Keep the plan high level but concrete enough that each step can be “done or not done”.

## Phase 3 – Ask questions only when needed

- Before asking the user anything, first:
  - Try to infer reasonable defaults based on the ticket, existing code, and standard backend/LangChain patterns.
  - Clearly document any assumptions you decide to make instead of asking.
- **Only ask questions** when:
  - Acceptance criteria are incomplete or conflicting.
  - There are multiple materially different behaviors and you cannot safely choose one.
  - A decision affects external contracts (public APIs, events, schemas) or regulatory/safety concerns.
- When you must ask:
  - Group related questions together.
  - Pause implementation details that depend on the answers, but continue with independent work where possible.

## Phase 4 – Develop the code

- Follow the repo’s Python rules and best practices.
- Implement the plan step by step:
  - Prefer small, focused changes with clear responsibilities.
  - Update or create tests alongside code changes.
  - Keep veterinary LangChain safety patterns in mind when relevant (disclaimers, triage mindset, guarded tool use).
- As you describe changes:
  - Reference specific files and functions you are modifying.
  - Mention new public APIs or behavior changes explicitly.

## Phase 5 – Move ticket from “To Do” to “In Progress”

- Once you start actual implementation work:
  - If Jira tooling is available in this environment, propose or execute the appropriate transition from **To Do** to **In Progress** for this ticket.
  - Otherwise, explicitly instruct the user which Jira transition to apply.

## Phase 6 – Create a PR with a good description

- Prepare a pull request against the appropriate base branch (usually `main` unless specified otherwise).
- The PR title should follow the ticket, e.g. `[<TICKET_KEY>] <short summary>`.
- The PR description should include:
  - Summary of the change in 2–5 bullet points.
  - How it satisfies each acceptance criterion (explicit checklist).
  - Any important design decisions or trade-offs.
  - Testing: commands run, test cases covered, and results.
  - Known limitations or follow-up work, if any.
- If you cannot directly create the PR, output:
  - The git commands to run.
  - The suggested PR title and body.

## Phase 7 – Move ticket from “In Progress” to “In Review”

- After the PR is ready:
  - If Jira tooling is available, propose or execute the transition from **In Progress** to **In Review** (or equivalent, e.g. “Code Review”).
  - Otherwise, clearly instruct the user to move the ticket to the review state.
- Summarize:
  - The PR link or identifier.
  - What reviewers should focus on (e.g. tricky logic, integration points, performance or safety considerations).

Throughout all phases, keep a strong engineering mindset:

- Be explicit about assumptions.
- Prefer safety and clarity over cleverness.
- Maintain alignment with the veterinary LangChain backend patterns when the ticket touches chatbot or triage behavior.

