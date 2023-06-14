import requests

from pages.quote_pages import QuotePage

page_content = requests.get('https://quotes.toscrape.com/').content
page = QuotePage(page_content)  #pass the website html content to the 'QuotePage' class 


#prints out the results (__repr__ method default unless a specific type of data is specified)
for quote in page.quotes:
    print(quote)
    # print(quote.author)

