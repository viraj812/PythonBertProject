from bert_processing import bert_predict_
from text_to_speech import speak_, speech_to_text_
from PyPDF2 import PdfReader
from gensim.summarization import summarize

def getContext():
    reader = PdfReader("../static/progit.pdf")
    # page = reader.pages[0]
    page = [i.extract_text() for i in reader.pages]
    page = [i.replace("\n", " ") for i in page]
    text = ""

    for line in page:
        text += line
    # print(text)

    text = summarize(text, ratio=0.25)
    return text

def main():
    text = getContext()
    # print(text)
    question = "what is version control?"
    output = bert_predict_(question, text)
    speak_(output)

if __name__ == '__main__':
    main()
