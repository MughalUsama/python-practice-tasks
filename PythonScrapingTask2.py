from bs4 import BeautifulSoup
import requests


def get_scrapped_dictionary(url):
    result_dict = dict()
    while url:
        page = requests.get(url)  # parsing main page
        soup = BeautifulSoup(page.text, "html.parser")
        entry_titles = soup.find_all('h2', attrs={"class": "entry-title"})
        for entry in entry_titles:
            entry_descendants = entry.descendants
            for desc in entry_descendants:
                if desc.name == 'a' and desc.get('rel', '') == ['bookmark'] and desc.get("href", "") != "":
                    description_page = requests.get(desc.get("href"))  # parsing description pages
                    description_soup = BeautifulSoup(description_page.text, "html.parser")
                    description_entry_titles = description_soup.find_all('h1', attrs={"class": "entry-title"})
                    description_entry_img = description_soup.select('p > img')
                    description_entry_img = [img['data-src'] for img in description_entry_img]
                    result_dict[description_entry_titles[0].text] = description_entry_img
        next_url = soup.select(".nav-previous a")
        if next_url:
            url = next_url[0]['href']
        else:
            url = None
    return result_dict


if __name__ == "__main__":
    site_url = "http://recurship.com/"
    result = get_scrapped_dictionary(site_url)
    print(result)
