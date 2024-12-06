import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def cleaning_URLs(data):
    """Remove URLs from text."""
    return re.sub(r'((www.[^\s]+)|(https?://[^\s]+))', ' ', data)

def cleaning_numbers(data):
    """Remove numbers from text."""
    return re.sub(r'\d+', '', data)

def remove_pattern(input_txt, pattern):
    """Remove a specific pattern (e.g., Twitter handles) from text."""
    r = re.findall(pattern, input_txt)
    for word in r:
        input_txt = re.sub(word, '', input_txt)
    return input_txt

def remove_stopwords(text):
    """Remove common stopwords from text for better analysis."""
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return ' '.join(word for word in words if word.lower() not in stop_words)

def clean_text(dataframe, text_column):
    """Apply all cleaning functions to the text column."""
    dataframe[text_column] = dataframe[text_column].apply(cleaning_URLs)
    dataframe[text_column] = dataframe[text_column].apply(cleaning_numbers)
    dataframe[text_column] = dataframe[text_column].apply(lambda x: remove_pattern(x, "@[\w]*"))
    dataframe[text_column] = dataframe[text_column].str.replace("[^a-zA-Z#]", " ", regex=True)
    dataframe[text_column] = dataframe[text_column].apply(remove_stopwords)
    return dataframe
