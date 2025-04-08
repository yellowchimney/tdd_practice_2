from lib.word_counter import count_words

def test_returns_int():
    result = count_words("hello")

    assert isinstance(result, int)

def test_returns_zero_for_empty_string():
    result = count_words("")

    assert result == 0

def test_returns_one_for_one_word_string():
    result = count_words("hello")

    assert result == 1

def test_returns_correct_number_of_words():
    result = count_words("hello wild world")

    assert result == 3

    result = count_words("In this project you will build a personal diary system.")

    assert result == 10