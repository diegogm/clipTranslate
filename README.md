# Clip Translate

This Python application automatically translates text copied to the clipboard using the Google Translate API. The script continuously monitors the clipboard content, performs the translation if the text changes, and updates the clipboard with the translated text.

## Features

* **Automatic Translation**: Detects when new text is copied to the clipboard and automatically translates it.
* **Caching Mechanism**: Saves recently translated phrases to avoid redundant translations and enhance performance.

## Prerequisites

Before you start using Clipboard Translator, ensure you have Python installed on your system. To install them using pip:

```bash
pip install -r requirements.txt 
```

## Usage
To run the script, navigate to the directory containing translate_clipboard.py and execute the following command in the terminal:

```bash
python translate_clipboard.py --source [source_language_code] --target [target_language_code]
```

Replace [source_language_code] and [target_language_code] with the desired ISO language codes to customize the translation languages.

## Configuration

The default source language is Spanish (es), and the target language is English (en). Modify these settings by passing the desired language codes as arguments when running the script, as shown in the Usage section.

## License
This project is open-sourced under the BSD license. See the LICENSE file for more details.

## Contributing
Contributions to Clipboard Translator are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## Disclaimer
This software uses the googletrans library, which relies on Google Translate's unofficial API. The functionality might break if there are changes on Google's end.

## Contact
If you have any questions or feedback, please open an issue in the project repository.
