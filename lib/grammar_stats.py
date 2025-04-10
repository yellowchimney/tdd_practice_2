class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.valid_texts = 0

    def check(self, text):
        if not isinstance(text, str):
            return False
    
        valid_puctuation = ('.', '!', '?')
        if text and text[0].isupper() and text.endswith(valid_puctuation):
            self.total_texts += 1
            self.valid_texts += 1
            return True
        else:
            self.total_texts += 1
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass