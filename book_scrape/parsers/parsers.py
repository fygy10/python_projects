from locators.locators import BookLocators
import re
import logging

logger = logging.getLogger('scraping.book_parser')

class BookParser:     #parses a specific quote for author, quote text, and quote tags for each quote passed through it


    RATINGS = {

        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5

    }


    def __init__(self, parent):
        logger.debug('Parsing books')
        self.parent = parent       #'parent' is already a BS4 object

    def __repr__(self):
        return f'Book: {self.title}, costs ${self.price}, and has a rating of {self.rating} stars.'

    @property
    def title(self):
        locator = BookLocators.TITLE
        item =  self.parent.select_one(locator)
        item_name = item.attrs['title']    
        return item_name

    @property
    def rating(self):
        locator = BookLocators.RATING
        item =  self.parent.select_one(locator)
        classes = item.attrs['class']   #takes all value associated with the class of the rating
        rating = [r for r in classes if r != 'star_rating']     #filters out the non-rating class to return the rating
        rating_number = BookParser.RATINGS.get(rating[1])   #returns 'None' if not found; 
        return rating_number
    
    @property
    def price(self):
        locator = BookLocators.PRICE
        item = self.parent.select_one(locator).string
        expression = '([0-9,]+\.[0-9]+)'
        match = re.search(expression, item)
        return float(match.group(1))    #turns the string result into a float

