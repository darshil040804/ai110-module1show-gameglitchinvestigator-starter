# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  
- If input was higher than secret number, the hint was to go higher and if input was lower than secret number, the hint was to go lower. However, it should have been the exact opposite. 
- After completing one game, when I clicked new game, a new secret number was loaded, but the submit guess button did not let me submit any new guesses
- Every difficulty level had a range for example 1-20, 1-50, etc. But the instructions always asked to guess something between 1-100. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code location
|-------|-------------------|-----------------|------------------------|-----|
| guessed 60| go higher | go lower |go higher hint was displayed | app.py |
| clicked new game| new game to start|new secret number loaded but unable to submit new guesses |Game over. Start a new game to try again. | app.py |
| selected difficulty: hard|range to change to 1-50 |range remained 1-100 | no change in output | app.py|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
