# Team AI: Command & Directory Reference
## COMMAND-DIRECTORY.md

**Project:** Team AI — Documentation & Workflow Automation
**Owner:** [Your Name] (Technical Lead)
**Purpose:** Standalone reference for repository structure, slash commands, skills, and MCP integrations
**Audience:** Lead and power users; formatted for print-to-PDF

---

## Section 1: Annotated Repository Directory Tree

The full `team-ai/` repository structure. Every file and folder is listed with a one-line description of its purpose.

    team-ai/
    │
    ├── .claude/
    │   │   Claude Code configuration directory — not committed to public branches
    │   │
    │   ├── commands/
    │   │   │   Slash command definitions — one file per command
    │   │   │
    │   │   ├── weekly-report-gen.md        Slash command: generate weekly status report draft
    │   │   ├── budget-forecast.md          Slash command: run budget forecast from Snowflake data
    │   │   ├── task-handoff.md             Slash command: generate structured task handoff doc
    │   │   ├── audit-workflow.md           Slash command: run compliance audit workflow checklist
    │   │   └── onboarding-guide-gen.md     Slash command: generate onboarding guide for a new role
    │   │
    │   └── settings.json                   Claude Code settings: MCP server configs, permissions, env vars
    │
    ├── skills/
    │   │   Skill definitions — one folder per skill, each with its own SKILL.md
    │   │
    │   ├── weekly-report-gen/
    │   │   └── SKILL.md                    Purpose, inputs, outputs, logic steps, human review checkpoint
    │   │
    │   ├── budget-forecast/
    │   │   └── SKILL.md                    Purpose, inputs, outputs, logic steps, human review checkpoint
    │   │
    │   ├── task-handoff/
    │   │   └── SKILL.md                    Purpose, inputs, outputs, logic steps, human review checkpoint
    │   │
    │   ├── audit-workflow/
    │   │   └── SKILL.md                    Purpose, inputs, outputs, logic steps, human review checkpoint
    │   │
    │   └── onboarding-guide-gen/
    │       └── SKILL.md                    Purpose, inputs, outputs, logic steps, human review checkpoint
    │
    ├── docs/
    │   │   Long-form documentation — strategy, decisions, workflow docs, templates
    │   │
    │   ├── workflows/
    │   │   │   One file per documented team workflow
    │   │   │
    │   │   ├── TEMPLATE.md                 Standardized template all workflow docs must follow
    │   │   ├── workflow-[name].md          Completed workflow doc (one file per workflow; created in Phase 3)
    │   │   └── gap-analysis.md             Gap matrix from Phase 3A audit: workflow × coverage level
    │   │
    │   ├── STRATEGY.md                     AI strategy rationale, guiding principles, and long-term direction
    │   └── DECISIONS.md                    Log of major architectural decisions with rationale and date
    │
    ├── CLAUDE.md                           Primary context file: team context, tool stack, workflow inventory, tone guidelines
    └── README.md                           Repo purpose, how to contribute, branch naming strategy

---

## Section 2: Slash Command Quick Reference

All commands are triggered in Claude Code with a `/` prefix. All commands produce draft output for human review — none auto-publish or auto-send.

    Command Name            What It Does                                        Who Uses It
    ─────────────────────────────────────────────────────────────────────────────────────────────────
    /weekly-report-gen      Pulls team activity data and generates a            Lead; power users
                            structured weekly status report draft.
                            Output: markdown doc ready for review and send.

    /budget-forecast        Queries Snowflake for current spend data and        Lead
                            generates a budget forecast with variance notes.
                            Output: forecast table + narrative summary draft.

    /task-handoff           Takes task context as input and generates a         Lead; power users
                            structured handoff document with open items,
                            dependencies, and next-owner instructions.
                            Output: handoff doc for review before sharing.

    /audit-workflow         Runs through the compliance audit checklist for     Lead
                            a specified workflow, flagging gaps or risks.
                            Output: annotated checklist draft for review.

    /onboarding-guide-gen   Takes a role description and generates a            Lead
                            structured onboarding guide with workflow links,
                            tool access steps, and first-30-days checklist.
                            Output: onboarding doc draft for review.

---

## Section 3: Skill Inventory

Each skill is a structured prompt + workflow executed by Claude Code. Every skill has a mandatory human review checkpoint — no skill output is published, sent, or committed without explicit human approval.

    Skill Name              Inputs Required                Outputs Produced              Human Review Step
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────
    weekly-report-gen       Date range; team member        Structured weekly status      Lead reads and edits
                            names or IDs; activity         report in markdown; optional  draft before sending
                            source (Snowflake / manual)    section for blockers/risks    to any audience

    budget-forecast         Fiscal period; budget          Forecast table with actuals,  Lead verifies numbers
                            category; Snowflake query      projected spend, variance,    against source before
                            scope                          and narrative summary         sharing with leadership

    task-handoff            Task name; current owner;      Structured handoff doc with   Sending owner reviews
                            context notes; next owner      open items, dependencies,     and approves before
                            (if known); deadline           next steps, and open Qs       delivering to recipient

    audit-workflow          Workflow name; audit period;   Annotated checklist with      Lead reviews flagged
                            compliance framework or        pass/fail/flag per step;      items and determines
                            checklist reference            risk summary narrative        remediation actions

    onboarding-guide-gen    Role title; start date;        Structured onboarding guide   Lead reviews for
                            team; tool access list;        with day-by-day checklist,    accuracy before
                            primary workflows              workflow links, contact list  sharing with new hire

---

## Section 4: MCP Integration Reference

MCP (Model Context Protocol) servers connect Claude Code to live data sources. All integrations require compliance approval before installation. Read-only scope is the default; write access requires a separate approval.

    Tool        MCP Server              Permission Scope        Approval Status       Notes
    ──────────────────────────────────────────────────────────────────────────────────────────────────
    Snowflake   Community / custom      Read-only by default;   Pending compliance    No official Anthropic
                server (TBD)            write requires separate review (file Week 1)  server exists; community
                                        approval                                      or custom server needed

    Notion      TBD — pending audit     Read-only by default    Pending audit         Check company-approved
                of approved servers                             (complete Week 1)     server list first

    Airtable    TBD — pending audit     Read-only by default    Pending audit         Check company-approved
                of approved servers                             (complete Week 1)     server list first

    Slack       TBD — pending audit     Read-only by default    Pending audit         Check company-approved
                of approved servers                             (complete Week 1)     server list first

    ─────────────────────────────────────────────────────────────────────────────────────────────────
    Note: "Pending audit" means the company-approved MCP server list has not yet been checked for
    this tool. Do not install any server before audit and compliance approval are both complete.
    Document all approvals and denial decisions in docs/DECISIONS.md with date and approver name.

---

## Reference Notes

**Branch naming convention:**

    draft/phase1-setup          Phase 1 initial repo and CLAUDE.md setup
    draft/skill-[skill-name]    Per-skill development branch (e.g. draft/skill-budget-forecast)
    draft/workflow-[name]       Per-workflow documentation branch (e.g. draft/workflow-snowflake-query)

**Key rule — main is always stable:** No work merges to `main` without a PR. No direct pushes. Branch protection is enforced from day one.

**Key rule — human checkpoint is mandatory:** Every skill and slash command produces a draft. The human decides what happens to that draft. Nothing auto-sends, auto-publishes, or auto-commits.
