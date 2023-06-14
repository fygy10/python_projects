from bs4 import BeautifulSoup

# extract from within specific quotes


class QuoteLocators:
    AUTHOR = 'small.author'
    TEXT = 'span.text'
    TAGS = 'div.tags a.tag' 