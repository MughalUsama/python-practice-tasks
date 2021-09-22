import requests
from bs4 import BeautifulSoup


def scrap_site(url, no_of_pages_to_scrap):
    books_dict = dict()
    page_no = 1
    while url:
        print("Scrapping Page . . .", page_no)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        all_links = [a["href"] for a in soup.select('.product_pod h3 a')]
        for description_link in all_links:
            if description_link.split('/')[0] != 'catalogue':  # if not on 1st page
                description_link = 'catalogue/'+description_link
            if len(url.split('/')) > 4:  # if not on 1st page
                url = url.rsplit('/', 2)[0] + '/'
            description_page = requests.get(url+description_link)
            description_soup = BeautifulSoup(description_page.text, "html.parser")
            title = description_soup.select('.product_main > h1')[0].text
            price_without_tax = description_soup.find_all(text='Price (excl. tax)')[0].parent.next_sibling.text[1:]
            price_with_tax = description_soup.find_all(text='Price (incl. tax)')[0].parent.next_sibling.text[1:]
            price_dict = dict()
            price_dict['Price (excl. tax)'] = price_without_tax
            price_dict['Price (incl. tax)'] = price_with_tax
            books_dict[title] = price_dict
        next_url = soup.select('.next a')[0]["href"]   # extracting url from next button
        if next_url:
            if not next_url.startswith('catalogue'):  # if not on 1st page and url does not start with catalogue
                next_url = 'catalogue/'+next_url
            url = url.rpartition('/')[0]+"/"+next_url  # concatenating new url with base. Splitting till last '/'
            # to get current base url
        else:
            url = None
        if page_no == no_of_pages_to_scrap:
            break
        page_no += 1
    return books_dict


if __name__ == "__main__":
    _url = 'http://books.toscrape.com/'
    pages_to_scrap = 3
    print(scrap_site(_url, pages_to_scrap))
