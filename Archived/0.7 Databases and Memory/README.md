# 0.7 — Add Persistent Memory

> **📌 Introduction to the Final Group Project.**
> In this session, you will meet your final project team (groups of 4). By the end of Session 9, your team will have built and deployed a multi-agent AI app — one agent per team member, each with a different purpose, all in one polished Bolt app.
>
> Today's lab introduces the memory problem and two solutions. The decisions you make here will directly shape your final project architecture.

## Objective

By the end of this lab, you will understand why your app forgets everything when it restarts, how to save conversation history to a local JSON file, and how Supabase provides a cloud database for deployed apps with real users.

---

## Lab Steps

### Step 1: See the problem — Why does memory disappear?

- Run your `app.py` from Session 3. Have a 5-message conversation. Close the terminal.
- Restart the app. The AI has forgotten everything.
- Write down: Where does the `history` variable live? What happens to it when Python stops?
- This is called **in-memory state** — it only exists while the program is running.

### Step 2: Solution 1 — Save to a JSON file (local Python)

- In your `agent` folder, create a new file called `memory.py`.
- Paste the starter code below.
- Update your `app.py` to call `load_history()` at the start and `save_history(history)` after each turn.
- Restart the app — your conversation history should still be there.

### Step 3: Solution 2 — Explore Supabase in your Bolt app

- Open your Bolt app from Session 5 or 6.
- Prompt Bolt:
  ```
  Add Supabase persistence to this app.
  Save every message to a Supabase messages table.
  Use the SUPABASE_URL and SUPABASE_ANON_KEY environment variables.
  Each row should store: user_id, role, content, and a timestamp.
  Load the last 20 messages for the current user when the app starts.
  ```
- Open your Supabase dashboard. Find the table Bolt created.
- Watch the rows appear in real time as you chat.

### Step 4: Connect to your final project

As a team, discuss and write down:
- What data will your final project need to save?
- Will you use JSON (simple, local) or Supabase (cloud, multi-user)?
- How many tables might you need?

You will use these answers in the Session 8 planning lab.

---

## Starter Code

```python
# memory.py — save and load conversation history as a JSON file

import json
import os

HISTORY_FILE = 'history.json'

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)        # write list to file

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []                    # first run: no file yet
    with open(HISTORY_FILE, 'r') as f:
        return json.load(f)          # read list from file

# ─── How to use it in app.py ────────────────────────────
# history = load_history()           # load at start
# ... chat loop ...
# save_history(history)              # save after every turn
```

```
# Bolt prompt — add Supabase persistence:

Add Supabase persistence to this app.
Save every message to a Supabase messages table.
Use the SUPABASE_URL and SUPABASE_ANON_KEY environment variables.
Each row should have: user_id, role, content, timestamp.
Load the last 20 messages for the current user when the app starts.
```

---

## Expected Output

```
# First run:
>> Tell me your name.
Agent: My name is Alex, your study assistant.

# Close the app. Restart.

# Second run — history loaded from JSON:
>> What did we talk about last time?
Agent: Last time you asked me my name — I'm Alex, your study assistant.
```

---

## Bonus Challenges

🟡 **Bonus 1**
- Add a `/history` command in your Python app that prints the last 5 saved messages in a readable format.

🟠 **Bonus 2**
- Add session support: at the start, ask the user for a session name (e.g. `"study-session-1"`).
- Save and load history per session so different sessions have separate histories.

🔴 **Bonus 3**
- In your Supabase dashboard, try to write a query that filters messages by date.
- Can you retrieve only today's messages? What about messages from a specific user?
- Write down what you had to figure out to make this work.
