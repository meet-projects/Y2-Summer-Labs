# Code Commenting & Reflection Guide

*Read once. You'll use it in every lab. It takes the mystery out of two questions:
what should I comment, and what am I supposed to reflect on.*

---

## Part 1 — Code Commenting Guidelines

*Original guidelines, preserved as written by the team.*

As you complete each lab, add a small number of comments that demonstrate your
understanding of the code. **Your goal is *not* to comment on every line.** Instead,
explain the purpose of the important parts of your program.

**What to comment**

1. **Setup & Initialization** — what's being prepared before the program runs.
   `# Set up everything the program needs before it can begin`
2. **Important Variables** — the ones that carry the program.
   `# Stores information that will be used throughout the program`
3. **Main Logic** — the top of a loop, function, or major block.
   `# Repeatedly perform the main task until the stopping condition is reached`
4. **External Operations** — anything talking outside the program (API, file, database).
   `# Send data to an external service and receive a response`
5. **New Features You Add** — one comment on the purpose of each feature.
   `# Allow the user to restart this feature without restarting the program`

**What *not* to comment** — anything that just re-reads the code out loud.
Explain *why a part exists*, not *what each line does*. Skip comments like
`# Increase x by 1` or `# Print the result` — the code already says that.

**Rule of thumb.** Before a major section, ask: *"If someone else read this code, would
this comment help them understand the purpose of this section?"* If yes — write it. If
you're just narrating syntax — skip it.

**Expected amount.** ~**5–10 meaningful comments** per lab. Quality over quantity.
*(Yes, that range contains a 6 and a 7. Get the "six-seven" out of your system now.
That's the only one you get. 🫱🫲 Moving on.)*

<details>
<summary><b>Example — Morse Code Translator (click to expand)</b></summary>

```python
# Store every supported character that can be translated to Morse code
alphabet = ['A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z',' ']

# Store the Morse code equivalent for each character in the same position
morse_code = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---',
              '-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-',
              '..-','...-','.--','-..-','-.--','--..',' ']

# Build the letter-to-Morse lookup table
dictionary_morse = {}
for i in range(len(alphabet)):
    dictionary_morse[alphabet[i]] = morse_code[i]

# Get a sentence from the user and convert it to uppercase
sentence = input("Please write your sentence here: ").upper()

# Store the translated Morse code as it is being built
sentence_morse = ""

# Translate the sentence one character at a time
for character in sentence:
    if character == " ":
        sentence_morse += " / "
    elif character in dictionary_morse:
        sentence_morse += dictionary_morse[character] + " "

# Display the completed Morse code translation
print(sentence_morse)
```
</details>

---

## Part 2 — The Three Reflections

**AI can write your comments. It can explain concepts. It cannot give you *your* analogy.**
It doesn't know what you predicted before you ran the code. It has never seen your
specific bug. Do these three honestly — they map what's actually in your head.

> *Cheating yourself here is like watching the highlights and saying you watched the
> game. You know the score. You missed the game.*

### 1 · Personal Analogy — *~3 min · written · solo*
When you can explain a concept in your own words, using something you already understand
deeply, you've actually encoded it. A memorized definition just proves you can repeat.
**Generic analogies are banned** — "it's like a library" is a skill issue. It has to
reference something *you* care about (football, music, food, cars, games). If an AI could
have generated it, it doesn't count.

### 2 · Bug Diary — *fill in DURING the lab, not after*
The gap between what you **thought** was wrong and what was **actually** wrong is where
debugging skill lives. Guessed right the first time? That's pattern-matching luck, not
debugging. The moment you hit a bug — *before you fix it* — take 60 seconds to write your
first guess. Then fix it. Then note what was really wrong. **The gap is the entry.**
*Counts as a bug:* an error, wrong output, a loop that won't stop, the AI replying
weirdly — anything you had to fix. *Zero bugs today? Take the line you were least sure
about when you wrote it: what did you think it did vs. what does it actually do?*

### 3 · If I Deleted This Line — *~5 min · predict first, then test*
If you can predict what breaks when you remove a line, you have a real mental model. If
you can't, you don't — even if the code runs. **The protocol, in order:**
1. Pick a line. Write your prediction **before touching anything.**
2. Be specific. "It'll crash" isn't specific. "It'll crash with a `KeyError` because the
   key doesn't exist yet" is.
3. Delete the line. Run it.
4. Write what actually happened.
5. Compare. If there's a gap — that gap is the lesson.

> **No Neymar predictions.** Write what you *actually* think will happen, not what sounds
> impressive. An honest wrong guess teaches more than a confident right one you
> reverse-engineered from the answer.

*The exact concept, prompt, and lines to try are printed at the end of each lab.*
