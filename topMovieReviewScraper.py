import requests
from bs4 import BeautifulSoup
import imdb
from imdb import IMDb
import csv
import json


def scrape_titles(url):
    page = requests.get(url)
    page
    # Page Response 200 means page is validated
    soup = BeautifulSoup(page.content, 'html.parser')
    movie_titles = soup.find_all('span', {'data-qa': 'discovery-media-list-item-title'})

    # Parse Movies
    titles = []
    for movie in movie_titles:
        titles.append(movie.get_text().strip())
    
    return titles

def main():

    #  grab latest releases of movies
    # Edit page number to increase number of movies
    url = "https://www.rottentomatoes.com/browse/movies_in_theaters/sort:popular?page=1"
    titles = scrape_titles(url)

    ia = imdb.Cinemagoer()
    ia1 = IMDb()


    # Now grab the reviews for the latest releases if available

    # Define a delimiter to separate reviews
    #review_delimiter = "\n     \n"

    # with open('latest_movies_reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:

    #     csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     # Write the header row
    #     csvwriter.writerow(['Movie Title', 'Movie ID', 'Review Content'])

    all_reviews = []
    movie_count = 0
    for title in titles:
        try:
            search_results =  ia.search_movie(title)
            if not search_results:
                print(f'No results for {title}')
                continue

            id = search_results[0].movieID
            reviews_data = ia.get_movie_reviews(id)

            if not reviews_data or 'reviews' not in reviews_data['data']:
                print(f"No reviews found for {title}")
                continue  # Skip to the next movie

            reviews = reviews_data['data']['reviews']
            if len(reviews) < 10:
                continue

            reviews = reviews[:100] if len(reviews) > 100 else reviews
            #reviews = review_delimiter.join(review['content'].replace('\n', ' ') for review in reviews)
            #csvwriter.writerow([title, id, reviews])

            # Add the movie and its reviews to the list
            all_reviews.append({
            'title': title,
            'movie_id': id,
            'review amount': len(reviews),
            'reviews': [{'content': review['content']} for review in reviews]
            })
            movie_count += 1 # Increment the movie count

        except Exception as e:
            # If an error occurs, print it and continue with the next movie
            print(f"An error occurred while processing {title}: {e}")
            continue
        
    final_json = {
        'total_movies': movie_count,
        'movies': all_reviews
    }
    # Save the data to a JSON file
    with open('latest_movies_reviews.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(final_json, jsonfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()