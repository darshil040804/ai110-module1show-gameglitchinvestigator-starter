# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** A Streamlit number-guessing game. You pick a difficulty, guess the secret number within a limited number of attempts, and get Higher/Lower hints and a score.

**Bugs I found:**
- The Higher/Lower hints were wrong and, later, flipped on every second guess.
- The info text always said "between 1 and 100", even on Easy (1-20) and Hard (1-50).
- The secret number could fall outside the selected difficulty range after switching difficulty.
- "Attempts left" was one guess behind, and the game ended one guess early.
- The first guess sometimes seemed to do nothing.

**Fixes I applied (with Claude Code):**
- Moved `get_range_for_difficulty` into `logic_utils.py` as the single source of truth and showed `low`/`high` in the info text.
- Regenerated the secret and reset the game whenever the difficulty changes.
- Removed the `str()` cast on the secret that made `check_guess` compare strings.
- Started attempts at 0 and updated "attempts left" after each guess is processed.
- Moved the guess input into a form so Enter and the button both submit, and made difficulty a plain dropdown.
- Updated the three starter tests to unpack the `(outcome, message)` tuple and added five range tests.

## 📸 Demo Walkthrough

A sample game on **Normal** (range 1-100, 8 attempts), with the secret number at 14. The values below come from running the game.

1. The game loads: "Guess a number between 1 and 100. Attempts left: 8", score 0.
2. You enter **40**. The game says "Go LOWER!", attempts left 7, score -5.
3. You enter **5**. The game says "Go HIGHER!", attempts left 6, score -10.
4. You enter **25**. The game says "Go LOWER!", attempts left 5, score -15.
5. You enter **14**. The game says "Correct!", shows "You won! The secret was 14. Final score: 35", and the status becomes won.
6. Submitting again shows "You already won. Start a new game to play again."
7. Switching the difficulty to **Easy** starts a fresh game: "Guess a number between 1 and 20. Attempts left: 6", and the secret is picked from 1-20. The score is kept from the earlier game.

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
collected 8 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 12%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 25%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 37%]
tests/test_game_logic.py::test_range_easy PASSED                         [ 50%]
tests/test_game_logic.py::test_range_normal PASSED                       [ 62%]
tests/test_game_logic.py::test_range_hard PASSED                         [ 75%]
tests/test_game_logic.py::test_range_unknown_difficulty_defaults PASSED  [ 87%]
tests/test_game_logic.py::test_range_is_valid_for_all_difficulties PASSED [100%]

============================== 8 passed in 0.04s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
