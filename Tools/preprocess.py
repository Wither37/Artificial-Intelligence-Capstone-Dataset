import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import nltk
from tqdm import tqdm

# Ensure necessary resources are downloaded
nltk.download("stopwords")
nltk.download("wordnet")

# Load the dataset
df = pd.read_csv("cleaned_data.csv", header=None, names=["Review", "Star Rating"])

# Initialize tqdm for progress tracking
tqdm.pandas(desc="Processing")

# Convert text to lowercase
df["Review"] = df["Review"].str.lower()

# Remove punctuation and special characters
df["Review"] = df["Review"].progress_apply(lambda x: re.sub(r"[^\w\s]", "", x))

# Remove stopwords
stop_words = set(stopwords.words("english"))
df["Review"] = df["Review"].progress_apply(lambda x: " ".join([word for word in x.split() if word not in stop_words]))

# Lemmatization
lemmatizer = WordNetLemmatizer()
df["Review"] = df["Review"].progress_apply(lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split()]))

# Add Sentiment Score
df["Sentiment"] = df["Review"].apply(lambda x: TextBlob(x).sentiment.polarity)

# Add Word Count
df["Word Count"] = df["Review"].progress_apply(lambda x: len(x.split()))

# Add Character Count
df["Character Count"] = df["Review"].progress_apply(lambda x: len(x))

# Reorder columns to move 'Star Rating' to the last
df = df[["Review", "Word Count", "Character Count", "Sentiment", "Star Rating"]]

# Save the preprocessed dataset
df.to_csv("preprocessed_2.csv", index=False)

print("Text preprocessing complete. Processed dataset saved as 'preprocessed_2.csv'.")
