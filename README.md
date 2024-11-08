# aiderScripts

## Letterboxd Diary Scraper

A Python script to scrape your Letterboxd diary entries and export them in a format compatible with Letterboxd's import feature.

### Requirements

```
requests
beautifulsoup4
```

### Installation

```bash
pip install requests beautifulsoup4
```

### Usage

You can run the script in two ways:

1. Using environment variable:
```bash
export LETTERBOXD_USERNAME=your_username
python letterboxd_scraper.py
```

2. Passing username as command line argument:
```bash
python letterboxd_scraper.py your_username
```

The script will create a `letterboxd-import.csv` file in the current directory with your diary entries formatted for Letterboxd import.
