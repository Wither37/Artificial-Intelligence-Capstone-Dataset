# Dataset

We collected movie reviews from IMDb, an online database of movie information, by scraping reviews from 100 randomly selected movies. The dataset consists of 9702 entries, each containing a review (string) and a star rating (integer, ranging from 1 to 10). Two versions of the preprocessed dataset were created: one with only reviews and ratings, designed primarily for deep learning methods, and another with additional features—word count (integer), character count (integer), and sentiment polarity (float)—intended for feature-based models.

## Data Type

The raw dataset includes reviews as strings (textual data) and star ratings as integers (1 to 10). The preprocessed dataset with additional features includes the following columns: "Review" (string), "Word Count" (integer, number of words in the review), "Character Count" (integer, total number of characters including spaces), "Sentiment" (float, sentiment polarity ranging from -1 to 1), and "Star Rating" (integer).

## External Source

The data was sourced from IMDb ([https://www.imdb.com/](https://www.imdb.com/)), specifically from the review pages of 100 randomly selected movies.

## Amount and Composition

The dataset contains 9702 entries collected from 100 movies, with a maximum of 100 reviews per movie. The exact number of reviews per movie may vary (up to 100) depending on availability. The raw dataset consists of two columns: "Review" (text of the review) and "Star Rating" (rating from 1 to 10). The preprocessed dataset with additional features includes five columns: "Review", "Word Count", "Character Count", "Sentiment", and "Star Rating".

## Conditions for Data Collection

The primary conditions were that each review must contain both text and a corresponding star rating. A maximum limit of 100 reviews per movie was set to ensure manageable data collection. No additional constraints were imposed on review length, language (assumed to be English based on IMDb’s primary user base), or content, allowing for a diverse set of reviews as long as they met the basic requirement of having text and a rating.

## Process of Data Collection

### Scraping

Data collection was performed using a Python script leveraging the Selenium library with Chrome WebDriver. Movie IDs were read from an input CSV file (`movie.csv`), which contained a list of IMDb movie identifiers (e.g., "tt1234567"). For each movie, the script constructed the URL `https://www.imdb.com/title/{movie_id}/reviews`, accessed the page, and clicked the "See More" button (identified by the class "ipc-see-more__button") to load all available reviews. After a 3-second delay to ensure the page loaded fully, the script scraped review text (from elements with class "ipc-html-content-inner-div") and star ratings (from elements with class "ipc-rating-star--rating"), collecting up to 100 reviews per movie. The data was saved to `data.csv` with columns "Review" and "Star Rating". The scraping process was executed on a standard computer with Chrome installed, and additional libraries used included pandas for data handling.

### Preprocessing

The raw data (renamed to `cleaned_data.csv`) was preprocessed using a separate Python script. The preprocessing steps included:

1. Converting reviews to lowercase.
2. Removing punctuation and special characters using regular expressions (re library).
3. Removing stop words using NLTK’s English stop words list.
4. Lemmatizing words using NLTK’s WordNetLemmatizer.

Additional features were computed:

- Sentiment polarity using TextBlob’s sentiment analysis (ranging from -1 to 1).
- Word count as the number of words in the preprocessed review.
- Character count as the total number of characters (including spaces) in the preprocessed review.

The processed data was saved to `preprocessed_2.csv` with columns "Review", "Word Count", "Character Count", "Sentiment", and "Star Rating". This preprocessing was also performed on a standard computer, utilizing libraries such as pandas, re, NLTK (stopwords and WordNetLemmatizer), TextBlob, and tqdm for progress tracking.

## Hardware and Software

The data collection and preprocessing were conducted on a standard computer equipped with Chrome for Selenium scraping. Software tools included:

- Python 3.x
- Selenium with Chrome WebDriver (for scraping)
- pandas (data manipulation)
- re (regular expressions)
- NLTK (stop words and lemmatization)
- TextBlob (sentiment analysis)
- tqdm (progress tracking)

## Examples

- **Raw Data**: ["The Shawshank Redemption has great performances, extremely well written script and story all leading to a deeply emotional climax! One of the best dramas of all time!",10]
- **Preprocessed Data (without extra features)**: [shawshank redemption great performance extremely well written script story leading deeply emotional climax one best drama time,10]
- **Preprocessed Data (with extra features)**: [shawshank redemption great performance extremely well written script story leading deeply emotional climax one best drama time,17,126,0.41875,10]