import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(layout="wide")
st.title("📊 Data Visualizations")

# --- Check if data is available ---
if "results_df" not in st.session_state:
    st.warning("No data found. Please perform a search on the 'Results Table' page first.")
    st.stop()

# Load data
df = st.session_state["results_df"]

# --- Sidebar Filters ---
st.sidebar.header("🔎 Filter Options")
app_ids = df["Name"].unique().tolist()
selected_ids = st.sidebar.multiselect("Select Application(s) by Name:", app_ids, default=app_ids)

filtered_df = df[df["Name"].isin(selected_ids)]

# --- Layout Columns ---
col1, col2 = st.columns(2)

# --- Bar Chart: Ratings Distribution ---
with col1:
    st.subheader("⭐ Ratings Distribution")
    if "Rating" in filtered_df.columns:
        fig, ax = plt.subplots()
        sns.histplot(filtered_df["Rating"], bins=10, ax=ax)
        st.pyplot(fig)
    else:
        st.info("No rating data available.")

# --- Bar Chart: Top Rated Apps ---
with col2:
    st.subheader("🏆 Top Rated Apps")
    top_apps = filtered_df.sort_values("Rating", ascending=False).head(10)
    st.bar_chart(top_apps.set_index("Name")["Rating"])

# --- Pie Chart: Paid vs Free ---
st.subheader("💰 Free vs Paid (simulated)")

# Add dummy Paid/Free column if needed
if "Paid" not in df.columns:
    import numpy as np
    filtered_df["Paid"] = np.random.choice(["Free", "Paid"], size=len(filtered_df))

pie_data = filtered_df["Paid"].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=140)
ax2.axis("equal")
st.pyplot(fig2)

# --- Word Cloud: Based on Taglines or Descriptions ---
st.subheader("☁️ Word Cloud (from Taglines)")

text = " ".join(filtered_df["Tagline"].dropna().tolist())

if text:
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig3, ax3 = plt.subplots()
    ax3.imshow(wordcloud, interpolation='bilinear')
    ax3.axis('off')
    st.pyplot(fig3)
else:
    st.info("No taglines available for word cloud.")
