import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import nltk
from tqdm import tqdm

nltk.download("stopwords")
nltk.download("wordnet")

df = pd.read_csv("cleaned_data.csv", header=None, names=["Review", "Star Rating"])
tqdm.pandas(desc="Processing")
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Convert text to lowercase, remove punctuation, special characters, stopwords, and lemmatization
df["Review"] = df["Review"].str.lower()
df["Review"] = df["Review"].progress_apply(lambda x: re.sub(r"[^\w\s]", "", x))
df["Review"] = df["Review"].progress_apply(lambda x: " ".join([word for word in x.split() if word not in stop_words]))
df["Review"] = df["Review"].progress_apply(lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split()]))

# additional features
df["Sentiment"] = df["Review"].apply(lambda x: TextBlob(x).sentiment.polarity)
df["Word Count"] = df["Review"].progress_apply(lambda x: len(x.split()))
df["Character Count"] = df["Review"].progress_apply(lambda x: len(x))

df = df[["Review", "Word Count", "Character Count", "Sentiment", "Star Rating"]]
df.to_csv("preprocessed_2.csv", index=False)
print("Text preprocessing complete. Processed dataset saved as 'preprocessed_2.csv'.")
