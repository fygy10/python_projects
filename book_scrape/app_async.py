import requests
import logging
import async_timeout
import asyncio
import aiohttp
import time

from pages.pages import BookPage

logging.basicConfig(format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                    datefmt='%Y-%m-%d %H:%M', 
                    level=logging.DEBUG, 
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = BookPage(page_content)  #pass the website html content to the 'QuotePage' class 

loop = asyncio.get_event_loop()

books = page.books

async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:    #tasks move to here one by one; results printed below
            print(f'Page took {time.time() - page_start}')      #tasks likely not finish in the sam eorder depending on length of request time
            return await response.text()
        

#not creating a session for each page want to fetch aggregates them
async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop = loop) as session:   #iterate over urls and 
        for url in urls:
            tasks.append(fetch_page(session, url))      #append the co-rountine urls create into tasks list once passed through 'fetch_page' function
        grouped_tasks = asyncio.gather(*tasks)  #gather all tasks
        return await grouped_tasks  #return;waits for tasks to all be completed

urls = [f'http://books.toscrape.com/catalogue/page-{page_number+1}.html' for page_number in range(1, page.page_count)] #MAC avoid https
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total pages time: {time.time() - start}')

for page_content in pages:
    page = BookPage(page_content)
    books.extend(page.books)