import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import search_producthunt, get_sample_reviews, compute_sentiments, compute_app_sentiment_score

st.title(" Sentiment Analysis on App Reviews")

# Entrée utilisateur pour le nom du produit
query = st.text_input("Enter a product keyword to search:", "calendar")

if query:
    # Recherche des apps
    df = search_producthunt(query)
    st.write("### Search Results", df)

    sentiment_scores = {}
    if not df.empty:
        for app in df["Name"].head(5):  # Limite à 5 apps pour le test
            reviews = get_sample_reviews(app)
            sentiments = compute_sentiments(reviews)
            score = compute_app_sentiment_score(sentiments)
            sentiment_scores[app] = score

        # Afficher les résultats dans un graphique
        st.write("### Sentiment Scores")
        sentiment_df = pd.DataFrame(sentiment_scores).T
        st.bar_chart(sentiment_df)

        # Détails d’une app
        selected_app = st.selectbox("Select an app to see review sentiments:", sentiment_scores.keys())
        if selected_app:
            reviews = get_sample_reviews(selected_app)
            results = compute_sentiments(reviews)
            st.write("### Detailed Sentiment Results")
            for i, r in enumerate(results):
                st.write(f"Review {i+1}: {reviews[i]}")
                st.write(f"Sentiment: {r['label']} (Score: {r['score']:.2f})")
