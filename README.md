 Movie Recommendation System:
Performed data preprocessing and combined relevant text features (such as overview, genres, cast, crew, etc.) into a single column called "tags".
Applied Porter Stemmer to normalize the text (stemming similar words to their root form).
Used CountVectorizer to convert the textual data into numerical vectors.
Calculated cosine similarity scores to find the top 4 most similar movies based on the user's selected movie.
Built a clean and interactive web interface using Streamlit, allowing users to search and get instant movie recommendations.



 Tools & Libraries:
Pandas, Numpy, Scikit-learn (for preprocessing and ML)
NLTK (for stemming)
Streamlit (for frontend)
