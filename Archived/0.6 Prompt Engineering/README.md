# 0.6 — Prompt Engineering for Product Builders

> **📌 End of Mini Project 2.**
> At the end of this session, your pair or group submits the Bolt app you have been building across Sessions 4, 5, and 6. It should be clean, functional, and clearly show the work of both team members. Share your public Bolt URL with your instructor.

## Objective

By the end of this lab, you will have applied four prompt engineering techniques to your agent — directly inside your Bolt app — and compared the outputs before and after each change.

All improvements to your system prompt are made by **prompting Bolt**.

---

## Lab Steps

### Step 1: Technique 1 — Tighten the role definition

- Look at your current system prompt. Does it clearly define:
  - WHO the agent is?
  - WHAT it does?
  - WHAT IT WILL NOT DO?
- Prompt Bolt to update the system prompt with a more precise role definition.
- Test: does the agent stay in role when you send it off-topic messages?

### Step 2: Technique 2 — Force structured output

- Prompt Bolt to update the system prompt so every response follows this exact format:
  ```
  [Summary]: one sentence
  [Response]: your main answer
  [Next Step]: one action the user should take
  ```
- Test the output. Does the agent follow the format consistently across multiple messages?

### Step 3: Technique 3 — Add a few-shot example

- Prompt Bolt to add one example of a perfect input-output pair to the system prompt.
- Format: `User: [example input] / Agent: [example output]`
- Test again. Does the tone or format improve?

### Step 4: Technique 4 — Chain-of-thought

- Prompt Bolt to add this instruction to the system prompt:
  ```
  Before answering, briefly think through the problem step by step.
  Do not show your thinking — only show the final formatted response.
  ```
- Test with a complex question. Does the quality improve?
- Run the same question with and without this instruction and compare.

### Step 5: Submit — Mini Project 2

- Your app should now have: two agents, a polished UI, structured responses, and consistent behavior.
- Both team members' names should be visible somewhere in the app (title, subtitle, or about section).
- Share your public Bolt URL with your instructor.

---

## Starter Prompts

```
# Technique 1 — Tighten the role:
Update the system prompt to clearly define:
- WHO the agent is (name and role)
- WHAT it does (specific task)
- WHAT IT WILL NOT DO (clear boundaries)

# Technique 2 — Structured output:
Update the system prompt so every response uses this exact format:
[Summary]: one sentence repeating what the user asked
[Response]: the main answer
[Next Step]: one concrete action the user can take

# Technique 3 — Few-shot example:
Add this example at the end of the system prompt:
User: [your example input]
Agent:
[Summary]: ...
[Response]: ...
[Next Step]: ...

# Technique 4 — Chain-of-thought:
Add this to the system prompt:
"Before answering, think through the problem step by step.
Do not show your thinking. Only show the formatted output."
```

---

## Expected Output

```
>> I need to prepare for a coding interview in 2 days.

[Summary]: You have a coding interview in 2 days and need to prepare.
[Response]: Focus on arrays, trees, and dynamic programming.
Spend 45 minutes per topic with real practice problems.
[Next Step]: Solve 2 array problems on LeetCode right now.
```

---

## Bonus Challenges

🟡 **Bonus 1**
- Create two versions of your system prompt — one with structured format, one without.
- Run the same 3 messages through both. Write down which responses are more useful and why.

🟠 **Bonus 2**
- Prompt Bolt to add this line at the top of your system prompt:
  `"You are an expert instruction follower. You always follow the format exactly."`
- Test whether this improves how consistently the agent follows the format.

🔴 **Bonus 3**
- Prompt Bolt to add a built-in A/B test mode: a toggle that switches between two versions of your system prompt.
- Use it to compare which prompt produces better responses for the same question.
