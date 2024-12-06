# Sentiment-Analysis-Using-Machine-Learning
Abstract :
This project explores the use of sentiment analysis, a 
subset of natural language processing (NLP), to gauge 
public opinion on two major Indian political parties: BJP 
and Congress. Using machine learning tools and pre
collected tweets, the project classifies sentiments into 
positive and negative categories. The results provide 
insights into political trends, public perceptions, and 
possible factors influencing these sentiments. The 
analysis highlights the utility of machine learning in 
understanding social media dynamics in political 
discourse. 
1.Introduction 
The rapid adoption of social media has provided a rich 
source of real-time data on public opinion, especially 
regarding politics. Platforms like Twitter serve as a 
global stage where users share their thoughts on 
political events, leaders, and campaigns. Sentiment 
analysis leverages NLP techniques to quantify these 
opinions, making it an essential tool for political 
strategists, researchers, and policymakers. 
This project specifically focuses on tweets mentioning 
BJP and Congress. By analyzing the sentiments 
expressed in these tweets, we aim to answer the 
following questions: 
1. What is the overall public sentiment towards each 
party? 
2. How do positive and negative sentiments 
compare? 
3. Can this analysis provide actionable insights for 
political campaigns? 
Fig1. Word Cloud  
2. Literature Review 
Sentiment analysis has been extensively studied in the 
context of political analysis. Studies have shown that 
the sentiment polarity of tweets can predict electoral 
outcomes with a reasonable degree of accuracy. For 
instance, researchers have used social media data 
during the 2016 US elections and India's 2014 elections 
to study public opinion. 
The literature also highlights key challenges, including 
the handling of noisy text, sarcasm, and the dynamic 
nature of language on social media. Recent 
advancements, such as the use of transformers like 
BERT, have significantly improved sentiment 
classification accuracy. However, simpler models like 
TextBlob still remain effective for basic sentiment tasks 
due to their ease of use and interpretability. 

4.Proposed Solution/Algorithm 
This project employs a structured pipeline for 
sentiment analysis, involving data cleaning, sentiment 
computation, sampling, and visualization. 
Data Cleaning 
To ensure accurate sentiment classification, the tweets 
were cleaned using the following methods: 
1. URL Removal: URLs were removed using regular 
expressions to eliminate irrelevant content. 
2. Stopword Removal: Common English stopwords, 
such as "and," "the," and "is," were filtered out 
using NLTK. 
3. Special Character Removal: Non-alphanumeric 
characters were removed to standardize the text. 
4. Lowercasing: Text was converted to lowercase for 
consistency. 
Flowchart 
Sentiment Analysis 
TextBlob was used to calculate the sentiment polarity 
of each tweet, assigning a score between -1 (negative 
sentiment) and 1 (positive sentiment). Tweets were 
then categorized into: 
• 
• 
Positive Sentiments: Polarity > 0 
Negative Sentiments: Polarity < 0 
Random Sampling 
To address imbalances in the dataset, random sampling 
was applied to ensure that the sentiment distribution 
was representative of the overall data. 
Visualization 
The processed data was visualized using Plotly, 
presenting the proportion of positive and negative 
sentiments for both BJP and Congress in a grouped bar 
chart. 


Strengths: 
Ease of Implementation: The use of TextBlob 
provided a quick and reliable sentiment analysis 
pipeline. 

Visualization: Plotly enabled clear and interactive 
presentation of the results, making insights 
accessible to non-technical audiences. 
Challenges: 
Dataset Limitations: The inability to scrape live 
tweets limited the scope of analysis to pre-existing 
data, potentially missing recent trends or events. 

Sarcasm Detection: The model struggled with 
identifying sarcasm, a common challenge in 
sentiment analysis. 
Neutral Sentiments: Neutral tweets were excluded, 
which might have provided additional context to 
the analysis. 
7. Conclusion 
This project demonstrates the potential of sentiment 
analysis in understanding public opinion about political 
parties. The results indicate that while both BJP and 
Congress enjoy significant positive sentiments on 
Twitter, there is also notable criticism for each. 
Future work can address the following: 
1. Advanced Models: Incorporate deep learning 
models like BERT for improved accuracy. 
2. Real-Time Data: Re-enable Twitter scraping for 
real-time sentiment tracking. 
3. Multilingual Support: Extend analysis to include 
tweets in regional languages to capture a broader 
audience. 
Despite its limitations, this project highlights the 
importance of social media analysis in political research 
and opens avenues for further exploration. 
