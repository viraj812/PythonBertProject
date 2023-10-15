from transformers import pipeline

def bert_predict_(question, context):

    model = pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad')
    output = model(question, context)

    print(output['answer'])

    return output['answer']
