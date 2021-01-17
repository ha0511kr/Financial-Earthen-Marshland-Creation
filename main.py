from keywordExtractor import Keyword
from SummariseText_Transformers_import import SummariseText
from wikipediascrape import Wikipedia


def main():
    #wiki = Wikipedia()
    #text = wiki.getFullArticle("Google")
    text = "Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs. It infers a function from labeled training data consisting of a set of training examples."
    sum_t = SummariseText()
    sum_t.setInput(text)
    summ = sum_t.getSummary()
    print(summ)

    key_w = Keyword()
    key_w.setInput(summ)
    list_key = key_w.getKeyword()

    print(list_key)


if __name__ == "__main__":
    main()
