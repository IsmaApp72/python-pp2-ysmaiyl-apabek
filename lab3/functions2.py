# Define the list of movies as provided
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Task 1: Function to check if a movie's IMDB score is above 5.5
def is_highly_rated(movie):
    return movie['imdb'] > 5.5

# Task 2: Function to get sublist of movies with IMDB score above 5.5
def get_highly_rated_movies(movies_list):
    return [movie for movie in movies_list if movie['imdb'] > 5.5]

# Task 3: Function to get movies by category
def get_movies_by_category(movies_list, category):
    return [movie for movie in movies_list if movie['category'] == category]

# Task 4: Function to compute the average IMDB score
def average_imdb_score(movies_list):
    total_score = sum(movie['imdb'] for movie in movies_list)
    return total_score / len(movies_list)

# Task 5: Function to compute the average IMDB score for a given category
def average_imdb_score_by_category(movies_list, category):
    category_movies = get_movies_by_category(movies_list, category)
    if category_movies:
        return average_imdb_score(category_movies)
    return 0  # Return 0 if no movies are found in the category

# Now let's test the functions with the provided movies data

# Test for Task 1
test_movie = {"name": "Test Movie", "imdb": 6.0, "category": "Test"}
is_movie_highly_rated = is_highly_rated(test_movie)

# Test for Task 2
highly_rated_movies = get_highly_rated_movies(movies)

# Test for Task 3
category = "Romance"
movies_in_category = get_movies_by_category(movies, category)

# Test for Task 4
avg_imdb = average_imdb_score(movies)

# Test for Task 5
avg_imdb_romance = average_imdb_score_by_category(movies, category)

(is_movie_highly_rated, highly_rated_movies, movies_in_category, avg_imdb, avg_imdb_romance)
