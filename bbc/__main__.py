from bbc.cli.args import parse_args
from bbc.cli.handlers import (
    handle_list_topics,
    handle_parse,
    handle_parse_all
)

def main():
    args = parse_args()

    if args.list_topics:
        handle_list_topics()
    elif args.parse:
        handle_parse(args.parse, args.limit, args.output)
    elif args.parse_all:
        handle_parse_all(args.limit, args.output)

if __name__ == '__main__':
    main()