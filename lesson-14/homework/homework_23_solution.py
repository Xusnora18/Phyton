
import json
import random
import requests

# Task 1: JSON Parsing
def task_1_parse_students():
    with open("students.json", "r") as file:
        students = json.load(file)
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Task 2: Weather API
def task_2_weather_api(city="Tashkent"):
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("Failed to retrieve data")

# Task 3: JSON Modification
def task_3_manage_books():
    def load_books():
        with open("books.json", "r") as file:
            return json.load(file)

    def save_books(books):
        with open("books.json", "w") as file:
            json.dump(books, file, indent=4)

    books = load_books()

    # Example of adding a book
    books.append({"title": "New Book", "author": "John Doe", "year": 2025})

    # Example of updating a book
    for book in books:
        if book["title"] == "Old Title":
            book["title"] = "Updated Title"

    # Example of deleting a book
    books = [book for book in books if book["title"] != "Book To Delete"]

    save_books(books)

# Task 4: Movie Recommendation System
def task_4_recommend_movie(genre):
    api_key = "your_api_key_here"
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "Search" in data:
            movie = random.choice(data["Search"])
            print(f"Recommended Movie: {movie['Title']} ({movie['Year']})")
        else:
            print("No movies found for this genre.")
    else:
        print("Failed to retrieve movie data")
