from recommendation import recommend

movies = recommend("Inception")

for movie in movies:
    print(movie)