from deep_translator import GoogleTranslator

def translate_(text, src, target):
    translator = GoogleTranslator(src=src, target=target)
    translated_text = translator.translate(text)
    print(translated_text)
    return translated_text