from keybert import KeyBERT
class Keyword:
    def __init__(self):
        self.model = KeyBERT('xlm-r-distilroberta-base-paraphrase-v1')
        self.textInput = ""
    def setInput(self, textInput):
        self.textInput = textInput
    def getKeyword(self):
        keyword = self.model.extract_keywords(self.textInput, keyphrase_ngram_range=(1, 2), stop_words=None)
        return keyword


