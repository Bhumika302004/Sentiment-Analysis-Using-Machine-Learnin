import pandas as pd

def split_tweets(input_file, tweet_column, output_bjp_file, output_congress_file):
    """Split the dataset into BJP and Congress tweets and save them as separate files."""
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        return False

    if tweet_column not in df.columns:
        print(f"Error: The column '{tweet_column}' is not found in the dataset.")
        return False

    bjp_tweets = df[df[tweet_column].str.contains('BJP', case=False, na=False)]
    congress_tweets = df[df[tweet_column].str.contains('Congress', case=False, na=False)]

    bjp_tweets.to_csv(output_bjp_file, index=False)
    congress_tweets.to_csv(output_congress_file, index=False)

    print(f"BJP tweets saved to {output_bjp_file}")
    print(f"Congress tweets saved to {output_congress_file}")
    return True
