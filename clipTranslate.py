import time
import argparse
from googletrans import Translator, LANGUAGES
import pyperclip as clipboard

def validate_languages(src_lang, target_lang):
    if src_lang not in LANGUAGES.keys():
        raise ValueError(f"Unsupported source language: {src_lang}. Supported languages are: {', '.join(LANGUAGES.keys())}")
    if target_lang not in LANGUAGES.keys():
        raise ValueError(f"Unsupported target language: {target_lang}. Supported languages are: {', '.join(LANGUAGES.keys())}")

def translate_clipboard(src_lang='es', target_lang='en'):
    translator = Translator()
    previous_text = ""
    cache = {}

    try:
        validate_languages(src_lang, target_lang)

        while True:
            text = clipboard.paste()
            if text != previous_text and text:
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

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Translation stopped by user.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("Cannot translate text:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Translate text from clipboard.')
    parser.add_argument('--source', '-s', default='es', help='Source language (default: es)')
    parser.add_argument('--target', '-t', default='en', help='Target language (default: en)')

    args = parser.parse_args()
    translate_clipboard(src_lang=args.source, target_lang=args.target)
