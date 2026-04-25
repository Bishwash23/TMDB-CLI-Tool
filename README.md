# tmdb-app

A CLI tool to fetch and display movies from The Movie Database (TMDB).

## Requirements

- Python 3.7+
- TMDB API key (free at [themoviedb.org](https://www.themoviedb.org))

## Installation

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/tmdb-app.git
cd tmdb-app
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set up your API key:**

Create a `.env` file in the root folder:
```
TMDB_API_KEY=your_api_key_here
```

> Get a free API key at [themoviedb.org](https://www.themoviedb.org) → Settings → API

## Usage

```bash
python tmdb_app.py --type "popular"
python tmdb_app.py --type "top"
python tmdb_app.py --type "playing"
python tmdb_app.py --type "upcoming"
```

**Arguments:**

| `--type` | Description |
|---|---|
| `popular` | Most popular movies |
| `top` | Top rated movies |
| `playing` | Now playing in theatres |
| `upcoming` | Upcoming movies |
