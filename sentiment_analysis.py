import pandas as pd
import numpy as np
from textblob import TextBlob

def find_pol(review):
    """Calculate sentiment polarity using TextBlob."""
    return TextBlob(review).sentiment.polarity

def analyze_sentiment(file_path):
    """Perform sentiment analysis on tweets from a given file."""
    df = pd.read_csv(file_path)

    df["Sentiment Polarity"] = df["text"].apply(find_pol)
    df["Expression Label"] = np.where(
        df["Sentiment Polarity"] > 0, "positive", "negative"
    )
    df.loc[df["Sentiment Polarity"] == 0, "Expression Label"] = "Neutral"

    df = df[df["Sentiment Polarity"] != 0.0]
    return df

def random_sample(df, remove_n, seed=10):
    """Randomly sample rows from the dataset."""
    np.random.seed(seed)
    drop_indices = np.random.choice(df.index, remove_n, replace=False)
    return df.drop(drop_indices)
