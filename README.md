# AI Architecture for Teams

A complete framework for deploying Claude Code as a team productivity and documentation system. Fork this repo, open it in Claude Code, and run `/onboarding` — by the end of that session you'll have a configured `CLAUDE.md` and a customized implementation plan ready to execute.

---

## What This Builds

By the end of the 5-phase project, your team will have:

1. A GitHub repo (`team-ai`) with structured workflow documentation, AI skills, and slash commands
2. Claude.ai Projects configured for non-technical team members
3. Claude Code slash commands for power users
4. MCP integrations connecting Claude to your team's live data sources

---

## Start Here

**Step 1 — Fork this repo**

**Step 2 — Clone it locally and open in Claude Code:**
```bash
git clone https://github.com/YOUR_USERNAME/ai-architecture-for-teams
claude ai-architecture-for-teams
```

**Step 3 — Run the onboarding:**
```
/onboarding
```

This starts a structured Q&A session. Your answers are used to auto-fill `CLAUDE.md` with your real team context. By the end you'll have a completed context file and a clear next action.

**Step 4 — Follow the plan**

Open `PROJECT-PLAN.md`. It's your implementation roadmap, phase by phase.

---

## The 5 Phases

| Phase | Name | What Gets Built |
|-------|------|-----------------|
| 1 | Repo Setup & CLAUDE.md | Foundational repo + context file that orients Claude in every session |
| 2 | MCP Integrations | Compliance-approved connections to live data sources |
| 3 | Workflow Documentation | Core workflows documented using Cognitive Task Analysis (CTA) |
| 4 | Skills & Slash Commands | Highest-ROI automations built as Claude Code skills |
| 5 | Team Rollout | Tiered rollout — Claude.ai Projects for everyone, Claude Code for power users |

Each phase has a gate — a specific outcome that must be achieved before the next phase begins.

---

## Files in This Repo

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Team context file — auto-filled by `/onboarding`, read by Claude every session |
| `PROJECT-PLAN.md` | Full 5-phase implementation plan with tasks, gates, and methodology |
| `COMMAND-DIRECTORY.md` | Annotated repo structure, slash command reference, skill inventory, MCP table |
| `META/CLAUDE.md` | How to use the META pattern for cross-session Claude Code continuity |
| `.claude/skills/onboarding/` | The onboarding skill triggered by `/onboarding` |

---

## Key Design Principles

**Compliance before configuration.**
No MCP server is installed without approval. File requests early — approval lead time is the only external dependency you cannot control.

**Human in the loop, always.**
No skill auto-sends, auto-publishes, or auto-commits. Every skill produces a draft. The human decides what happens next.

**Documentation before automation.**
A workflow that isn't documented cannot be reliably automated. Phase 3 is a prerequisite for Phase 4.

**Cognitive Task Analysis (CTA) for workflow docs.**
Standard documentation captures the happy path. CTA forces documentation of exceptions, judgment calls, and implicit checks — the knowledge that lives in experts' heads.

**Tiered rollout over big-bang launch.**
Non-technical team members get Claude.ai Projects. Power users get Claude Code slash commands. Match the tool to the user's comfort level.

**Draft branches protect main.**
All work lives on `draft/` branches. `main` is always in a working state.

---

## Who This Is For

- Technical leads or ops leads bringing structured AI tooling to a non-technical team
- Anyone building a Claude Code skill library for internal use
- Teams with compliance requirements around AI tool adoption
- Anyone who has tried "just give the team ChatGPT access" and found it didn't stick

---

## Branch Naming Convention

```
draft/phase1-setup              Phase 1 initial repo and CLAUDE.md setup
draft/skill-[skill-name]        Per-skill development
draft/workflow-[name]           Per-workflow documentation
```
