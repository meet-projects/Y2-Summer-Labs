# 0.2 — Understand the Backend & the API

## Objective

By the end of this lab, you will understand the flow of data from your Python code to the Anthropic API and back. You will read the full API response, change key parameters, and observe the effects.

The goal is not just to make it work — it is to understand **why** it works.

---

## Lab Steps

### Step 1: Inspect — Read what the API actually returns

- Run your `app.py` from Session 1.
- Before printing the reply, add this line:
  ```python
  print(response)
  ```
- Send a message and look at the full response object printed in the terminal.
- Find these fields in the output: `id`, `model`, `role`, `content`, `stop_reason`, `usage`
- Write down: What does `usage.input_tokens` and `usage.output_tokens` mean?

### Step 2: Experiment — Change the parameters

- Change `max_tokens` to `50`. Send a long question. What happens?
- Change `max_tokens` back to `300`.
- Change `temperature` to `0`. Send the same message 3 times. Are the answers identical?
- Change `temperature` to `1`. Send the same message 3 times. What do you notice?
- Write down: What does temperature actually control?

### Step 3: Read the history — See the messages list

- After 3 turns of conversation, add this line **before** the API call:
  ```python
  print('History:', history)
  ```
- Send a message and look at what gets printed.
- How many messages are in the history after 3 turns? (Hint: it's more than 3.)
- Write down: Why does the API need the full history every single time?

---

## Starter Code

```python
# Add this BEFORE the API call to inspect the full response:
# print(response)

# Add this BEFORE the API call to see the full message history:
# print('History so far:', history)

# Parameters you will experiment with:
response = client.messages.create(
    model='claude-3-haiku-20240307',
    max_tokens=300,   # try 50, then 500
    temperature=0.7,  # try 0, then 1
    system=system_message,
    messages=history
)
```

---

## Expected Output

```
History: [
  {'role': 'user', 'content': 'Hello'},
  {'role': 'assistant', 'content': 'Hi! How can I help you today?'},
  {'role': 'user', 'content': 'Tell me a joke'},
]
Usage: input_tokens=45, output_tokens=30
```

---

## Bonus Challenges

🟡 **Bonus 1**
- Print the token usage after every reply in a readable format.
- Example: `[Tokens used — In: 45 | Out: 30 | Total: 75]`

🟠 **Bonus 2**
- Add a token counter that tracks the total tokens used across the whole conversation.
- Print the running total after each turn.

🔴 **Bonus 3**
- Estimate the cost of the conversation using Haiku pricing (~$0.25 per million input tokens, ~$1.25 per million output tokens).
- Print the estimated cost in cents after every turn.


<br>

## 🧠 Reflection — Lab 0.2

*~10 min at the end of lab. Solo and honest.*

**1 · Personal Analogy — tokens as the unit of cost.**
Tokens are what you pay in. Every message in `history` gets re-sent and re-counted *every*
turn, so the longer the chat runs, the more each new reply costs. **Where in your world
does a price quietly add up per-unit like this — something you actually keep an eye on?**
(Banned: "it's like a taxi meter." Find your own. 2–4 sentences.)

**2 · If I Deleted This Line — pick any 3, predict *first*, then delete & run:**
- `history.append({'role': 'user', 'content': user_input})` — what does the AI now receive, and what happens to `input_tokens`?
- `history.append({'role': 'assistant', 'content': reply})` — what does the AI forget, and how does the token count grow differently?
- `print('History so far:', history)` — you lose visibility... but does the AI *behave* any differently? (Difference between debug output and logic.)

**3 · Bug Diary.** One bug, logged live — first guess, real cause, the gap.
