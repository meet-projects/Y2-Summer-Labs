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
