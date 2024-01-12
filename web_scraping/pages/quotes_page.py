from bs4 import BeautifulSoup

from web_scraping.locators.quotes_page_locators import QuotesPageLocators
from web_scraping.parsers import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.soup.select(QuotesPageLocators.QUOTE)]
