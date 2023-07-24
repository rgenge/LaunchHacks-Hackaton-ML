# Resource: https://huggingface.co/blog/sentiment-analysis-python#1-what-is-sentiment-analysis
from transformers import pipeline

# This code snippet uses the pipeline class to make predictions
# from models available in the Hub. It uses the default model for
# sentiment analysis to analyze the list of texts called data:
sentiment_pipeline = pipeline(model="nightlyfade/finetuning-sentiment-model-3000-samples")
data = ["I love this movie", "This movie sucks!"]
sentiment_pipeline(data)

