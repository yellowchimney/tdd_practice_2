from lib.string_snippet import make_snippet

def test_returns_string():
    result = make_snippet("hello")

    assert isinstance(result, str)

def test_returns_full_string_for_string_shorter_than_5_words():
    string = "hello wild world"
    result = make_snippet(string)

    assert result == string

def test_returns_first_5_words():
    string = "In this project you will build a personal diary system. "
    "You'll start by writing a couple of functions that will be useful later on."
    result = make_snippet(string)
    split_into_words = result.split()

    assert result == "In this project you will"
    assert len(split_into_words) == 5