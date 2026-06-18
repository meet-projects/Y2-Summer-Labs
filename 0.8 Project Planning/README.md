# 0.8 — Plan and Architect Your Final Project

## Objective

By the end of this lab, your team will have a written project plan: the problem you are solving, your architecture, your agent designs, and a task list with owners.

**Nothing is built yet in this lab.** This session is about thinking clearly before you write a single prompt.

---

## Lab Steps

### Step 1: Define — What are you building?

As a team, answer these questions in writing:

1. What does your app do? (1–2 sentences)
2. Who is the user?
3. How many agents does your app have, and what does each one do?
4. What would a bad version of this app look like? What makes yours better?

### Step 2: Design — Map your agents

Each team member owns one agent. Define yours:

- Agent name and role
- What the user says to it
- What it always does and what it never does
- What format it responds in

Write a first draft of your system prompt. You will refine it in Session 9.

### Step 3: Design — Draw the architecture

On paper or a whiteboard, draw your app:

- One box for the Bolt frontend
- One box per agent (system prompt inside)
- One box for the database (if you're using Supabase)
- Arrows showing the flow of data between boxes

Photograph your diagram and keep it — you will refer to it in Session 9.

### Step 4: Plan — Write the task list

- Break your project into tasks. Each task should take no more than 30 minutes.
- Use the template below. Assign each task to one team member.
- Mark which tasks are MVP (must have for launch) and which are nice-to-have.
- Be honest: can your team finish the MVP in Session 9?

---

## Planning Template

```
# ─── PROJECT DEFINITION ─────────────────────────────────
PROJECT_NAME = ''
PROBLEM      = ''   # What problem does this solve?
USER         = ''   # Who uses this?

# ─── AGENTS ─────────────────────────────────────────────
# Agent 1:
#   Name:
#   Role:
#   System prompt draft:

# Agent 2:
#   Name:
#   Role:
#   System prompt draft:

# Agent 3:
#   Name:
#   Role:
#   System prompt draft:

# Agent 4:
#   Name:
#   Role:
#   System prompt draft:

# ─── ARCHITECTURE ───────────────────────────────────────
# Frontend:   Bolt.new (UI + deployment)
# AI:         Anthropic Claude API via Bolt
# Database:   JSON (local) / Supabase (cloud) / none

# ─── TASK LIST ──────────────────────────────────────────
tasks = [
  {'task': 'Write system prompt — Agent 1', 'owner': '', 'priority': 'MVP'},
  {'task': 'Write system prompt — Agent 2', 'owner': '', 'priority': 'MVP'},
  {'task': 'Write system prompt — Agent 3', 'owner': '', 'priority': 'MVP'},
  {'task': 'Write system prompt — Agent 4', 'owner': '', 'priority': 'MVP'},
  {'task': 'Build Bolt app with all agent tabs', 'owner': '', 'priority': 'MVP'},
  {'task': 'Test and refine each agent', 'owner': '', 'priority': 'MVP'},
  {'task': 'Add Supabase persistence', 'owner': '', 'priority': 'nice-to-have'},
  {'task': 'Polish UI and deploy', 'owner': '', 'priority': 'MVP'},
]
```

---

## Deliverables

By the end of this lab your team should have:

1. Written project definition (problem, user, agents)
2. Architecture diagram (photographed)
3. First draft of all four system prompts
4. Task list with owners and priorities

---

## Bonus Challenges

🟡 **Bonus 1**
- Write a 2-sentence elevator pitch for your app. Read it out loud to another team.

🟠 **Bonus 2**
- Create a simple wireframe of your UI: sketch what the screen looks like when a user opens your app. Label every element.

🔴 **Bonus 3**
- Write a failure pre-mortem: imagine your project fails completely. Write 3 specific reasons why — then write what you will do to prevent each one.
