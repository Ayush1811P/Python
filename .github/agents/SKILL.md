# Agent-Customization Skill: Session-Friendly Workflow Extraction

## Purpose
Provide a reusable skill for extracting and codifying a user's multi-step workflow from a conversation, saving it as a `SKILL.md`, and using ephemeral session memory to avoid re-reading the entire repository repeatedly.

## Scope
- Intended as a workspace-scoped helper for developers and agents working in this repository.

## Behavior & Principles
- Extract the step-by-step process, decision points, and quality checks from the conversation.
- Persist only session-scoped notes about the workflow to `/memories/session/` so subsequent turns can re-use them without re-parsing the whole repo.
- Treat session memory as ephemeral: it is valid during the session and should be discarded (garbage-collected) when the session ends.
- When a new session starts, do not assume session memory exists; ask to re-summarize if necessary.

## Workflow
1. Read the recent conversation and identify whether a clear workflow exists. If none, ask the user: desired outcome? workspace-scoped or personal? quick checklist or detailed workflow?
2. Extract: steps (ordered list), decision points (branches or conditionals), and completion checks (what indicates a step is done).
3. Store the extracted summary in `/memories/session/<skill-name>.md` for fast reuse during the session.
4. Draft a `SKILL.md` artifact (this file) describing the workflow, ambiguity, and required clarifications.
5. Save the `SKILL.md` to `.github/agents/` in the workspace.
6. Ask user focused clarifying questions about any ambiguous step.
7. Iterate: update session memory and the `SKILL.md` until the user confirms.

## Decision Points (what to capture)
- Inputs that change the path (e.g., "if tests fail, run X", "if repo large, summarize only changed files").
- Quality gates (e.g., lint passing, tests green, manual approval required).

## Quality Criteria
- Each step is actionable and testable.
- Decision points include the condition and the alternate actions.
- Completion checks are explicit (e.g., "CI reports success", "file saved at path X").

## Session Memory Guidelines (per user's preference)
- Use `/memories/session/<skill-id>.md` to store extracted workflows and any short-term facts.
- Do NOT re-scan the entire repository each turn; first consult session memory.
- If a referenced file was edited outside the session, re-validate only the affected pieces rather than re-reading everything.
- When the session terminates, that session memory may be discarded (garbage-collected). The agent should ask to re-import or re-extract on the next session.

## Example Prompts
- "Extract a step-by-step workflow from our recent conversation and save it to session memory." 
- "Draft a `SKILL.md` for the deployment checklist we discussed and store session notes for reuse." 

## Ambiguities to Ask About (recommended starter questions)
- Should this skill be workspace-scoped (checked into the repo) or personal (kept locally)?
- How persistent should memory be beyond the session? (Currently: ephemeral.)
- Any special files/paths to ignore when resuming or revalidating?

## Iteration & Finalization
- After each draft, present a concise summary of changes and ask the user to confirm or correct specific steps.
- When finalized, recommend example prompts and related skills to create next (e.g., test-run skill, release-checklist skill).

## Implementation Notes for Agents
- Read `/memories/session/<skill-id>.md` first; if present and recent, reuse it.
- If memory is missing or stale, ask the user whether to re-extract from the conversation or to scan repository deltas.

---
Created by agent-customization skill template. Update or extend as needed.
