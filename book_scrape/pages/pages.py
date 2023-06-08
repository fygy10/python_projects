from bs4 import BeautifulSoup
import re
import logging

from locators.locators_page import BookPageLocators
from parsers.parsers import BookParser


#child logger for main logger
logger = logging.getLogger('scraping.book_page')


class BookPage:

    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup')
        self.soup = BeautifulSoup(page_content, 'html.parser')      #takes the html content and parses it using BeautifulSoup

    
    #parsed content move to this function which
    #collects the all books from the html using 'BookPageLocators.BOOK' and its specific html for the books and then
    #iterates over and passes each item found to 'BookParser'
    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(BookPageLocators.BOOK)]
    

    @property
    def page_count(self):
        content = self.soup.select_one(BookPageLocators.PAGER).string
        expression = 'Page [0-9]+ of ([0-9]+)'
        match = re.search(expression, content)
        pages = int(match.group(1)) #group '1' is the second set of bracker in regex after 'of'
        return pages
   
     