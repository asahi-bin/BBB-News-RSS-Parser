import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description = 'BBC News RSS Parser'
    )

    mode = parser.add_mutually_exclusive_group(required=True)

    mode.add_argument('-l', '--list-topics', action='store_true', help='Show available BBC topics')
    mode.add_argument('-p', '--parse', type=str, help='Parse BBC topic (default: Top_Stories)')
    mode.add_argument('--parse-all', action='store_true', help='Parse all BBC topics')

    parser.add_argument('--limit', type=int, default=None, help='Limit number of parsed news')
    parser.add_argument('-o', '--output', type=str, default='./bbc/data', help='Output directory')

    return parser.parse_args()