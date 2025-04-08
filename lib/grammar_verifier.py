def verify_grammar(text):
    if not isinstance(text, str):
        return False
    
    valid_puctuation = ('.', '!', '?')
    if text and text[0].isupper() and text.endswith(valid_puctuation):
        return True
    else:
        return False

# My function should take a string and return true if the
# string starts with a capital letter and ends with a 
# punctuation mark and  false in all other cases.
# So my test cases should include:
# valid string with capital letter at [0] and puctuation mark at the end.
# string that starts with CL, but doesn't end with a valid punctuation mark
# string that has a punctuation mark at the end but doesn't start
# with capital letter
# a string that doesn't meet any of these conditions
# potentially a completely invalid input (empty, numeric, list)