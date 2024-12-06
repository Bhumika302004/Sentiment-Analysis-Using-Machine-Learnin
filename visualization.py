import plotly.graph_objects as go

def visualize_sentiment(bjp_data, congress_data):
    """Visualize sentiment analysis results."""
    count_bjp = bjp_data.groupby("Expression Label")["text"].count()
    count_congress = congress_data.groupby("Expression Label")["text"].count()

    total_bjp = len(bjp_data)
    total_congress = len(congress_data)

    negative_per_bjp = (count_bjp.get("negative", 0) / total_bjp) * 100
    positive_per_bjp = (count_bjp.get("positive", 0) / total_bjp) * 100

    negative_per_congress = (count_congress.get("negative", 0) / total_congress) * 100
    positive_per_congress = (count_congress.get("positive", 0) / total_congress) * 100

    Politicians = ["Congress", "BJP"]
    lis_pos = [positive_per_congress, positive_per_bjp]
    lis_neg = [negative_per_congress, negative_per_bjp]

    fig = go.Figure(data=[
        go.Bar(name="Positive", x=Politicians, y=lis_pos),
        go.Bar(name="Negative", x=Politicians, y=lis_neg)
    ])

    fig.update_layout(barmode="group", title="Sentiment Analysis of BJP and Congress Tweets")
    fig.show()
