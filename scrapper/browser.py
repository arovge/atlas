from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class CatalogBrowser:
    def __init__(self):
        options = Options()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.link_list = []
        self.get_link_list()
        
    def get_page(self, url):
        self.driver.get(url)
        return self.driver.page_source

    def get_link_list(self):
        page = self.get_page('https://catalog.msoe.edu/content.php?catoid=20&navoid=557')
        nested_rows = self.find_nested_rows(page)
        self.find_links(nested_rows)

    def find_nested_rows(self, page):
        soup = BeautifulSoup(page, 'html.parser')
        table_body = soup.find('table', class_='table_default').find('tbody')
        rows = table_body.find('tr', { 'role': 'main' })
        cells = rows.find('td', class_='block_n2_and_content')
        nested_table = cells.find_all('table', class_='table_default')[-1]
        nested_cell = nested_table.find_all('tr')
        return nested_cell

    def find_links(self, nested_rows):
        nested_cell = nested_rows[-1]
        links = nested_cell.find_all('a')
        self.link_list = list(map(lambda link : 'https://catalog.msoe.edu' + link['href'], links))