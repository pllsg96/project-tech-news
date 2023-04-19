import requests
import time
from parsel import Selector
from pprint import pprint


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
    all_news = selector.css("article.entry-preview")
    for new in all_news:
        link = new.css("a::attr(href)").get()
        links_to_news.append(link)
    return links_to_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link_to_next_page = selector.css("a.next.page-numbers::attr(href)").get()
    return link_to_next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    # news_data = []
    news_url = selector.css("link[rel='canonical']::attr(href)").get()
    news_title = selector.css("h1.entry-title::text").get()
    news_title = news_title.strip()
    news_timestamp = selector.css("li.meta-date::text").get()
    news_writer = selector.css("a.url.fn.n::text").get()
    news_reading_time = selector.css("li.meta-reading-time::text").get()
    news_reading_time = news_reading_time.split(" ")
    news_summary = selector.css(
        "div.entry-content:first-of-type > p:nth-of-type(1) *::text"
        ).getall()
    news_summary = ("".join(news_summary)).strip()
    news_category = selector.css("span.label::text").get()

    return {
        "url": news_url,
        "title": news_title,
        "timestamp": news_timestamp,
        "writer": news_writer,
        "reading_time": int(news_reading_time[0]),
        "summary": news_summary,
        "category": str(news_category),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    url = ("https://blog.betrybe.com/carreira/frases-de-lideranca/")
    site_trybe = fetch(url)
    xomps = scrape_news(site_trybe)
    pprint(xomps)
