# 0.3 — Build a Goal-Based AI Agent

## Objective

By the end of this lab, you will transform your chatbot from a freeform assistant into a goal-based AI agent: one that has a clear purpose, gives structured output, and remembers context across the conversation.

This is your **Mini Project 1** submission. Take it seriously — make it clean, focused, and well-prompted.

---

## Lab Steps

### Step 1: Design — Choose your agent's purpose

- Pick **one** goal for your agent. Examples: interview coach, coding debugger, study quiz bot, presentation feedback assistant, MEET project advisor.
- Write down on paper:
  1. What is the agent's job?
  2. What should it always do?
  3. What should it never do?
- You will turn this into a system prompt.

### Step 2: Build — Write a goal-focused system prompt

- Replace the existing `system_message` with a new one based on your agent's goal.
- Your system prompt **must include**:
  - The agent's name and role
  - What it does when the user speaks
  - What format it responds in
  - At least one rule (always / never)
- Use the starter template below as a starting point.

### Step 3: Test — Validate behavior across multiple turns

- Send at least 4 messages that test different situations.
- Does it stay in role? Does it remember earlier messages?
- Try to break it: send a message outside its scope. What happens?
- Refine the system prompt based on what you observe. Run again.

### Step 4: Submit — Mini Project 1

- Make sure your `app.py` runs cleanly with no errors.
- Your agent should have: a clear role, structured responses, and consistent behavior.
- Submit your `agent` folder for review.

---

## Starter Code

```python
system_message = """
You are [NAME], a [ROLE].

Your job is to [MAIN TASK].

Rules:
- Always [RULE 1]
- Always [RULE 2]
- Never [RULE 3]

Response format:
- Start with a one-sentence summary of what the user said.
- Then give your response.
- End with one follow-up question.
"""
```

---

## Expected Output

```
>> I have an interview tomorrow for a software engineering role.

Agent: Got it — you have a software engineering interview tomorrow.
Let's get you ready. Tell me: what types of questions are you most
worried about — technical coding, system design, or behavioral?
```

---

## Bonus Challenges

🟡 **Bonus 1**
- Add a goal tracker: at the start of the session, ask the user what their goal is today.
- Store it in a variable and include it in every message sent to the API.

🟠 **Bonus 2**
- Add a `/summary` command: when the user types `/summary`, the agent reviews the full conversation and gives a structured summary of what was discussed.

🔴 **Bonus 3**
- Make the agent score the user's responses (e.g., for interview practice, rate each answer 1–5 and explain why).
- Include the scoring rubric in the system prompt.
- Track the scores in a list and print the average at the end.
