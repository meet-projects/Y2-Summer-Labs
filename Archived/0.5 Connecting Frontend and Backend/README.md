# 0.5 — Customize & Extend Your Bolt App

## Objective

By the end of this lab, you will understand the structure of the app Bolt generated, make meaningful improvements through prompting, and add a second AI agent as a separate tab — building toward the multi-agent structure of your final group project.

All work in this lab is done by **prompting Bolt** — no manual code editing.

---

## Lab Steps

### Step 1: Understand — Read the code Bolt wrote

- Open your Bolt project from Session 4.
- Find the file where the API call happens. Read it carefully.
- Answer these questions in writing:
  - Where is the system prompt stored?
  - Where is the conversation history stored?
  - What happens when the user presses Send?
  - What gets sent to the API?

### Step 2: Improve — Upgrade the app through prompting

Ask Bolt to make these improvements **one at a time**. Test after each one before moving to the next.

1. `"Add a loading indicator while the AI is responding."`
2. `"Add a message count that shows how many messages have been sent."`
3. `"Add a friendly error message if the API call fails, instead of crashing."`

### Step 3: Extend — Add a second agent tab

- Design a second AI agent that does something different from your first.
- Write a system prompt for it.
- Prompt Bolt:
  ```
  Add a second tab called [NAME] that uses this system prompt:
  [YOUR PROMPT]
  It should have its own separate conversation history from the first tab.
  ```
- Test both tabs. Make sure switching tabs doesn't mix up the conversations.

---

## Starter Prompts

```
# Add a second agent tab:
Add a second tab to the app called '[AGENT NAME]'.
This tab should:
- Have its own chat interface
- Use this system prompt: [PASTE YOUR NEW SYSTEM PROMPT HERE]
- Have completely separate conversation history from the first tab
- Have a different color accent or visual style to make it distinct

# Add error handling:
Update the app to handle API errors gracefully.
If the API call fails for any reason, show a friendly message in the chat:
'Something went wrong. Please try again.'
Do not show a stack trace or crash the app.

# Add a loading indicator:
While the AI is generating a response, show a loading animation
in the chat (e.g., three animated dots or a spinner).
Hide the loading indicator once the response arrives.
```

---

## Expected Output

```
[App has two tabs — each with its own agent and conversation history]
Tab 1: [Your Session 3 agent]
Tab 2: [Your new agent]

[Switching tabs preserves each conversation separately]
[A loading indicator appears while the AI is thinking]
[If the API fails, a friendly error message appears in the chat]
```

---

## Bonus Challenges

🟡 **Bonus 1**
- Prompt Bolt to add a **copy** button next to each AI message.
- Try: `"Add a small copy icon next to each assistant message. Clicking it copies the message text to the clipboard."`

🟠 **Bonus 2**
- Add a conversation export feature: a button that downloads the full chat as a `.txt` file.
- Prompt Bolt to implement this, then read the generated code — how does a browser file download actually work?

🔴 **Bonus 3**
- Try to intentionally break the app by asking Bolt to add a feature that conflicts with existing logic.
- Document what broke and why. Then fix it.
- This is real debugging practice: AI-generated code is not always right, and knowing how to debug it is the skill.
