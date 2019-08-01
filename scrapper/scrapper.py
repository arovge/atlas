from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# headless browser
def get_page():
    url = 'https://catalog.msoe.edu/content.php?catoid=20&navoid=557'
    options = Options()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver.page_source

# parsing stuff
def get_link_list(page):
    soup = BeautifulSoup(page, 'html.parser')
    table_body = soup.find('table', class_='table_default').find('tbody')
    rows = table_body.find('tr', { 'role': 'main' })
    cells = rows.find('td', class_='block_n2_and_content')
    nested_table = cells.find_all('table', class_='table_default')[-1]
    nested_cell = nested_table.find_all('tr')[-1]
    links = nested_cell.find_all('a')
    link_list = map(lambda link : 'https://catalog.msoe.edu' + link['href'], links)
    return link_list

def main():
    page = get_page()
    link_list = get_link_list(page)
    for link in link_list:
        print(link)


if __name__ == '__main__':
    main()