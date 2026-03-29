# Onboarding Skill — /onboarding

## Purpose

Walk a new user through a structured Q&A session to understand their team, tools, workflows, and constraints. At the end, automatically write a completed `CLAUDE.md` so they are ready to begin Phase 1 of the AI Architecture for Teams project.

## When to Trigger

- User runs `/onboarding`
- User opens the project and `CLAUDE.md` still contains `[NOT SET]` placeholders
- User says "let's set up", "start from scratch", "configure this", or similar

## Workflow

### Stage 0 — Welcome

Greet the user warmly. Explain what's about to happen in plain language:

> "Welcome to AI Architecture for Teams. Before we build anything, I need to understand your team, your tools, and what you're actually trying to solve. I'll ask you a series of questions in a few rounds — your answers will be used to build a `CLAUDE.md` file that gives me the context I need in every future session. This takes about 10–15 minutes. Ready?"

Wait for confirmation before proceeding.

---

### Stage 1 — Team Basics (ask all at once, numbered)

Ask these as a single numbered list. Wait for all answers before moving on.

1. What is your team's name or what do you call yourselves? (e.g. "Budget & Ops Team", "Data Platform Team")
2. What does your team do in one or two sentences? What does a successful week look like?
3. How many people are on the team, including you?
4. What is your role and title?
5. How would you describe your team's technical comfort level? (e.g. "mostly non-technical", "mixed", "mostly engineers")

---

### Stage 2 — Tool Stack (ask all at once, numbered)

> "Now let's map your tool stack. For each tool, I need to know what your team actually uses it for — not just that you use it."

6. What is your primary data or analytics tool? (e.g. Snowflake, BigQuery, Redshift, Excel) What do you use it for?
7. What does your team use for project/task management? (e.g. Notion, Airtable, Jira, Asana) What do you use it for?
8. What do you use for team communication? (e.g. Slack, Teams, email)
9. What do you use for document storage and sharing? (e.g. Google Drive, SharePoint, Confluence)
10. Any other tools that are central to how your team works? List them and what they're used for.

---

### Stage 3 — Core Workflows (ask all at once, numbered)

> "Now I need to understand your core workflows — the recurring processes your team runs. These will be the focus of Phase 3 (documentation) and Phase 4 (automation)."

11. List your team's 3–5 most important recurring workflows. For each, give it a name and one sentence on what it produces. (e.g. "Weekly spend report — produces a summary of budget actuals sent to leadership every Monday")
12. Which of those workflows is the most painful or time-consuming right now?
13. Which workflow would have the highest impact if it were fully documented and automated?
14. Which workflow is most at risk — the one where if a key person left, things would break?

---

### Stage 4 — Constraints & Reality Check (ask all at once, numbered)

> "Last round. These questions help me scope the plan to what's actually achievable."

15. How many hours per week can you realistically dedicate to building this system? (Be honest — not the ideal, the real number.)
16. Does your company have a compliance or IT approval process for AI tools and integrations? If yes, roughly how long does approval take?
17. Are there any hard deadlines — audits, fiscal year end, leadership reviews — that affect your timeline?
18. What has already been tried? Any previous attempts at documentation, automation, or tooling — what happened?
19. What would make this project fail? What are you most worried about?

---

### Stage 5 — Synthesis & Confirmation

After receiving all answers:

1. Summarize back what you heard in 6–8 bullet points covering: team context, tool stack, top workflows, biggest pain, key constraints
2. Flag any contradictions or gaps — e.g. "You mentioned only 2 hours/week but also a 6-week deadline — that's tight, want to talk about scope?"
3. Ask: "Does this summary accurately reflect your situation? Anything to correct or add before I write your CLAUDE.md?"

Wait for confirmation.

---

### Stage 6 — Write CLAUDE.md

Once confirmed, write a completed `CLAUDE.md` using the answers. Replace every `[NOT SET]` placeholder with real content derived from the answers.

**CLAUDE.md sections to fill in:**
- Team name, size, department, what the team does
- My role
- Team roles (list each functional role from their answers, one line per role)
- Technical comfort level breakdown (lead / power users / everyone else)
- Tool stack (one entry per tool with what it's used for)
- Core workflows (one entry per workflow with name, what it produces, owner role, frequency, key tools)

**Rules for writing CLAUDE.md:**
- Use the user's own language — don't paraphrase into corporate speak
- Keep workflow descriptions concrete: what gets produced, who receives it, how often
- Do NOT include the organization's real name — use `[Your Organization]` as a placeholder for privacy
- Remove the `STATUS: NOT CONFIGURED` block at the top
- Keep all Hard Rules and Output Guidelines sections intact

After writing, show the completed CLAUDE.md to the user and ask:
> "Here's your completed CLAUDE.md. Review it and let me know if anything needs adjusting before I save it."

---

### Stage 7 — Save and Next Steps

Once the user approves the CLAUDE.md:

1. Save the file (overwrite the template version)
2. Tell the user:
   > "Your CLAUDE.md is ready. You're now set up for Phase 1. Here's what comes next:
   >
   > **Immediate next actions:**
   > 1. Create your `team-ai` GitHub repo with branch protection on `main`
   > 2. Open `PROJECT-PLAN.md` — it's your full implementation roadmap
   > 3. File your MCP compliance approval requests (Phase 2) — do this now, approval takes time
   >
   > Whenever you're ready to start Phase 1, just say 'let's begin' and I'll walk you through it."

---

## Quality Rules

- Never skip a stage — all questions must be answered before writing CLAUDE.md
- Never fill in CLAUDE.md with guesses or assumptions — only use answers the user provided
- Never include the user's organization name in CLAUDE.md (privacy)
- If a user skips a question, ask it again before moving to the next stage
- The tone throughout should be warm and conversational — this is a setup session, not an interview
