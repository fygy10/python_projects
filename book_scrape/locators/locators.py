from bs4 import BeautifulSoup

# extract from within specific book entries


class BookLocators:
    RATING = 'article.product_pod p.star-rating'
    TITLE = 'article.product_pod h3 a'
    PRICE = 'article.product_pod p.price_color'