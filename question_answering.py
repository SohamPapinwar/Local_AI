from transformers import BertForQuestionAnswering, BertTokenizer
import torch

def answer_question(question, text):
    # Load pre-trained BERT model and tokenizer from local directory
    model_dir = "bert-base-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_dir)
    model = BertForQuestionAnswering.from_pretrained(model_dir)

    # Tokenize inputs
    inputs = tokenizer.encode_plus(question, text, return_tensors="pt", max_length=512, truncation=True)

    # Perform inference
    outputs = model(**inputs)

    # Get the start and end scores
    start_scores = outputs.start_logits
    end_scores = outputs.end_logits

    # Get the most likely answer
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores)
    answer_tokens = inputs["input_ids"][0][start_index:end_index+1]
    answer = tokenizer.decode(answer_tokens)

    return answer