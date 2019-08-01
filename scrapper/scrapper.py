from bs4 import BeautifulSoup
from browser import CatalogBrowser

def find_nested_rows(page):
    soup = BeautifulSoup(page, 'html.parser')
    table_body = soup.find('table', class_='table_default').find('tbody')
    rows = table_body.find('tr', { 'role': 'main' })
    cells = rows.find('td', class_='block_n2_and_content')
    nested_table = cells.find_all('table', class_='table_default')
    print(nested_table)
    return nested_table

def process_page(browser, link):
    page = browser.get_page(link)
    nested_rows = browser.find_nested_rows(page)
    for row in nested_rows:
        course = row.find_all('td', class_='width')
        if course:
            print(course[0].find('a'))

def main():
    browser = CatalogBrowser()
    link_list = browser.link_list
    for link in link_list:
        process_page(browser, link)

if __name__ == '__main__':
    main()