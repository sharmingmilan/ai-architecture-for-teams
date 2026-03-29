# META/CLAUDE.md — How to Use This Template

> This folder contains Claude Code session context tooling.
> If you are adapting this project for your own team, this file explains how to use the META pattern to maintain continuity across Claude Code sessions.

---

## What This Is

The `META/` folder holds a context file that Claude reads at the start of every session to pick up where the last one left off. Think of it as a project memory file — it tracks what has been decided, what has been built, and what comes next.

This is especially useful for multi-session projects where context would otherwise be lost between conversations.

---

## How to Adapt This for Your Project

When you start using this template for your own team, create your own `META/CLAUDE.md` with these sections:

### 1. What This Project Is
One paragraph describing the project goal, who is building it, and what the end state looks like.

### 2. Current Status
A table of what has been decided, what files have been created, and what has not been done yet. Update this at the end of every session.

### 3. The Phases — Summary
A quick-reference table showing each phase name, timeline, and current status.

### 4. Key Decisions Made and Why
For every significant decision, record:
- **What** was decided
- **Why** (the reasoning, constraints, or trade-offs)
This becomes invaluable when a future session asks "why did we do it this way?"

### 5. Files to Create Next
An ordered list of the next files to build. Keeps you focused at the start of each session.

### 6. How to Pick Up in a New Session
Simple numbered steps: read this file → read the plan → ask "anything changed since last session?"

---

## End-of-Session Update Protocol

At the end of each working session, update this file by answering:

1. What did we actually complete? (Be specific)
2. What did we start but not finish?
3. Did anything change from the plan — a decision reversed, a scope change, a new constraint?
4. Did we hit any blockers or discover anything unexpected?
5. What is the single next action for the next session?
6. Any new files created or moved?

Then update only the sections that changed. Keep it current — a stale META file is worse than none.

---

## Why This Pattern Works

Claude Code sessions are stateless. Each new session starts with no memory of prior work unless context is explicitly provided. The META file solves this by acting as a structured handoff document between sessions.

The more specific and up-to-date the META file, the less time you spend re-explaining context at the start of each session — and the faster you can get back to building.

---

## Key Decisions Baked Into This Template

### Cognitive Task Analysis (CTA) for workflow documentation
Standard documentation captures the happy path. CTA forces documentation of exceptions, judgment calls, and implicit checks — the knowledge that lives in experts' heads. The CTA question set in `PROJECT-PLAN.md` Phase 3 is designed to surface this tacit knowledge.

### Tiered rollout (Claude.ai Projects first, Claude Code second)
Non-technical team members get Claude.ai Projects with pre-loaded context. Power users get Claude Code slash commands. Forcing a non-technical team onto the CLI creates friction that kills adoption.

### Human review checkpoint in every skill — non-negotiable
No skill auto-sends, auto-publishes, or auto-commits. Every skill produces a draft for human review. This is a permanent architectural constraint, not a training-wheels feature.

### Compliance-first MCP integration
No MCP server is installed without compliance approval. File requests early — approval lead time is the only external dependency you cannot control.

### Branch protection from day one
Branch protection on `main` before any file is committed. PRs required; no direct push. CLAUDE.md is load-bearing — a bad direct push silently corrupts Claude's context.

---

## Requirements Gathering Protocol

Before writing or rebuilding any project plan, run this requirements gathering sequence. Do not skip it — planning without it produces a plan that doesn't fit the real constraints.

### Round 1 — Situation and Constraints

1. What problem are you actually trying to solve? (Not "build an AI system" — what is the underlying pain?)
2. What does success look like in 90 days?
3. What has already been tried? What happened?
4. Who on the team is most affected by the current gaps?
5. What is your actual time budget per week — not the ideal, the real number?
6. What is the team's current relationship with AI tools?
7. Are there any hard deadlines, audits, or events that constrain the timeline?

### Round 2 — Scope and Priorities

8. Of your core workflows, which would have the highest impact if documented and automated first?
9. Which workflow is most at risk right now?
10. What would you cut if you had to deliver something useful in half the time?
11. What is the one thing that would make this project fail?
12. Who on the team do you trust to be an honest critic of the system once it's built?

### After gathering answers:
- Summarize back in 5–6 bullet points
- Surface any contradictions or gaps explicitly
- Propose a revised scope with trade-offs called out
- Wait for explicit approval before writing anything

---

## Verification Prompt

After `CLAUDE.md` is live on `main`, open a fresh Claude Code session and ask:

> "What team is this, what are our core workflows, and what are you never allowed to do automatically?"

If Claude answers correctly from `CLAUDE.md` alone — Phase 1 gate is passed. If it hedges or guesses, `CLAUDE.md` needs more specificity.
