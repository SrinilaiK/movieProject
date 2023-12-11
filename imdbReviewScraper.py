import imdb
from imdb import IMDb


# Scrapes Reviews for one movie

def main():
    path = '/mnt/c/Users/Kevin/Desktop/College/!JuniorYear/MovieProject/output1Review.txt'
    ia = imdb.Cinemagoer()

    # get a movie
    title = input('Enter the movie title: ')

    id = ia.search_movie(title)[0].movieID

    
    ia1 = IMDb()

    reviews = ia1.get_movie_reviews(id)['data']['reviews']
        
    with open(path, 'w', encoding='utf-8') as f:
        # Write the content of each review to the file, limited to the first 100 reviews
        for review in reviews[:100]:
            f.write(review['content'] + "\n")
            f.write("---------\n")  

if __name__ == "__main__":
    main()