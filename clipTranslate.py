import time
from googletrans import Translator
import pyperclip as clipboard

cache = {}


def translate_clipboard(src_lang='es', target_lang='en'):
    translator = Translator()
    previous_text = ""

    while True:
        text = clipboard.paste()

        if text != previous_text and text:
            try:

                if text in cache:
                    translated_text = cache[text]
                    cached = True
                else:
                    translated = translator.translate(text.strip(), src=src_lang, dest=target_lang)
                    translated_text = translated.text.strip()
                    cache[text] = translated_text
                    cached = False

                clipboard.copy(translated_text)

                print(f'[cache={cached}] Translated: "{translated_text}"')
                previous_text = translated_text
            except Exception as e:
                print("Cannot translate text:", e)

        time.sleep(0.1)


if __name__ == "__main__":
    translate_clipboard()
