import streamlit as st
from recommendation import recommend

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom, #0E1117, #111827);
}

/* Main Title */
.main-title {
    text-align: center;
    color: #FF4B4B;
    font-size: 60px;
    font-weight: 800;
    text-shadow: 0px 0px 15px rgba(255,75,75,0.7);
    margin-bottom: 30px;
}

/* Section Headings */
.section-title {
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
}

/* Recommendation Banner */
.recommend-title {
    color: #00FF88;
    font-size: 30px;
    font-weight: bold;
    text-align: center;
    margin: 20px 0;
}

/* Movie Title */
.movie-title {
    color: white;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;
}

/* Rating */
.rating {
    color: gold;
    text-align: center;
    font-size: 16px;
}

/* Genre */
.genre {
    color: #D1D5DB;
    text-align: center;
    font-size: 14px;
}

/* Input Label */
label {
    color: white !important;
    font-size: 20px !important;
    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- POSTERS ----------------
poster_dict = {

    "Inception": "posters/inception.jpg",
    "Interstellar": "posters/interstellar.jpg",
    "The Dark Knight": "posters/darkknight.jpg",
    "Tenet": "posters/tenet.jpg",
    "Avatar": "posters/avatar.jpg",
    "Titanic": "posters/titanic.jpg",
    "The Notebook": "posters/notebook.jpg",
    "Avengers Endgame": "posters/endgame.jpg",
    "Iron Man": "posters/ironman.jpg",
    "Doctor Strange": "posters/doctorstrange.jpg",
    "Frozen": "posters/frozen.jpg",
    "Toy Story": "posters/toystory.jpg",
    "Finding Nemo": "posters/nemo.jpg",
    "Cars": "posters/car.jpg",
    "The Prestige": "posters/prestige.jpg"

}

# ---------------- RATINGS ----------------
ratings = {

    "Inception": "⭐ 8.8",
    "Interstellar": "⭐ 8.7",
    "The Dark Knight": "⭐ 9.0",
    "Tenet": "⭐ 7.5",
    "Avatar": "⭐ 7.8",
    "Titanic": "⭐ 7.9",
    "The Notebook": "⭐ 7.8",
    "Avengers Endgame": "⭐ 8.4",
    "Iron Man": "⭐ 7.9",
    "Doctor Strange": "⭐ 7.5",
    "Frozen": "⭐ 7.4",
    "Toy Story": "⭐ 8.3",
    "Finding Nemo": "⭐ 8.2",
    "Cars": "⭐ 7.2",
    "The Prestige": "⭐ 8.5"

}

# ---------------- GENRES ----------------
genres = {

    "Inception": "Sci-Fi • Thriller",
    "Interstellar": "Adventure • Drama • Sci-Fi",
    "The Dark Knight": "Action • Crime • Drama",
    "Tenet": "Action • Sci-Fi • Thriller",
    "Avatar": "Adventure • Fantasy • Sci-Fi",
    "Titanic": "Drama • Romance",
    "The Notebook": "Drama • Romance",
    "Avengers Endgame": "Action • Adventure • Sci-Fi",
    "Iron Man": "Action • Adventure • Sci-Fi",
    "Doctor Strange": "Action • Fantasy • Sci-Fi",
    "Frozen": "Animation • Family • Fantasy",
    "Toy Story": "Animation • Comedy • Family",
    "Finding Nemo": "Animation • Adventure • Family",
    "Cars": "Animation • Comedy • Family",
    "The Prestige": "Drama • Mystery • Thriller"

}

# ---------------- TITLE ----------------
st.markdown(
    """
    <div class="main-title">
        🎬 AI Movie Recommendation System
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- INPUT ----------------
st.markdown(
    "<div class='section-title'>Enter Movie Name</div>",
    unsafe_allow_html=True
)

movie = st.text_input(
    "",
    placeholder="Example: Titanic"
)

# ---------------- BUTTON ----------------
if st.button("🎥 Recommend Movies"):

    recommendations = recommend(movie)

    if not recommendations:

        st.error("Movie not found!")

    else:

        st.markdown(
            """
            <div class="recommend-title">
                🍿 Recommended Movies For You
            </div>
            """,
            unsafe_allow_html=True
        )

        cols = st.columns(5)

        for i, movie_name in enumerate(recommendations):

            with cols[i]:

                if movie_name in poster_dict:

                    st.image(
                        poster_dict[movie_name],
                        use_container_width=True
                    )

                st.markdown(
                    f"""
                    <div class="movie-title">
                        {movie_name}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="rating">
                        {ratings.get(movie_name,'⭐ N/A')}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="genre">
                        {genres.get(movie_name,'')}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.info(
            "Recommendations are generated based on movie similarity."
        )