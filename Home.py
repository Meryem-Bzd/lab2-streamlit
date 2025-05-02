import streamlit as st

st.title("🔍 Competitor Analysis App")

st.markdown("""
Welcome to our Streamlit web application for interactive competitor analysis based on real-time web data.

---

### 📌 Project Overview

This app allows you to:
- Perform a **custom search** on any type of product or application
- Automatically retrieve results through **dynamic web scraping** 
- Display the data in a **results table**
- Generate **interactive data visualizations** (charts, word clouds, etc.)
- Use the **sidebar filters** to interactively explore the data

---

### 🔧 Features

- Free-text search for any product/topic on Product Hunt
- Automated data extraction via Selenium
- Display results in a searchable, scrollable table
- Visualize trends and key metrics (e.g., rating distribution, top-rated apps, free vs paid)
- Sidebar filters for refined visual analysis
- Organized **multi-page layout** using Streamlit's navigation

---

### ▶️ How to Use the App

1. Go to the **"Results Table"** page.
2. Enter any **search term** of your choice (e.g., “productivity”, “AI tools”, “design”, etc.).
3. View the results in a structured data table.
4. Then head to the **"Visualizations"** page to explore charts based on the results.
5. Use the **sidebar filters** to focus on specific apps or metrics.

---

### 📈 Technologies Used

- **Python**, **Streamlit** for the web interface
- **Selenium** for real-time data scraping
- **Pandas**, **Matplotlib**, **Seaborn**, **WordCloud** for data processing and visualization
- **Session State** to share data between pages

---

### 🚀 Future Improvements

- Add a search history feature
- Allow users to download results as CSV
- Integrate more data sources beyond Product Hunt
- Include a detailed app view with screenshots or external links

---
""")
