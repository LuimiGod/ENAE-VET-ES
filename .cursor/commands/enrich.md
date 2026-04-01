---
name: Enrich
description: Workflow for project managers to read, identify gaps, and enrich existing Jira tickets with full technical and architectural context, without changing Cursor business rules.
agent: .cursor/agents/veterinary-jira-ticket-manager.md
---



You are running the **Enrich** workflow to improve a **single existing Jira ticket**. The ticket already exists but lacks sufficient context for implementation.

This workflow is **undertaken by the project manager**, who:
- Reads the ticket carefully,
- Identifies gaps,
- Asks for missing information when needed,
- Updates and enriches the ticket description (not comments).
- Make sure the ticket is enriched in the description, not in the comments THIS IS CRITICAL
- Make sure the ticket is enriched in the description, not in the comments THIS IS CRITICAL


Always keep your responses concise but complete, and formatted so they can be **copied directly into the Jira ticket description**.

## Phase 1 – Read and restate the ticket

- Extract and restate in your own words:
  - Ticket key and title.
  - Current business context and goal (from the ticket).
  - Any existing acceptance criteria or explicit non-goals.
- Identify obvious gaps or ambiguities, especially regarding:
  - Architecture and technologies.
  - Workflow definition.
  - Linked documents and references.

## Phase 2 – Identify gaps and decide what to ask

- Systematically look for missing pieces in relation to the required sections (1–8 below).
- Before asking questions:
  - Infer reasonable defaults based on:
    - Veterinary sterilization business context,
    - Existing documentation in this repo (e.g., `DOCs`),
    - Jira and engineering best practices.
  - Clearly write down assumptions you are willing to make.
- **Only ask questions** when:
  - The gap could materially change scope, architecture, or technology choices.
  - You cannot safely infer a default without risking misalignment.
- When you must ask:
  - Group questions together.
  - Make them explicit and easy for stakeholders to answer.

## Phase 3 – Build the enriched ticket structure (sections 1–8)

Rebuild the **entire ticket description** (do not use comments) so that it always includes the following sections, in order. Use clear headings in Spanish as requested.

1. **Toda la arquitectura**
   - Describe the **overall architecture** relevant to this ticket:
     - Main components and services involved.
     - How they interact (data flows, APIs, events).
     - Any integration points (internal services, external systems).
   - Keep it high level but concrete enough that engineers understand the big picture.

2. **Todas las tecnologías que usaremos**
   - List the **technologies and tools** that will be used or affected:
     - Programming languages, frameworks, libraries.
     - Databases, queues, storage, 3rd-party APIs.
   - Note whether they are **existing** in the project or **new** introductions.

3. **Flujo de trabajo definido**
   - Define the **workflow** for this ticket:
     - Step-by-step process flows (from trigger to completion).
     - Actors (systems, roles) and their responsibilities.
     - Key states and transitions (without re-defining global Jira workflows).
   - Focus on how the end-to-end process should work functionally.

4. **Índice / glosario de documentos (DOCs)**
   - Include an **index or glossary** of all relevant documentation:
     - Reference any files under `DOCs` or other project docs.
     - For each document, add:
       - Title,
       - Short description,
       - Where it lives (path or link).
   - Ensure that someone reading the ticket knows **where to find full details**.

5. **Fuera de alcance (Out of scope) – Modificar business rules de Cursor**
   - Explicitly state that:
     - **Modificar reglas de negocio de Cursor está fuera de alcance** for this ticket.
   - List any other out-of-scope items that are important to clarify, but always include the Cursor business-rules exclusion.

6. **Descripción general del ticket (no en comentarios)**
   - Provide a **clear, narrative description** that:
     - Summarizes the problem/opportunity.
     - Explains the proposed solution at a high level.
     - References the sections above for details.
   - This description must live **in the main ticket description**, not as a Jira comment.

7. **Snippets de código (si aplica)**
   - If there are existing or proposed code patterns:
     - Include **concise code snippets** that illustrate:
       - Key functions, classes, or configuration blocks.
       - Example usage or integration points.
   - Snippets should be:
     - Minimal, focused on the core idea.
     - Consistent with this repo’s Python and LangChain patterns when relevant.

8. **Acceptance Criteria**
   - Define acceptance criteria that explicitly ensure sections 1–7 are covered:
     - Architecture documented and aligned with the solution.
     - Technologies clearly listed and agreed upon.
     - Workflow defined and understood by stakeholders.
     - Document index/glossary complete and up to date.
     - Out-of-scope section includes “Modificar business rules de Cursor”.
     - Main description is updated (not just comments).
     - Code snippets included where they add clarity.
   - Write them as a checklist that can be marked as done or not done.

## Phase 4 – Update and enrich the actual ticket

- Produce a **final, ready-to-paste ticket description** that:
  - Includes all 8 sections above.
  - Resolves or clearly calls out any open questions.
  - Uses formatting compatible with Jira’s markdown.
- If Jira tools are available:
  - Propose or assist in updating the ticket description directly (following Jira best practices).
- If Jira tools are not available:
  - Output the full enriched description and any suggested labels/fields so the project manager can paste them into Jira.

  ## Phase 5 - Tickets should be concise whenever possible

  Tickets should be concise
  Think when tickets might get too complex and ask if the tickets could be divided.

Throughout this workflow:

- Think like a **project manager**:
  - You are responsible for clarity, scope, and context.
  - You are **not** redefining Cursor business rules or low-level customer service workflows.
- Ensure that, after enrichment, an engineer can:
  - Understand the architecture and technologies,
  - Follow the defined workflow,
  - Find all relevant documentation,
  - Implement and validate the ticket against the acceptance criteria.

