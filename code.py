from translate import Translator
From_Lan = input("Input the language to be translated: ")
To_Lan = input("Enter the language in which to wanted to get the translate: ")
translator = Translator ( From_lang = f"{From_Lan}" , to_lang = f"{To_Lan}")
line = input("Enter the Line: ")
result = translator.translate(f'{line}')
print(result)
