# Team AI: Documentation & Workflow Automation System
## PROJECT-PLAN.md

**Project:** Team AI — Documentation & Workflow Automation
**Owner:** [Your Name] (Technical Lead)
**Start Date:** 2026-03-26
**Target Completion:** Week 12 (~2026-06-18)
**Status:** Planning

---

## Quick Reference: Phases at a Glance

| Phase | Name | Weeks | Owner | Key Deliverable |
|-------|------|-------|-------|-----------------|
| 1 | Repo Setup & CLAUDE.md | 1–2 | Lead | Functional GitHub repo, CLAUDE.md loads in Claude Code |
| 2 | MCP Integrations | 1–2 (parallel) | Lead + Compliance | Approved integrations tested and documented |
| 3 | Workflow Documentation Capture | 3–5 | Lead + Team | 5 complete workflow docs on `main` |
| 4 | Skills & Slash Command Build-out | 6–9 | Lead | 5 skills merged, slash commands operational |
| 5 | Team Rollout | 10–12 | Lead + Team | 100% access; 80% self-sufficient within 2 weeks |

---

## Phase 1: Repo Setup & CLAUDE.md
**Weeks 1–2 | Owner: Lead only**

### Overview
Establish the foundational repository and the core context file (`CLAUDE.md`) that will orient Claude in every future session. Nothing else can proceed until Claude can correctly answer questions about team context from CLAUDE.md.

### Tasks

| # | Task | Notes |
|---|------|-------|
| 1 | Create `team-ai` GitHub repo | Enable branch protection on `main`: PR required, no direct push |
| 2 | Create full directory structure | Skeleton files with headers only — see COMMAND-DIRECTORY.md for full tree |
| 3 | Write `CLAUDE.md` | Team context, tool stack, workflow inventory, tone and output guidelines for Claude |
| 4 | Write `docs/STRATEGY.md` | AI strategy rationale and guiding principles |
| 5 | Write `docs/DECISIONS.md` | Log of major architectural decisions with rationale (start here, update throughout) |
| 6 | Write `docs/workflows/TEMPLATE.md` | Standardized workflow doc template all team members will use in Phase 3 |
| 7 | Write `README.md` | Repo purpose, how to contribute, branch strategy |

### Branch Strategy
All work in Phase 1 happens on feature branches (`draft/phase1-setup`). Merge to `main` only after CLAUDE.md gate is passed.

### Deliverable
Functional repo on GitHub. CLAUDE.md loads correctly in Claude Code (`/context` check confirms).

### Gate — Must pass before Phase 2 work is merged or Phase 3 begins
> Claude Code can load CLAUDE.md and correctly answer questions about team context (team size, tool stack, core workflows, output tone) without additional prompting.

---

## Phase 2: MCP Integrations
**Weeks 1–2 (parallel with Phase 1) | Owner: Lead + Compliance**

### Overview
Connect Claude Code to the team's live data sources via Model Context Protocol (MCP) servers. **No unapproved MCP server will be installed.** All integrations require compliance sign-off before configuration.

### Priority Integration Order

| Priority | Tool | Status | Notes |
|----------|------|--------|-------|
| 1 | Snowflake | Likely needs compliance review | Community/custom MCP server — flag early; see below |
| 2 | Notion | TBD — audit first | Check if company-approved server exists |
| 3 | Airtable | TBD — audit first | Check if company-approved server exists |
| 4 | Slack | TBD — audit first | Check if company-approved server exists |

### Tasks

| # | Task | Notes |
|---|------|-------|
| 1 | Audit existing company-approved MCP servers | Document which tools already have approved servers |
| 2 | File compliance/approval requests for any gaps | Do NOT install unapproved servers — document request date and expected turnaround |
| 3 | For each approved server: configure in `settings.json` | Read-only permission scope only at this stage |
| 4 | For each approved server: run read-only smoke test | Confirm data is returned; document in `DECISIONS.md` |
| 5 | For each approved server: document connection details | Permission scopes, auth method, any known limitations |
| 6 | For blocked integrations: document workaround or deferral | Do not leave gaps undocumented |

### Snowflake Flag
Snowflake does not have an official Anthropic-maintained MCP server as of this writing. A community or custom server will likely be required. **File the compliance review request in Week 1.** If approval is delayed, document a manual query workaround (copy-paste Snowflake results into Claude) so Phase 4 skill testing is not blocked.

### Deliverable
Each approved MCP integration: configured, smoke-tested with read-only queries, and documented in `DECISIONS.md`.

### Gate — Must pass before Phase 4 skills connect to live data
> Claude Code can execute a live Snowflake spend query and return data. Blocked integrations have a documented workaround or deferral decision in `DECISIONS.md`.

---

## Phase 3: Workflow Documentation Capture
**Weeks 3–5 | Owner: Lead orchestrates; each team member owns their workflow doc**

### Overview
Capture the team's five core workflows as complete, structured documentation that a new hire could follow. This phase uses **Cognitive Task Analysis (CTA)** — a research-backed method for surfacing tacit expert knowledge.

---

> **What is CTA and why does it matter?**
>
> CTA (Cognitive Task Analysis) is a framework for capturing the "how I actually do it" that gets lost when people write down only the official steps. Standard documentation captures the happy path. CTA forces documentation of exceptions, judgment calls, error recovery, and implicit checks — the knowledge that lives in an expert's head and is invisible until something goes wrong.
>
> The key CTA technique used here: **ask about failure and edge cases, not the normal flow.** "What do you do when X breaks?" surfaces more useful knowledge than "walk me through the process."

---

### Sub-phase 3A — Existing Doc Audit
**Week 3 | Lead only**

| # | Task |
|---|------|
| 1 | Pull all existing docs from Google Drive, Notion, Confluence, relevant Slack threads |
| 2 | Run AI-assisted gap analysis against the workflow inventory in CLAUDE.md |
| 3 | Produce a gap matrix: workflow × coverage level (full / partial / missing) |
| 4 | Prioritize capture effort by gap level + business criticality |

**Deliverable:** Gap matrix doc committed to `docs/` before interview scheduling begins.

---

### Sub-phase 3B — Structured Interviews
**Week 4 | Lead + each workflow owner**

For each of the 5 core workflows, conduct a 60-minute interview with the primary owner.

**CTA Question Set (use all of these in every interview):**

| Question | Purpose |
|----------|---------|
| "Walk me through the last time you did this end to end." | Gets a concrete instance, not the idealized version |
| "What do you do when X goes wrong?" | Surfaces error recovery and judgment calls |
| "What does a new person always get wrong the first time?" | Identifies invisible assumptions |
| "What do you check before you consider this done?" | Captures implicit quality criteria |
| "What would break if you weren't here?" | Identifies undocumented dependencies |

**Process:**
1. Record all sessions (with explicit consent from each participant)
2. Transcript → structured doc using `docs/workflows/TEMPLATE.md`
3. Lead does synthesis; interviewee reviews and approves before doc is committed
4. No doc is committed to `main` without interviewee sign-off

---

### Sub-phase 3C — Screen Recording Walkthroughs
**Weeks 4–5 | Team**

High-complexity workflows get a screen recording (Loom or equivalent). Priority candidates:

- Snowflake navigation and query workflows
- Airtable task lifecycle management
- Report generation end-to-end

**Rules:**
- Recording is linked from the workflow doc, not a substitute for it
- Written doc must be complete and self-contained; video is supplementary
- No recordings of sensitive data; use test/sample data if needed

---

### Sub-phase 3D — Direct Writing + Review
**Week 5 | Team + Lead review**

| # | Task |
|---|------|
| 1 | Each team member writes first draft for their workflow using TEMPLATE.md |
| 2 | Lead reviews using the CTA gap checklist (exceptions covered, decisions explained, new-hire followable) |
| 3 | Revisions on `draft/workflow-[name]` branches |
| 4 | PR to `main` only when lead has approved completeness |

---

### Deliverable
5 complete workflow docs committed to `main`. Gap analysis report saved to `docs/`.

### Gate — Must pass before Phase 4 begins
> Each workflow doc passes the CTA completeness checklist: exceptions are covered, judgment calls are explained, and a new hire could follow the doc without asking for help.

---

## Phase 4: Skills & Slash Command Build-out
**Weeks 6–9 | Owner: Lead only**

### Overview
Build the five highest-ROI automations as Claude Code skills with corresponding slash commands. Each skill is a structured prompt + workflow that Claude executes; every skill has a mandatory human review checkpoint before any output leaves Claude Code.

### Build Order (highest ROI first)

| Priority | Skill Name | Rationale |
|----------|-----------|-----------|
| 1 | `weekly-report-gen` | Highest-frequency manual task — immediate time savings |
| 2 | `budget-forecast` | Highest business value; connects to Snowflake data |
| 3 | `task-handoff` | Most common team interaction; reduces handoff errors |
| 4 | `audit-workflow` | Compliance-critical; seasonally time-sensitive |
| 5 | `onboarding-guide-gen` | Lower frequency but high strategic value for team growth |

### Per-Skill Build Process

For each skill, follow this sequence:

| Step | Task |
|------|------|
| 1 | Create branch `draft/skill-[name]` |
| 2 | Write `skills/[name]/SKILL.md` — purpose, inputs, outputs, step-by-step logic, human review checkpoint |
| 3 | Write `.claude/commands/[name].md` — the slash command Claude executes |
| 4 | Test on synthetic or historical data only — do NOT connect to live MCP data yet |
| 5 | Lead runs the skill 3+ times with real-ish inputs; validates output quality |
| 6 | PR to `main` with a test log attached — log must show at least 3 representative runs |

### Non-Negotiable Rule: Human Review Checkpoint
**Every skill must include an explicit human review step.** No skill may:
- Auto-publish output to any system
- Auto-send messages, emails, or Slack posts
- Auto-commit files to any repository
- Auto-submit forms or update records

The output of every skill is a draft for human review. The human decides what happens next.

### Deliverable
5 skills merged to `main`. Each has a passing test log in its PR.

### Gate — Must pass before Phase 5 rollout
> Each skill can be triggered via its slash command, produces reviewable output, and has a documented and enforced human checkpoint before any output leaves Claude Code.

---

## Phase 5: Team Rollout — Tiered, Low-Friction
**Weeks 10–12 | Owner: Lead sets up; team participates voluntarily**

### Overview
Roll out AI tooling in two tiers matched to technical comfort level. The goal is adoption, not training completion. Success is measured by independent use, not attendance.

---

### Tier 1 — Claude.ai Projects
**Weeks 10–11 | All non-technical team members**

| # | Task |
|---|------|
| 1 | Lead creates a Claude.ai Project per major workflow area |
| 2 | Upload: relevant CLAUDE.md sections, workflow docs, output templates |
| 3 | Configure custom instructions per project: tone, output format, review reminders |
| 4 | Run a 15-minute Slack demo — show one real workflow, not a features tour |
| 5 | No training decks, no required reading — "here's the thing, try it" |

**Why this approach:** Non-technical team members are more likely to engage when onboarding is immediate and low-stakes. The demo shows a real use case they recognize. The Projects context means they get useful output from the first message.

---

### Tier 2 — Claude Code Slash Commands
**Week 12 | Power users only (1–2 willing volunteers)**

| # | Task |
|---|------|
| 1 | Identify 1–2 willing team members for early access |
| 2 | Async Loom walkthrough: running a command, reviewing output, what NOT to do |
| 3 | Create dedicated Slack channel `#ai-tools` for questions, wins, and issues |

---

### Feedback & Iteration Loop

| Week | Action |
|------|--------|
| 10–13 | Weekly `#ai-tools` prompt: "What worked? What was confusing? What wasted time?" |
| Each week | Lead reviews feedback; queues fixes on `draft/` branches |
| Week 12 | Leadership report: usage counts, time saved (self-reported), error catches |

---

### Deliverable
100% of team has Claude.ai Project access. At least 2 team members have used a skill output in a real workflow.

### Gate — Final project success criteria
> 80% of team has used at least one AI-assisted workflow without needing help from the lead within 2 weeks of Tier 1 launch.

---

## Appendix: Key Principles

1. **Compliance before configuration.** No MCP server is installed without approval. Document every approval request and response.

2. **Human in the loop, always.** No automation publishes, sends, or commits without a human reviewing the output first. This is non-negotiable.

3. **Documentation before automation.** A workflow that isn't documented cannot be reliably automated. Phase 3 is a prerequisite for Phase 4, not a suggestion.

4. **Low friction over completeness.** A tool the team actually uses beats a comprehensive system nobody touches. Default to the simpler interface.

5. **Draft branches protect main.** All work lives on `draft/` branches until it's been tested and reviewed. `main` is always in a working state.

6. **Capture tacit knowledge.** The CTA methodology in Phase 3 exists because the most valuable team knowledge is often the least documented. Invest time here — it compounds.
