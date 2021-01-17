from transformers import pipeline
summarizer = pipeline("summarization")

textInput = input()

print(summarizer(textInput, max_length=450, min_length=30, do_sample=False)[0]["summary_text"])