def recommend(movie_name):

    movie_name = movie_name.strip().lower()

    recommendations = {

        "inception": [
            "Interstellar",
            "Tenet",
            "The Prestige",
            "Doctor Strange",
            "Avatar"
        ],

        "interstellar": [
            "Inception",
            "Tenet",
            "Avatar",
            "The Prestige",
            "Doctor Strange"
        ],

        "the dark knight": [
            "Inception",
            "Tenet",
            "Iron Man",
            "Avengers Endgame",
            "The Prestige"
        ],

        "tenet": [
            "Inception",
            "Interstellar",
            "The Prestige",
            "Doctor Strange",
            "Avatar"
        ],

        "avatar": [
            "Interstellar",
            "Doctor Strange",
            "Iron Man",
            "Avengers Endgame",
            "Inception"
        ],

        "titanic": [
            "The Notebook",
            "Interstellar",
            "The Prestige",
            "Avatar",
            "Frozen"
        ],

        "the notebook": [
            "Titanic",
            "Frozen",
            "Interstellar",
            "Avatar",
            "The Prestige"
        ],

        "avengers endgame": [
            "Iron Man",
            "Doctor Strange",
            "Avatar",
            "Inception",
            "Interstellar"
        ],

        "iron man": [
            "Avengers Endgame",
            "Doctor Strange",
            "Avatar",
            "Inception",
            "Interstellar"
        ],

        "doctor strange": [
            "Iron Man",
            "Avengers Endgame",
            "Avatar",
            "Inception",
            "Interstellar"
        ],

        "frozen": [
            "Toy Story",
            "Finding Nemo",
            "Cars",
            "Titanic",
            "The Notebook"
        ],

        "toy story": [
            "Finding Nemo",
            "Cars",
            "Frozen",
            "Titanic",
            "The Notebook"
        ],

        "finding nemo": [
            "Toy Story",
            "Cars",
            "Frozen",
            "Titanic",
            "The Notebook"
        ],

        "cars": [
            "Toy Story",
            "Finding Nemo",
            "Frozen",
            "Titanic",
            "The Notebook"
        ],

        "the prestige": [
            "Inception",
            "Interstellar",
            "Tenet",
            "Doctor Strange",
            "Avatar"
        ]
    }

    return recommendations.get(movie_name, [])