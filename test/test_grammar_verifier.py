from lib.grammar_verifier import verify_grammar

def test_returns_false_for_empty_string():
    result = verify_grammar("")

    assert result == False

def test_returns_false_for_invalid_input():
    result = verify_grammar(3)

    assert result == False

def test_returns_true_for_valid_string():
    result = verify_grammar("Hello world!")

    assert result == True

def test_returns_false_for_non_capital_letter():
    result = verify_grammar("hello world!")

    assert result == False

def test_returns_false_for_missing_punctuation():
    result = verify_grammar("Hello world")

    assert result == False

