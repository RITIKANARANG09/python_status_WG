import requests
import selenium
from web_scraping.pages import QuotesPage

page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)
