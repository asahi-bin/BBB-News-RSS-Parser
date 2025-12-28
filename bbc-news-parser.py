import argparse
import os

from fetcher import fetch_page
from parser import parse_news
from storage import save_to_json
from config import BBS_TOPICS

def print_topics():
    print('Available BBC topics:')
    for topic in BBS_TOPICS:
        print(f' - \033[32m{topic}\033[0m')

def main():
    parser = argparse.ArgumentParser(
        description='BBC News RSS Parser'
    )

    parser.add_argument(
        '-l', '--list-topics',
        action='store_true',
        help='Show available BBC topics'
    )

    parser.add_argument(
        '-p', '--parse',
        type=str,
        help='Parse BBC topic (default: Top_Stories)'
    )

    parser.add_argument(
        '--parse-all',
        action='store_true',
        help='Parse all BBC topics'
    )

    parser.add_argument(
        '--limit',
        type=int,
        default=None,
        help='Limit number of parsed news'
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        default='./data',
        help='Output directory'
    )

    args = parser.parse_args()
    # print(args)
    
    if args.list_topics:
        print_topics()
        return

    os.makedirs(args.output, exist_ok=True)

    if args.parse_all:
        for topic, url in BBS_TOPICS.items():
            print(f'\033[32m[+]\033[0m Parsing {topic}')
            html = fetch_page(url)
            news = parse_news(html, limit=args.limit)
            save_to_json(
                news,
                f'{args.output}/{topic}.json',
                topic
            )
    else:
        if args.parse not in BBS_TOPICS:
            print('\033[31mUnknown topic\033[0m')
            return
        
        url = BBS_TOPICS[args.parse]
        html = fetch_page(url)
        news = parse_news(html, limit=args.limit)
        save_to_json(
            news,
            f'{args.output}/{args.parse}.json',
            args.parse
        )

    # html = fetch_page(BBC_URL)
    # news = parse_news(html)
    # save_to_json(news, 'data/news.json')

if __name__ == '__main__':
    main()
