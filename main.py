import nltk
from data_cleaning import clean_text
from split_data import split_tweets
from sentiment_analysis import analyze_sentiment, random_sample
from visualization import visualize_sentiment

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')


# ---------------------------------------------
# Twitter Scrapper
# ---------------------------------------------

# def scrape_tweets(query, max_tweets, filename):
#     tweets_list = []
#     # Use snscrape to scrape tweets
#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
#         if i >= max_tweets:
#             break
#         tweets_list.append({
#             "user": tweet.user.username,
#             "text": tweet.content,
#             "date": tweet.date
#         })
    
#     # Save tweets to a CSV file
#     df = pd.DataFrame(tweets_list)
#     df.to_csv(filename, index=False)
#     print(f"Saved {len(tweets_list)} tweets to {filename}")

# if __name__ == "__main__":
#     # Scrape tweets about Donald Trump
#     scrape_tweets("Donald Trump", max_tweets=500, filename="donald_trump_tweets.csv")

#     # Scrape tweets about Kamala Harris
#     scrape_tweets("Kamala Harris", max_tweets=500, filename="kamala_harris_tweets.csv")




# File paths and configuration
input_file = 'raw_data.csv'
output_bjp_file = 'bjp.csv'
output_congress_file = 'congress.csv'
tweet_column = 'text'

# Step 1: Split tweets
if split_tweets(input_file, tweet_column, output_bjp_file, output_congress_file):
    # Step 2: Perform sentiment analysis
    bjp_reviews = analyze_sentiment(output_bjp_file)
    congress_reviews = analyze_sentiment(output_congress_file)

    # Step 3: Random sampling
    bjp_subset = random_sample(bjp_reviews, 324)
    congress_subset = random_sample(congress_reviews, 31)

    # Step 4: Visualization
    visualize_sentiment(bjp_subset, congress_subset)
