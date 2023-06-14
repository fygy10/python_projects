from bs4 import BeautifulSoup
from locators.quote_locator_page import QuotePageLocators
from parsers.quote_scraper import QuoteParser


class QuotePage:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')      #takes the html content and parses it

    
    #parsed content move to this function which
    #collects the all quotes from the html using 'QuotePageLocators.QUOTE' and then
    #passes them to the parser 'QuoteParser'
    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags] 