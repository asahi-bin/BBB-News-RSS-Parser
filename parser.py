# https://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup

def parse_news(html: str, limit: int) -> list:
    soup = BeautifulSoup(html, 'xml')
    articles = soup.find_all('item')

    news = []

    for article in articles[:limit]:
        title_tag = article.find('title')
        description_tag = article.find('description')
        data_tag = article.find('pubDate')
        link_tag = article.find('link')

        if not title_tag or not link_tag:
            continue

        news.append({
            'title': title_tag.get_text(strip=True),
            'description': description_tag.get_text(strip=True),
            'data': data_tag.get_text(strip=True),
            'url': link_tag.get_text(strip=True)
        })

    return news