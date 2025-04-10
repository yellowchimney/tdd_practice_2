from lib.diary_entry import DiaryEntry

def test_stores_title_and_contents():
    entry = DiaryEntry("How I spent summer", 
                       "It was fairly boring few weeks")
    
    assert entry.title == "How I spent summer"
    assert entry.contents == "It was fairly boring few weeks"

def test_returns_formated_string():
    entry = DiaryEntry("How I spent summer", 
                       "It was fairly boring few weeks")
    result = entry.format()

    assert isinstance(result, str)
    assert result == "How I Spent Summer: It was fairly boring few weeks"

def test_count_words_returns_correct_number_and_format():
    entry = DiaryEntry("How I spent summer?", 
                       "It was fairly boring few weeks!")
    result = entry.count_words()

    assert isinstance(result, int)
    assert result == 10

def test_returns_correct_min_estimation():
    with open("300_words_about_gardens.txt", mode="r") as f:
        text = f.read()
    entry = DiaryEntry("How I spent summer", 
                       text)
    result = entry.reading_time(200)

    assert result == 2

    result = entry.reading_time(100)

    assert result == 3

def test_returns_string_of_appropriate_length():
    with open("300_words_about_gardens.txt", mode="r") as f:
        text = f.read()
    entry = DiaryEntry("How I spent summer", 
                       text)
    # entry.format()
    chunk = entry.reading_chunk(100,1)
    words = len(chunk.split())
    assert words == 100
    assert chunk == (
        "How I Spent Summer: An English garden, often referred to as an English landscape garden, is a classic "
        "and timeless style of gardening that emphasizes natural beauty, peacefulness, and "
        "a gentle sense of romanticism. This style first emerged in 18th-century Britain "
        "as a response to the rigid, formal, and highly symmetrical designs of European "
        "gardens—especially those seen in France and Italy. Unlike their structured "
        "counterparts, English gardens were meant to reflect a more organic, relaxed, "
        "and emotionally evocative version of nature. "
        "These gardens are defined by rolling green lawns, gently curving gravel or stone "
        "paths, and irregularly shaped flower beds."
    )

def test_returns_consequent_string_parts_when_called_multiple_times():
    entry = DiaryEntry("How I spent summer?", 
                   "It was fairly boring few weeks!")
    chunk1 = entry.reading_chunk(2,1)
    chunk2 = entry.reading_chunk(2,1)
    chunk3 = entry.reading_chunk(2,1)
    assert chunk1 == "How I"
    assert chunk2 == "Spent Summer?:"
    assert chunk3 == "It was"