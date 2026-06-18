# 0.4 — Build a Frontend UI with Bolt.new

> **📌 This is the start of Mini Project 2.**
> From this session onwards, you will be working in pairs (or groups of 3 if needed). You and your partner will build one shared app together. All Bolt work across Sessions 4, 5, and 6 contributes to your Mini Project 2 submission.
>
> Choose your partner now and decide together: what will your shared agent do?

## Objective

By the end of this lab, your AI agent will have a real web interface — built by describing what you want, not by writing HTML or CSS.

You will use Bolt.new to generate the frontend, connect it to your agent logic, and customize it to match your agent's identity.

All work in Bolt is done by **prompting** — you describe what you want, Bolt builds it.

---

## Lab Steps

### Step 1: Prepare — Export your agent as a starting point

- Open your `app.py` from Session 3.
- Copy out the core logic: your `system_message`, the `history` structure, and the `client.messages.create()` call.
- You will use this to describe your app to Bolt.

### Step 2: Build — Generate the UI with Bolt.new

- Open [bolt.new](https://bolt.new) in your browser.
- In the prompt box, describe your app using the template in the starter code below.
- Press Enter and wait ~30 seconds for Bolt to generate your app.
- Click the preview button — you should see a working chat interface.
- Test it: type a message and confirm it matches your agent's personality.

### Step 3: Connect — Add your API key and go live

- In the Bolt editor, find the `.env` file or the environment variables section.
- Add your Anthropic API key:
  ```
  ANTHROPIC_API_KEY=your-key-here
  ```
- Click the reload button in the preview panel.
- Test your app end-to-end: it should respond using your exact system prompt.
- Click **Deploy** in Bolt — you now have a public URL.

---

## Starter Prompt

```
Build a clean chat web app with the following:

- A chat interface where the user types messages and the AI responds
- The AI is powered by the Anthropic Claude API (claude-3-haiku-20240307)
- Use this exact system prompt for the AI:
  [PASTE YOUR SYSTEM PROMPT HERE]
- Keep a conversation history so the AI remembers earlier messages
- The UI should have:
  - A title at the top: [YOUR AGENT NAME]
  - A subtitle: [ONE SENTENCE DESCRIBING WHAT IT DOES]
  - A text input at the bottom with a Send button
  - The conversation displayed as a chat thread
- Use a clean modern design with a dark or light theme (your choice)
- Load the API key from an environment variable called ANTHROPIC_API_KEY
```

---

## Expected Output

```
[Bolt generates a working web app in ~30 seconds]
[Preview shows a chat interface with your agent's name]

User: Hello
Agent: [Responds in character based on your system prompt]

Public URL: https://your-app.bolt.host
```

---

## Bonus Challenges

🟡 **Bonus 1**
- Prompt Bolt to add a **New Chat** button that clears the conversation history.
- Try: `"Add a clear/reset button that starts a new conversation."`

🟠 **Bonus 2**
- Add a second AI mode with a different system prompt and persona.
- Prompt Bolt: `"Add a toggle that switches between [Agent A] and [Agent B] mode. Each uses a completely different system prompt."`

🔴 **Bonus 3**
- Look at the code Bolt generated. Find where the API call is made.
- Compare it to your original `app.py`. Write down 3 differences and 3 similarities.
- This trains you to read and understand AI-generated code — a critical real-world skill.
