# Program Author: Brandon Bayquen
# Resource: https://huggingface.co/blog/sentiment-analysis-python#1-what-is-sentiment-analysis
import torch
from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import DataCollatorWithPadding
from transformers import AutoModelForSequenceClassification
import numpy as np
from datasets import load_metric
from huggingface_hub import login       # Don't use notebook_login, since we're not on Google Colab...
from transformers import TrainingArguments, Trainer
from transformers import pipeline

# 1. Activate GPU and Install Dependencies
# Check if GPU is available for training models:
print("GPU Hardware accelerator available?:", torch.cuda.is_available())

# 2. Preprocess data
imdb = load_dataset("imdb")

# Since IMDB is a very huge dataset, we'll create smaller, split train and test datasets
# for our neural network:
small_train_dataset = imdb["train"].shuffle(seed=42).select([i for i in list(range(3000))])
small_test_dataset = imdb["test"].shuffle(seed=42).select([i for i in list(range(3000))])

# To preprocess our data, we use DistilBERT tokenizer:
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Next, let's prepare the text inputs for the model for both splits of our dataset by
# using the map method:
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)

tokenized_train = small_train_dataset.map(preprocess_function, batched=True)
tokenized_test = small_test_dataset.map(preprocess_function, batched=True)

# To speed up training, let's use a data_collator to convert your training samples
# to PyTorch tensors and concatenate them with the correct amount of padding:
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# 3. Training the model
# You will be throwing away the pretraining head of the DistilBERT model and
# replacing it with a classification head fine-tuned for sentiment analysis.
# This enables you to transfer the knowledge from DistilBERT to your custom model

# For training, you will be using the Trainer API, which is optimized for
# fine-tuning Transformers models such as DistilBERT, BERT and RoBERTa.
# First, let's define DistilBERT as your base model:
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# Then, let's define the metrics you will be using to evaluate how good is your
# fine-tuned model (accuracy and f1 score):
def compute_metrics(eval_predictions):
    load_accuracy = load_metric("accuracy")
    load_f1 = load_metric("f1")

    logits, labels = eval_predictions
    predictions = np.argmax(logits, axis=-1)
    accuracy = load_accuracy.compute(predictions=predictions, references=labels)["accuracy"]
    f1 = load_f1.compute(predictions=predictions, references=labels)["f1"]
    return {"accuracy": accuracy, "f1": f1}     # Recall: Python dictionary

# Next, let's login to your Hugging Face account so you can manage your
# model repositories. You'll need to add your Hugging Face token as a string arg:
login("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")

# Before training our model, you need to define the training arguments
# and define a Trainer with all the objects you constructed up to this point:
repo_name = "finetuning-sentiment-model-3000-samples"

training_args = TrainingArguments(
    output_dir=repo_name,
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
    weight_decay=0.01,
    save_strategy="epoch",
    push_to_hub=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_test,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics
)

# Now, it's time to fine-tune the model on the sentiment analysis dataset:
trainer.train()
# And voila! You fine-tuned a DistilBERT model for sentiment analysis!
# [NOTE: Training time depends on the hardware you use and the number of samples in the
# dataset. In our case, it took almost 10 minutes using a GPU and fine-tuning
# the model with 3,000 samples. The more samples you use for training your model,
# the more accurate it will be but training could be significantly slower.]

# Next, let's compute the evaluation metrics to see how good your model is:
trainer.evaluate()

# 4. Analyzing new data with the model
# Now that you have trained a model for sentiment analysis, let's use it to analyze
# new data and get predictions! This unlocks the power of machine learning;
# using a model to automatically analyze data at scale, in real-time

# First, let's upload the model to the Hub:
trainer.push_to_hub()

# Now you can use the pipeline class to analyze two new movie reviews and see how your
# model predicts its sentiment.

# Run inferences with your new model using Pipeline:
sentiment_model = pipeline(model="nightlyfade/finetuning-sentiment-model-3000-samples")
sentiment_model(["I love this movie", "This movie sucks!"])

# (Note: In the IMDB dataset, Label 1 means positive and Label 0 is negative.)