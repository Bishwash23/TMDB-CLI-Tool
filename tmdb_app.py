import argparse, sys
from api import fetch_movies
from display import display_movies

def main():
    args = parse_args()
    if args.type not in ["playing", "popular", "top", "upcoming"]:
        sys.exit("Invalid type")
    
    movies = fetch_movies(args.type)
    display_movies(movies, args.type)

def parse_args():
    parse = argparse.ArgumentParser()

    parse.add_argument(
        "--type",
        choices=["playing", "popular", "top", "upcoming"],
        required=True
    )

    return parse.parse_args()

main()