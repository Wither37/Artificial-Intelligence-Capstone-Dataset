from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

def scrape_imdb_reviews_selenium(movie_url, max_reviews=100):
    driver = webdriver.Chrome()
    driver.get(movie_url)
    try:
        all_button = driver.find_element(By.CLASS_NAME, "ipc-see-more__button")
        ActionChains(driver).move_to_element(all_button).click().perform()
        time.sleep(3)
    except Exception as e:
        print("Could not find or click the 'All' button:", e)
    
    reviews = []

    while len(reviews) < max_reviews:
        review_elements = driver.find_elements(By.CLASS_NAME, "ipc-html-content-inner-div")
        star_elements = driver.find_elements(By.CLASS_NAME, "ipc-rating-star--rating")
        for review, star in zip(review_elements, star_elements):
            if len(reviews) >= max_reviews:
                break
            full_review = " ".join(review.text.splitlines())
            reviews.append({"Review": full_review, "Star Rating": star.text.strip()})
    driver.quit()
    return pd.DataFrame(reviews)

def scrape_reviews_for_movies(input_csv, output_csv, max_reviews=100):
    movie_ids = pd.read_csv(input_csv)['movie_id'].tolist()
    all_reviews = []
    for movie_id in movie_ids:
        print(f"Scraping reviews for movie: {movie_id}")
        movie_url = f"https://www.imdb.com/title/{movie_id}/reviews"
        reviews_df = scrape_imdb_reviews_selenium(movie_url, max_reviews)
        reviews_df = reviews_df[["Review", "Star Rating"]]       
        all_reviews.append(reviews_df)
        all_reviews_df = pd.concat(all_reviews, ignore_index=True)
        all_reviews_df.to_csv(output_csv, index=False)
        
    final_df = pd.concat(all_reviews, ignore_index=True)
    final_df.to_csv(output_csv, index=False)
    print(f"All reviews saved to {output_csv}")

input_csv = "movie.csv"
output_csv = "data.csv"
scrape_reviews_for_movies(input_csv, output_csv, max_reviews=100)