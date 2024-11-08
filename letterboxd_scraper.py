import requests
from bs4 import BeautifulSoup
import csv

def scrape_letterboxd_diary():
    base_url = "https://letterboxd.com/pedersandvoll/films/diary/for/2024/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    movies = []
    page = 1
    while True:
        url = f"{base_url}page/{page}/" if page > 1 else base_url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all diary entries
        diary_entries = soup.find_all('tr', class_='diary-entry-row')
        
        # If no entries found, we've reached the end
        if not diary_entries:
            break
    
        for entry in diary_entries:
            # Get movie title
            title_element = entry.find('h3', class_='headline-3')
            if title_element:
                title = title_element.find('a').text.strip()
            
            # Get release year
            year_element = entry.find('td', class_='td-released')
            if year_element:
                release_date = year_element.text.strip()
                
            # Get rating
            rating_element = entry.find('span', class_='rating')
            rating = ''
            if rating_element and 'class' in rating_element.attrs:
                classes = rating_element['class']
                for class_name in classes:
                    if class_name.startswith('rated-'):
                        rating = class_name.replace('rated-', '') + '/5'
                        break
        
            movies.append([title, release_date, rating])
        
        page += 1
    
    # Write to CSV in Letterboxd import format
    with open('letterboxd-import.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Year', 'Rating', 'WatchedDate'])
        
        for movie in movies:
            title = movie[0]
            year = movie[1]
            # Convert rating from "X/5" format to just the number
            rating = movie[2].split('/')[0] if movie[2] else ''
            # Get today's date as watched date since we don't have the actual watch date
            watched_date = "2024-01-01"  # You might want to adjust this
            
            writer.writerow([title, year, rating, watched_date])

if __name__ == "__main__":
    scrape_letterboxd_diary()
