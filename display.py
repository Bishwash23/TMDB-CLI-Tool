import sys

def display_movies(movies, type):
    if not movies:
        sys.exit("No movies found")

    title_map = {
        "playing" : "Now Playing Movies",
        "popular" : "Popular Movies",
        "top" : "Top Rated Movies",
        "upcoming" : "Upcoming Movies"
    }
    
    header = title_map[type]
    print(header)
    print("--------------------------------------------------")
    for index, movie in enumerate(movies):
        print(index+1)
        print(movie["title"])
        print(movie["overview"])
        print(movie["vote_average"], "/10")
        print(movie["release_date"])
        print("--------------------------------------------------")
