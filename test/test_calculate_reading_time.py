from lib.calculate_reading_time import calculate_reading_time

def test_returns_zero_for_empty_string():
    result = calculate_reading_time("")

    assert result == "This text will take 0 minute(s) to read"

def test_returns_correct_number_for_full_minutes_text():
    with open("200_words_about_roses.txt", mode="r") as f:
        text = f.read()

    result = calculate_reading_time(text)

    assert result == "This text will take 1 minute(s) to read"

def test_returns_minutes_and_seconds():
    with open("300_words_about_gardens.txt", mode="r") as f:
        text = f.read()

    result = calculate_reading_time(text)

    assert result == "This text will take 1 minute(s) and 26 second(s) to read"