# 0.9 — Deploy Your App to the Internet

## Objective

By the end of this lab, your team's final project app will be live on the internet with a public URL, fully functional, and ready to present at the Session 10 showcase.

All deployment is done through **Bolt's native deploy function**.

---

## Lab Steps

### Step 1: Build — Assemble your final app in Bolt

- Open a new Bolt project (or continue from your Session 5/6 app if your team is building on it).
- Prompt Bolt to build the full multi-agent app using the template below.
- Work through each agent tab one at a time. Test each one before moving to the next.

### Step 2: Polish — Work through the launch checklist

Go through this checklist as a team. Prompt Bolt to fix anything that isn't working.

- [ ] All four agents respond correctly in character
- [ ] Switching tabs does not mix up conversation histories
- [ ] Loading indicator appears while the AI is thinking
- [ ] Error handling works (test by temporarily removing the API key)
- [ ] App name and team name are visible in the header
- [ ] Design is clean and consistent across all tabs
- [ ] No placeholder text or unfinished UI elements visible

### Step 3: Deploy — Go live

- In Bolt, add your `ANTHROPIC_API_KEY` to the environment variables section.
- Click **Deploy**.
- Copy your public URL and share it with your instructor.
- Test the live URL — does everything work the same as in preview?

### Step 4: Prepare for the showcase

Each team member should be able to answer:

1. What does your agent do, and why did you design it that way?
2. What was the biggest challenge, and how did you solve it?
3. What would you add if you had more time?

Practice your demo: open the live URL and walk through each agent out loud.

---

## Starter Prompt

```
Build a clean multi-agent web app with 4 tabs.
Each tab is a separate AI agent with its own system prompt and conversation history.

Tab 1 — [AGENT NAME]:
System prompt: [PASTE HERE]

Tab 2 — [AGENT NAME]:
System prompt: [PASTE HERE]

Tab 3 — [AGENT NAME]:
System prompt: [PASTE HERE]

Tab 4 — [AGENT NAME]:
System prompt: [PASTE HERE]

The app should:
- Load the API key from an environment variable: ANTHROPIC_API_KEY
- Have a clean, modern design
- Show a loading indicator while the AI is responding
- Handle API errors gracefully with a friendly message
- Display the app name and team name in the header
```

---

## Expected Output

```
[App is live at a public Bolt URL]
[All four agent tabs respond correctly in character]
[Switching tabs preserves each conversation separately]
[Design is clean and polished]
[Team name and app name are visible in the header]
[API key is not visible anywhere in the public interface]
```

---

## Bonus Challenges

🟡 **Bonus 1**
- Prompt Bolt to add a landing page: a brief intro screen that explains what the app does before the user starts chatting.

🟠 **Bonus 2**
- Prompt Bolt to add Supabase persistence so conversations are saved across sessions.
- Test it: close the app, reopen it, and confirm the history is still there.

🔴 **Bonus 3**
- Prompt Bolt to add a usage dashboard: a small panel that shows how many messages each agent has received.
- Use it to find out which agent users engage with most.
