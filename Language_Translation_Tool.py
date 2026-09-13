import urllib.parse
import urllib.request
import json
import re


# ---------------------------------------------------------
# Translation API
# ---------------------------------------------------------
def translate_text(text, source_lang, target_lang):
    encoded_text = urllib.parse.quote(text)

    url = (
        "https://api.mymemory.translated.net/get?"
        f"q={encoded_text}&langpair={source_lang}|{target_lang}"
    )

    try:
        with urllib.request.urlopen(url, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))

        if data.get("responseStatus") == 200:
            return data["responseData"]["translatedText"]

        return "Translation failed."

    except Exception as e:
        return f"Error: {e}"


# ---------------------------------------------------------
# Protect Names / Proper Names
# ---------------------------------------------------------
def protect_names(text):
    protected_names = {}

    # Detect words beginning with a capital letter.
    # Example: Renish, John, London
    words = re.findall(r"\b[A-Z][a-zA-Z]+\b", text)

    # Common English words that should NOT be treated as names
    common_words = {
        "I", "Am", "Is", "Are", "The", "This", "That",
        "He", "She", "We", "They", "You", "My", "Your",
        "Hello", "How", "What", "Where", "When", "Why",
        "Good", "Morning", "Evening", "Night"
    }

    for index, word in enumerate(words):
        if word not in common_words:
            placeholder = f"ZXQNAME{index}ZXQ"
            protected_names[placeholder] = word
            text = re.sub(r"\b" + re.escape(word) + r"\b",
                          placeholder, text)

    return text, protected_names


# ---------------------------------------------------------
# Restore Names
# ---------------------------------------------------------
def restore_names(translated_text, protected_names):
    for placeholder, name in protected_names.items():

        # API may modify placeholder capitalization
        variations = [
            placeholder,
            placeholder.lower(),
            placeholder.upper(),
            placeholder.capitalize()
        ]

        for variation in variations:
            translated_text = translated_text.replace(
                variation, name
            )

    return translated_text


# ---------------------------------------------------------
# Special handling for "I am [Name]"
# ---------------------------------------------------------
def translate_with_name_protection(text, source_lang, target_lang):

    protected_text, protected_names = protect_names(text)

    translated_text = translate_text(
        protected_text,
        source_lang,
        target_lang
    )

    translated_text = restore_names(
        translated_text,
        protected_names
    )

    return translated_text


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
def main():

    print("=" * 60)
    print("             LANGUAGE TRANSLATION TOOL")
    print("=" * 60)

    languages = {
        "1": ("English", "en"),
        "2": ("Gujarati", "gu"),
        "3": ("Hindi", "hi"),
        "4": ("Spanish", "es"),
        "5": ("French", "fr"),
        "6": ("German", "de"),
        "7": ("Italian", "it"),
        "8": ("Portuguese", "pt"),
        "9": ("Japanese", "ja"),
        "10": ("Korean", "ko")
    }

    print("\nAvailable Languages:")

    for key, value in languages.items():
        print(f"{key}. {value[0]}")

    source_choice = input("\nSelect Source Language: ")
    target_choice = input("Select Target Language: ")

    if source_choice not in languages:
        print("\nInvalid source language.")
        return

    if target_choice not in languages:
        print("\nInvalid target language.")
        return

    text = input("\nEnter text to translate: ")

    if not text.strip():
        print("\nPlease enter some text.")
        return

    source_name, source_code = languages[source_choice]
    target_name, target_code = languages[target_choice]

    print("\nTranslating...")

    result = translate_with_name_protection(
        text,
        source_code,
        target_code
    )

    print("\n" + "=" * 60)
    print("                 TRANSLATION RESULT")
    print("=" * 60)

    print(f"Original Text   : {text}")
    print(f"Source Language : {source_name}")
    print(f"Target Language : {target_name}")
    print(f"Translated Text : {result}")

    print("=" * 60)


if __name__ == "__main__":
    main()
