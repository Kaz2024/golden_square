class GrammarStats:
    def __init__(self):
        self.total_text = 0
        self.good_text = 0

    def check(self, text):
        self.total_text += 1
        if text[0].isupper() and text[-1] in ".,!":
            self.good_text += 1 
            return True 
        return False 

    def percentage_good(self):
        if self.total_text == 0:
            return 0
        return (self.good_text/self.total_text) * 100
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass
