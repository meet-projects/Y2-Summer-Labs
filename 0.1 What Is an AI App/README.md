> ### Read this before you write a single line of code.
>
> Here's the thing nobody says out loud: this summer, an AI could finish most of these
> labs for you in about thirty seconds. You could paste every prompt, submit every
> `app.py`, and "complete" the course having learned almost nothing. The labs would be
> green. Your brain would be untouched.
>
> So let's be honest with each other. **These labs are not the point. What happens in
> your head while you build them is the point.**
>
> Getting code to run is now the easy part — the model does that. The rare, valuable
> skill is *understanding what you built*: knowing why it works, predicting what breaks,
> and catching the AI when it's wrong. That's the difference between a builder and a
> person who pastes.
>
> That's why every lab ends with a short reflection — an analogy, a bug diary, a "what
> breaks if I delete this line." Ten minutes. An AI **can't** do them for you, because
> they run on *your* experience, not the internet's. Do them honestly and you leave this
> summer genuinely dangerous. Skip them and you'll have a folder full of code you can't
> explain in an interview.
>
> Watching match highlights isn't the same as playing the game. You'd know the score.
> You'd have missed everything that mattered.
>
> Let's build. 🛠️
>
> ↳ Full reflection + commenting guide: [`REFLECTION-GUIDE.md`](../REFLECTION-GUIDE.md)


<br>

# 0.1 — Run Your First AI App

## Objective

By the end of this lab, you will have run a working AI chatbot in your terminal, made it respond to you, and changed its personality by editing the system prompt.

This is the moment it clicks: an AI application is just Python code that sends a message to a model over the internet and gets one back.

---

## Lab Steps

### Step 0: Folder Setup

- Create a new folder on your desktop called `agent`.
- Open it in VS Code — this is where you will be working all summer. Every new file you create will live here.

### Step 1: Setup — Get the base code running

- Create a new file called `app.py` and paste in the starter code below.
- Create a file called `.env` in the same folder and add your API key:
  ```
  ANTHROPIC_API_KEY=your-key-here
  ```
- In your terminal, install the required packages:
  ```
  pip install anthropic python-dotenv
  ```
- Run the app:
  ```
  python app.py
  ```
- Type a message and press Enter. You should see a response from the AI.
- Type `exit` to stop the app.

### Step 2: Explore — Talk to your agent

- Try at least 5 different messages. Notice how the AI stays in character.
- Ask it something helpful — does it actually help you? Why or why not?
- Ask it something vague or unclear. What happens?
- Write down: What is different about this compared to using ChatGPT directly?

### Step 3: Change — Edit the system prompt

- Find the `system_message` variable in the code.
- Change the name and personality completely. Make it a helpful tutor, a formal assistant, a motivational coach — your choice.
- Save and re-run the app. Test the new personality.
- Change it one more time. Try something creative.

---

## Starter Code

```python
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Alex. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-3-haiku-20240307',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
```

---

## Expected Output

```
>> Hello
Claude: Hi there! How can I help you today?

>> Can you help me study?
Claude: Of course! I'd love to help you study. What subject or topic would you like to work on?
```

---

## Bonus Challenges

🟡 **Bonus 1**
- Add a print statement that shows how many messages have been sent so far.
- Format it like this: `[Turn 3] You: ...`
- Hint: use `len(history)`.

🟠 **Bonus 2**
- Add a command word `reset` that clears the conversation history and starts fresh — without restarting the program.
- Print a message when the history is cleared.

🔴 **Bonus 3**
- Let the user choose the AI's personality at the start of the program.
- Before the chat loop, ask: `"What personality should the AI have?"`
- Use their answer as the `system_message`.


<br>

## 🧠 Reflection — Lab 0.1

*~10 min at the end of lab. Solo and honest. See [`REFLECTION-GUIDE.md`](../REFLECTION-GUIDE.md) for the why.*

**1 · Personal Analogy — conversation memory.**
Your agent has no memory of its own. Every turn, your code hands it the *entire*
conversation again from scratch (`history`). Explain that using something you actually
care about: **where in your world does something only work if you carry the whole
backstory with you, every single time?** (Banned: "it's like a diary." Too easy — make
it yours. 2–4 sentences.)

**2 · If I Deleted This Line — pick any 3, predict *first*, then delete & run:**
- `history.append({'role': 'assistant', 'content': reply})` — what changes about what the AI remembers?
- `load_dotenv()` — does the program even start? Why?
- `temperature=0.7` — does *anything visible* change? (Not every line is load-bearing — that's a real lesson.)
- the `break` inside `if user_input.lower() == 'exit':` — what happens when you try to quit?

**3 · Bug Diary.** Log one bug from today the moment it happened — first guess vs. what was
really wrong, and the gap. (Nothing broke? Take the line you were least sure about.)
