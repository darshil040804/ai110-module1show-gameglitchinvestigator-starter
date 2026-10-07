# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  
- If input was higher than secret number, the hint was to go higher and if input was lower than secret number, the hint was to go lower. However, it should have been the exact opposite. 
- After completing one game, when I clicked new game, a new secret number was loaded, but the submit guess button did not let me submit any new guesses
- Every difficulty level had a range for example 1-20, 1-50, etc. But the instructions always asked to guess something between 1-100. 
- Later I found more: the secret could be outside the selected range after I changed difficulty, the hint flipped between Higher and Lower on every second guess, and "attempts left" lagged one guess behind so the game ended one guess early.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code location
|-------|-------------------|-----------------|------------------------|-----|
| guessed 60| go higher | go lower |go higher hint was displayed | app.py |
| clicked new game| new game to start|new secret number loaded but unable to submit new guesses |Game over. Start a new game to try again. | app.py |
| selected difficulty: hard|range to change to 1-50 |range remained 1-100 | no change in output | app.py|

---

## 2. How did you use AI as a teammate?

- **Tool used:** Claude Code (agent mode) inside VS Code.
- **A correct suggestion:** I reported that the Higher/Lower hint kept flipping when I guessed 5 against a secret of 14. Claude found that `app.py` converted the secret to a string on every even attempt (`str(st.session_state.secret)`), so `check_guess` compared strings, and `"5" > "14"` is true because `"5"` sorts after `"1"`. It suggested removing the cast. That was correct because the flip lined up exactly with the even-numbered attempts. I verified it by guessing 5 against a secret of 14 several times in a row, and the hint stayed "Go HIGHER!" every time.
- **A suggestion I did not accept as written:** When I said the first guess seemed to do nothing, Claude's explanation was that pressing Enter in a bare `st.text_input` reruns the page without a Submit click, so it moved the input and button into an `st.form`. I treated that as a hypothesis, not a confirmed fix, because it could not reproduce the problem in a headless test, which clicks the button directly and never exercises the Enter key. The form is a reasonable change, but I did not accept the explanation as proven. I checked it by running the app headlessly (attempts left went 8 to 7 to 6 after each guess) and then trying both Enter and the button in the browser.

---

## 3. Debugging and testing your fixes

- **How I decided a bug was fixed:** I re-ran the exact steps that triggered it and compared against what I expected, then backed it with a pytest case where the logic could be tested on its own.
- **pytest:** I ran `python -m pytest -v` and got `8 passed`. That covers the 3 starter tests (`test_winning_guess`, `test_guess_too_high`, `test_guess_too_low`) and 5 new tests for `get_range_for_difficulty` (Easy 1-20, Normal 1-100, Hard 1-50, unknown difficulty falls back to 1-100, and low is always below high). The three starter tests were failing at first because `check_guess` returns an `(outcome, message)` tuple and the tests compared it to a plain string. The tests were wrong, not the code, so I updated them to unpack the tuple.
- **Manual / headless checks:**
  - Switching difficulty 60 times in a row always gave a secret inside the selected range.
  - Guessing 5 against a secret of 14 gave "Go HIGHER!" every time, with no more flipping.
  - "Attempts left" now counts down 8, 7, 6 ... 0 on Normal, and the game ends on the 8th guess instead of the 7th.
  - New Game resets the attempts back to 8.
- **Did AI help with tests:** Yes. I wrote the prompt describing the range bug and Claude generated the five range tests, then ran pytest and explained why the three starter tests failed. It also drove the app with Streamlit's `AppTest` so I could check the secret, hints and attempts without clicking through the game by hand.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you click a button or type in a box, Streamlit re-runs the whole script from top to bottom, so ordinary variables are reset each time. `st.session_state` is the one place that survives those reruns, so the secret number, attempts, score and status live there. That caused two of my bugs. The secret was only created the first time, so it never changed when I switched difficulty and could be out of range. The attempts counter was shown before the click was handled, so it displayed the value from the previous rerun.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I want to reuse writing a small pytest case for each bug and re-running the exact steps that triggered it, because that is how I knew a fix really worked. Next time I would describe the symptom precisely (what I typed, what I saw) instead of a vague summary, and I would check the AI's explanation against the code before accepting it. This project made me treat AI-generated code as a draft that can look finished and still be wrong, so I review it and test it myself.
