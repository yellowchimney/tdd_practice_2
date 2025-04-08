def calculate_reading_time(text):
    if len(text) == 0:
        return f"This text will take 0 minute(s) to read"

    else:    
        list_of_words = text.split()
        minutes = len(list_of_words)//200
        seconds = int(((len(list_of_words)/200) *60) % 60)
        if minutes and seconds:
            reading_time = f"{minutes} minute(s) and {seconds} second(s)"
        elif minutes and not seconds:
            reading_time = f"{minutes} minute(s)"
        else:
            reading_time = f"{seconds} second(s)"
        
    return f"This text will take {reading_time} to read"
        
    


# I need to break the text into words 
# and divide the number by 200 to get number of minutes
# I need to think in what format I want to return 
# the result. The easiest option is int representing
# the number of minutes. I can also return number of seconds,
# a float in minutes, a string with number of minutes and seconds
# The easiest argument I can think about is an empty string 
# and it should return 0. Then I can give strings of different
# lengths and check the outputs. 
# Although, thinking about it, string might not be the best format
# of the argument if we're talking about 5 minutes worth of text.
# Maybe, I should instead take a file and read the contents.
# That raises the question if file-reading behaviour should be 
# a part of this function, as it is unlikely I can test it 
# within the same function. Can I instead put a file contents
# as an argument in a test?