import argparse
import os
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

# Parse input arguments from SageMaker
parser = argparse.ArgumentParser()
parser.add_argument("--train", type=str, default="/opt/ml/input/data/train")
parser.add_argument("--model-dir", type=str, default="/opt/ml/model")
args = parser.parse_args()

# Load dataset from S3
dataset = load_dataset("csv", data_files={"train": os.path.join(args.train, "train.csv")})["train"]

# Define labels
label_list = ["Telecommunications", "Energy", "Others", "Complaints", "Invoice", "Suggestion", "Package"]
num_labels = len(label_list)

# Load tokenizer & model
model_name = "microsoft/deberta-v3-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

# Tokenize dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

dataset = dataset.map(tokenize_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir=args.model_dir,
    evaluation_strategy="epoch",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=5,
    save_steps=500,
    save_total_limit=2,
)

# Train the model
trainer = Trainer(model=model, args=training_args, train_dataset=dataset)
trainer.train()

# Save the model
trainer.save_model(args.model_dir)
tokenizer.save_pretrained(args.model_dir)
