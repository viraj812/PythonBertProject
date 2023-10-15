from bert_processing import bert_predict_
from text_to_speech import speak_, speech_to_text_
from PyPDF2 import PdfReader

def getContext():
    reader = PdfReader("book.pdf")
    # page = reader.pages[0]
    page = [i.extract_text() for i in reader.pages]
    page = [i.replace("\n", "") for i in page]
    text = ""

    for line in page:
        text += line
    # print(text)
    return text

def main():
    book = open("book.txt", 'r', encoding='utf-8').readlines()
    text = ""

    for line in book:
        text += line
    # question = speech_to_text_()
    question = "what is an algorithm?"
    output = bert_predict_(question, text)
    speak_(output)


# getContext("hello")

if __name__ == '__main__':
    main()
