from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
from transformers import pipeline
from typing import List, Dict

def search_producthunt(search_term: str) -> pd.DataFrame:
    """
    Performs a Product Hunt search using Selenium and returns a DataFrame with results.
    
    Args:
        search_term (str): The search query input by the user.
        
    Returns:
        pd.DataFrame: A dataframe containing product name, tagline, rating, and review count.
    """
    # Setup browser options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    
    # Path to your ChromeDriver
    #service = Service(r"C:\Users\Brandly\chromedriver-win64\chromedriver.exe")
    #browser = webdriver.Chrome(service=service, options=options)
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    
    # Format search URL
    query = search_term.replace(" ", "%20")
    url = f"https://www.producthunt.com/search?q={query}"
    browser.get(url)

    # Wait for results to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test^="spotlight-result-product"]'))
        )
    except Exception as e:
        print("Loading error:", e)

    # Scroll to load more results
    for _ in range(3):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Extract product info
    products = []
    items = browser.find_elements(By.CSS_SELECTOR, 'button[data-test^="spotlight-result-product"]')
    
    for item in items:
        try:
            name = item.find_element(By.CSS_SELECTOR, 'div[class*="text-16"]').text
            tagline = item.find_element(By.CSS_SELECTOR, 'div[class*="text-14"]').text
            stars = len(item.find_elements(By.CSS_SELECTOR, 'div[data-sentry-component="StarRating"] svg'))
            review_element = item.find_elements(By.CSS_SELECTOR, 'div.text-14.font-semibold.text-brand-500')
            review_count = review_element[0].text if review_element else "0"
            
            products.append({
                "Name": name,
                "Tagline": tagline,
                "Rating": stars,
                "Review Count": review_count
            })

        except Exception as e:
            print("Error during extraction:", e)

    browser.quit()
    
    return pd.DataFrame(products)


# Pipeline pour l'analyse de sentiment
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sample_reviews(app_name: str) -> List[str]:
    """
    Retourne un échantillon de faux avis d’utilisateurs.
    Remplace cette fonction par un appel API réel si possible.
    """
    return [
        f"{app_name} is amazing! Totally loved it!",
        f"I found {app_name} useful, but has some bugs.",
        f"{app_name} is terrible. Waste of time.",
    ]

def compute_sentiments(reviews: List[str]) -> List[Dict]:
    """
    Applique le modèle Hugging Face sur chaque avis.
    """
    return sentiment_pipeline(reviews)

def compute_app_sentiment_score(results: List[Dict]) -> Dict[str, float]:
    """
    Calcule les scores globaux pour une app.
    """
    counts = {"POSITIVE": 0, "NEGATIVE": 0}
    for r in results:
        label = r["label"].upper()
        if label in counts:
            counts[label] += 1
    total = sum(counts.values())
    return {
        "Positive": counts["POSITIVE"] / total if total else 0,
        "Negative": counts["NEGATIVE"] / total if total else 0,
    }
