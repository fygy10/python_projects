from bs4 import BeautifulSoup

# extract books from a page


class BookPageLocators:
    BOOK = 'div.page_inner section li.col-xs-6'
    PAGER = 'div.page_inner section ul.pager li.current'