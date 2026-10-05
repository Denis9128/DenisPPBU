from googletrans import Translator, LANGUAGES

translator = Translator()
t_text = translator.translate('hello', src='en', dest='ru')

print(t_text)