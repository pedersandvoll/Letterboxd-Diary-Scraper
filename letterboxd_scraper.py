import requests
from bs4 import BeautifulSoup
import csv

def scrape_letterboxd_diary():
    url = "https://letterboxd.com/pedersandvoll/films/diary/for/2024/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all diary entries
    diary_entries = soup.find_all('tr', class_='diary-entry-row')
    
    movies = []
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
    
    # Write to CSV
    with open('letterboxdExport.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['MovieTitle', 'MovieReleaseDate', 'UserRating'])
        writer.writerows(movies)

if __name__ == "__main__":
    scrape_letterboxd_diary()
