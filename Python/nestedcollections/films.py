movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    },
    {
        "title": "Animal",
        "year": 2023,
        "language": "Hindi",
        "genres": ["Drama", "Action", "Thriller"],
        "rating": 8.2
    }
]

# Q1: Total number of movies
total_movies = len(movies)  # Calculate the total number of movies in the list
print(f"Total movies are {total_movies}.")  # Print the total number of movies

# Q2: Movies with genre Drama
drama_movies = [mov.get("title") for mov in movies if "Drama" in mov.get("genres")]  # Extract titles of movies that have "Drama" as one of their genres
print(f"The movies with genre drama are {drama_movies}.")  # Print the titles of drama movies

# Q3: Latest movie
def latest(m):
    return m.get("year")  # Function to get the year of a movie

latest_movie = max(movies, key=latest)  # Find the movie with the latest year
latest_movies = [m.get("title") for m in movies if m.get("year") == latest_movie.get("year")]  # Extract titles of movies released in the latest year
print(f"Latest movies are {latest_movies}.")  # Print the titles of the latest movies

# Q4: Top movie (movie with highest rating)
def high_rating(m):
    return m.get("rating")  # Function to get the rating of a movie

highest_rating_movie = max(movies, key=high_rating)  # Find the movie with the highest rating
highest_rating_movies = [m.get("title") for m in movies if m.get("rating") == highest_rating_movie.get("rating")]  # Extract titles of movies with the highest rating
print(f"Highest rated movie is {highest_rating_movies}.")  # Print the titles of the highest-rated movies

# Q5: Movies with language Malayalam
malay_movies = [m.get("title") for m in movies if "Malayalam" in m.get("language")]  # Extract titles of movies with the language "Malayalam"
print(f"Movies with language Malayalam are {malay_movies}.")  # Print the titles of Malayalam movies

# Q6: Movies released after year 2016
movies_after_2016 = [m.get("title") for m in movies if m.get("year") > 2016]  # Extract titles of movies released after the year 2016
print(f"Movies released after 2016 are {movies_after_2016}.")  # Print the titles of movies released after 2016

# Q7: Movie with lowest rating
def low_rating(m):
    return m.get("rating")  # Function to get the rating of a movie

low_rating_movie = min(movies, key=low_rating)  # Find the movie with the lowest rating
print(f"Lowest rating movie is {low_rating_movie}.")  # Print the movie with the lowest rating

# Q8: Hindi movies with genre Action
hindi_action_movies = [m.get("title") for m in movies if m.get("language") == "Hindi" and "Action" in m.get("genres")]  # Extract titles of Hindi movies with "Action" genre
print(f"Hindi movies with genre action are {hindi_action_movies}.")  # Print the titles of Hindi action movies

# Q9: Movies released in the same years
movie_dictionary = {}  # Initialize an empty dictionary

for m in movies:
    release_year = m.get("year")  # Get the release year of the movie
    if release_year in movie_dictionary:  # If the year is already in the dictionary
        movie_dictionary.get(release_year).append(m.get("title"))  # Append the movie title to the list for that year
    else:
        movie_dictionary[release_year] = [m.get("title")]  # Create a new list for the year and add the movie title

print(movie_dictionary)  # Print the dictionary of movies released in the same years

# Q10: Oldest movie
oldest_movie = min(movies, key=lambda m: m.get("year"))  # Find the movie with the oldest year
oldest_movie_year = oldest_movie.get("year")  # Get the year of the oldest movie
oldest_movie_names = [m.get("title") for m in movies if m.get("year") == oldest_movie_year]  # Extract titles of movies released in the oldest year
print("Oldest movie(s):")
print(oldest_movie_names)  # Print the titles of the oldest movies

# Q11: Movies with genres either Drama or Comedy
drama_comedy = [m.get("title") for m in movies if "Drama" in m.get("genres") or "Comedy" in m.get("genres")]  # Extract titles of movies with either "Drama" or "Comedy" genres
print(f"Movies with genre either drama or comedy are {drama_comedy}.")  # Print the titles of drama or comedy movies

# Q12: Number of movies released in each year
years = [m.get("year") for m in movies]  # Extract the release years of all movies
year_count = {y: years.count(y) for y in years}  # Count the number of movies released each year
print(year_count)  # Print the count of movies released each year

# Q13: Print all genres
genres = {g for m in movies for g in m.get("genres")}  # Extract all unique genres from the movies
print(genres)  # Print the unique genres

# Q14: Print the count of each genre
all_genres = [g for m in movies for g in m.get("genres")]  # Extract all genres from the movies
genre_count = {g: all_genres.count(g) for g in all_genres}  # Count the number of occurrences of each genre
print(genre_count)  # Print the count of each genre

# Q15: Sort the movies in alphabetical order
sorted_movies = sorted(movies, key=lambda mov: mov.get("title"))  # Sort the movies by title in alphabetical order
sorted_movies_title = [m.get("title") for m in sorted_movies]  # Extract the sorted titles of the movies
print(f"Sorted movie titles are: {sorted_movies_title}.")  # Print the sorted movie titles
