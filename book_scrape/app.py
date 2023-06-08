import requests
import logging

from pages.pages import BookPage

logging.basicConfig(format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                    datefmt='%Y-%m-%d %H:%M', 
                    level=logging.DEBUG, 
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list...')

page_content = requests.get('https://books.toscrape.com').content
page = BookPage(page_content)  #pass the website html content to the 'QuotePage' class 

books = page.books

#multiple page scraping (pages 2-50)
for page_number in range(1, page.page_count):
    url = f'https://books.toscrape.com/catalogue/page-{page_number+1}.html'
    page_content = requests.get(url).content
    page = BookPage(page_content)
    books.extend(page.books)


# #prints out the results (__repr__ method default unless a specific type of data is specified)
# for book in page.books:
#     print(book)
#     # print(quote.author)

