from fetcher import fetch_page
from parser import parse_news
from storage import save_to_json

BBC_URL = 'https://feeds.bbci.co.uk/news/rss.xml'

def main():
    html = fetch_page(BBC_URL)
    news = parse_news(html)
    save_to_json(news, 'data/news.json')

if __name__ == '__main__':
    main()
