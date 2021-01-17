from transformers import pipeline


class SummariseText:
    def __init__(self):
        self.summarizer = pipeline("summarization")
        self.text = ""

    def setInput(self, textInput):
        self.text = textInput

    def getSummary(self):
        return self.summarizer(self.text, max_length=450, min_length=30, do_sample=False)[0]["summary_text"]
