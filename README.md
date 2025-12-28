# BBC News RSS Parser

## About
This project is designed for **automatic parsing of BBC news** through their official RSS feed.
The program downloads news, extracts titles and links, descriptions and publication date, and then saves them in JSON format.

The goal of the project is **easy to get relevant news in a structured form** so that they can be used for analytics, Telegram bot or other applications.

This is my first parser and I used AI to create it. It's not bad, but I want to do such projects without it on 100%. And just by writing this project, I learned what I need to learn (namely the libraries).

---

I recommend using **virtual environment (`venv`)** to isolate project dependencies.

### Installation of dependencies
```bash
# Create a virtual environment
python -m venv .venv

# Activate virtual environment
# Linux/macOS
source .venv/bin/activate

#Windows
.venv\Scripts\activate

# Install the necessary libraries
pip install requests beautifulsoup4
```

Read [Install packages in a virtual environment using pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)