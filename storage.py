import json
from datetime import datetime

def save_to_json(news: list, path: str):
    data = {
        'source': 'BBC',
        'parsed_at': datetime.now().isoformat(),
        'news': news
    }

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
