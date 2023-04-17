import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
                url,
                headers={"user-agent": "Fake user-agent"},
                timeout=3
            )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    links_to_news = []
    all_news = selector.css('article.entry-preview')
    for new in all_news:
        link = new.css("a::attr(href)").get()
        links_to_news.append(link)
    return links_to_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link_to_next_page = selector.css('a.next.page-numbers::attr(href)').get()
    return link_to_next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    site_trybe = ('https://blog.betrybe.com')
    xomps = scrape_updates(site_trybe)
    print(xomps)
