from locators.quote_locator import QuoteLocators

class QuoteParser:     #parses a specific quote for author, quote text, and quote tags for each quote passed through it

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Quote: {self.quote} by {self.author}'

    @property
    def quote(self):
        locator = QuoteLocators.TEXT
        return self.parent.select_one(locator).string   #search parent for the 

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string  

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return self.parent.select_one(locator).string 
