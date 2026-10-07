from logic_utils import check_guess, get_range_for_difficulty

# FIX: Claude updated these three starter tests to unpack the (outcome, message) tuple that
# check_guess returns; I reviewed the failing output and approved the change.
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# FIX: Range tests below were written by Claude from a prompt I wrote, to cover the range-mismatch bug.
def test_range_easy():
    # Easy should be 1 to 20
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    # Normal should be 1 to 100
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    # Hard should be 1 to 50
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_range_unknown_difficulty_defaults():
    # An unknown difficulty should fall back to 1 to 100
    assert get_range_for_difficulty("Impossible") == (1, 100)

def test_range_is_valid_for_all_difficulties():
    # low must always be less than high
    for difficulty in ["Easy", "Normal", "Hard", "Unknown"]:
        low, high = get_range_for_difficulty(difficulty)
        assert low < high
