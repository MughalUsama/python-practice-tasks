import random
from itertools import cycle
import requests
from bs4 import BeautifulSoup


def get_proxies_pool():
    proxies_url = 'https://www.sslproxies.org/'

    # Retrieve the site's page. The 'with'(Python closure) is used here in order to automatically close the session
    # when done
    with requests.Session() as res:
        proxies_page = res.get(proxies_url)

    # Create a BeautifulSoup object and find the table element which consists of all proxies
    proxies_soup = BeautifulSoup(proxies_page.content, 'html.parser')
    proxies_table = proxies_soup.find(class_='table')

    # Go through all rows in the proxies table and store them in the right format (IP:port) in our proxies list
    proxies = []
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append('{}:{}'.format(row.find_all('td')[0].string, row.find_all('td')[1].string))
    return proxies


def random_header():
    # Create a dict of accept headers for each user-agent.
    accepts = {"Firefox": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Safari, Chrome": "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,"
                                 "*/*;q=0.5"}
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 "
        "Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"]
    # Just for case user agents are not extracted from fake-user-agent package

    random_user_agent = random.choice(user_agents)
    valid_accept = accepts['Firefox'] if random_user_agent.find('Firefox') > 0 else accepts['Safari, Chrome']
    headers = {"User-Agent": random_user_agent,
               "Accept": valid_accept}
    return headers


def create_pools():
    proxies = get_proxies_pool()
    headers = [random_header() for _ in range(len(proxies))]  # list of headers, same length as the proxies list

    # This transforms the list into itertools.cycle object (an iterator) that we can run
    # through using the next() function in lines 16-17.
    proxies_pool = cycle(proxies)
    headers_pool = cycle(headers)
    return proxies_pool, headers_pool


def get_titles():
    # Usage example
    all_titles_list = []
    proxies_pool, headers_pool = create_pools()
    current_proxy = next(proxies_pool)
    current_headers = next(headers_pool)
    url = "https://www.sciencedirect.com/browse/journals-and-books?page={}&subject=environmental-science"
    page_number = 2
    while True:
        with requests.Session() as req:
            """page = req.get(url.format(page_number), proxies={"http": "http://" + current_proxy, "https": "http://" +
                                                                                                         current_proxy},
                           headers=current_headers, timeout=30, verify=False)
            """
            page = req.get(url.format(page_number))
        soup = BeautifulSoup(page.text, "html.parser")
        lst = soup.find_all("h1")
        all_titles_list.append([title.text for title in lst])
        page_number += 1
        current_proxy = next(proxies_pool)
        current_headers = next(headers_pool)
        next_button = soup.find_all('button', attrs={"aria-label": "Next page"})

        if page_number > 14 or (next_button and next_button[0].has_attr('disabled')):
            break
    return all_titles_list


if __name__ == "__main__":
    titles = get_titles()
    print(titles)
