from lib.grammar_stats import GrammarStats

def test_returns_true_for_valid_texts():
    stats = GrammarStats()
    result = stats.check("Some lovely text!")

    assert result == True

def test_returns_false_for_invalid_texts():
    stats = GrammarStats()
    result = stats.check("some creepy text")

    assert result == False

def test_saves_number_of_texts_checked():
    stats = GrammarStats()
    stats.check("some creepy text")
    assert stats.total_texts == 1


def test_saves_number_of_texts_passed():
    stats = GrammarStats()
    stats.check("some creepy text")

    assert stats.total_texts == 1
    assert stats.valid_texts == 0

    stats.check("Some lovely text!")

    assert stats.total_texts == 2
    assert stats.valid_texts == 1

def test_percentage_returns_percentage_of_valid_texts():
    stats = GrammarStats()
    stats.check("some creepy text")
    stats.check("Some lovely text!")
    result = stats.percentage_good()

    assert result == "50%"
