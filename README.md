# CodeAlpha-Internship1

# 🌐 Language Translation Tool

A simple Python-based **Language Translation Tool** developed as part of the **CodeAlpha Artificial Intelligence Internship**.

The application allows users to enter text, select a source language and target language, and receive the translated text using an online translation API.

## 📌 Project Overview

The Language Translation Tool provides an easy way to translate text between multiple languages.

The project uses Python's built-in libraries to communicate with the **MyMemory Translation API** and display the translated result in the terminal.

It also includes proper-name protection so that names such as **Renish, John, or London** are not unnecessarily translated by the translation service.

## ✨ Features

* 🌍 Supports multiple languages
* 🔤 Source language selection
* 🎯 Target language selection
* 📝 User text input
* 🌐 Online translation using an API
* 👤 Proper-name protection
* ⚠️ Invalid input handling
* ❌ Empty input validation
* 🔌 API error handling
* 💻 Simple Python terminal interface
* 🐍 Compatible with Python 3.13

## 🗣️ Supported Languages

The current version supports:

1. English
2. Gujarati
3. Hindi
4. Spanish
5. French
6. German
7. Italian
8. Portuguese
9. Japanese
10. Korean

## 🛠️ Technologies Used

* **Python 3.13**
* `urllib.parse`
* `urllib.request`
* `json`
* `re`
* **MyMemory Translation API**

## 🔄 How the Project Works

The basic workflow is:

```text
User enters text
        ↓
Select source language
        ↓
Select target language
        ↓
Protect proper names
        ↓
Send request to Translation API
        ↓
Receive translated response
        ↓
Restore protected names
        ↓
Display translated text
```

## 👤 Proper Name Protection

Translation APIs may sometimes interpret a person's name as a normal English word.

For example:

```text
Input:
I am Renish
```

Without name protection, the API may incorrectly translate **Renish**.

The program temporarily protects the name before translation and restores it afterward.

Expected result:

```text
I am Renish
        ↓
मैं Renish हूँ
```

This helps preserve proper names during translation.

## ▶️ How to Run

### Step 1 — Install Python

Install **Python 3.13** on your computer.

Check your Python version:

```bash
python --version
```

Example:

```text
Python 3.13.14
```

### Step 2 — Download or Clone the Project

Place the Python file inside your project folder.

Example:

```text
Language Translation Tool/
│
└── language_translation_tool.py
```

### Step 3 — Run the Program

Open Command Prompt or terminal inside the project folder and run:

```bash
python language_translation_tool.py
```

You can also run the `.py` file directly using **IDLE**.

## 💻 Example Output

```text
============================================================
             LANGUAGE TRANSLATION TOOL
============================================================

Available Languages:
1. English
2. Gujarati
3. Hindi
4. Spanish
5. French
6. German
7. Italian
8. Portuguese
9. Japanese
10. Korean

Select Source Language: 1
Select Target Language: 3

Enter text to translate: I am Renish

Translating...

============================================================
                 TRANSLATION RESULT
============================================================
Original Text   : I am Renish
Source Language : English
Target Language : Hindi
Translated Text : मैं Renish हूँ
============================================================
```

## 📂 Project Structure

```text
CodeAlpha_LanguageTranslationTool/
│
├── language_translation_tool.py
└── README.md
```

## ⚙️ Requirements

This project uses Python standard libraries, so no additional Python package installation is required.

You need:

* Python 3.13 or compatible Python version
* Internet connection
* Working Translation API access

## 🌐 Translation API

This project uses the **MyMemory Translation API** to process translation requests.

The program sends the following information to the API:

* Text to translate
* Source language
* Target language

The API returns the translated response, which is then displayed to the user.

## 🧪 Testing

The application can be tested using:

* Different source languages
* Different target languages
* Short sentences
* Long sentences
* Proper names
* Empty input
* Invalid language selections
* Internet/API connection failures

Example:

```text
Input:
Hello, how are you?

Source:
English

Target:
Gujarati

Output:
હેલો, તમે કેમ છો?
```

## 🎯 Internship Task

**Organization:** CodeAlpha

**Domain:** Artificial Intelligence

**Task:** Task 1 — Language Translation Tool

**Internship Project:** Language Translation Tool

## 🚀 Future Improvements

Possible future improvements include:

* Graphical User Interface (GUI)
* Web-based interface
* Copy translated text button
* Text-to-Speech
* Speech-to-Text
* Automatic source-language detection
* More supported languages
* Translation history
* Improved proper-name recognition
* Offline translation support

## 👨‍💻 Author

**Renish Chovatiya**

Developed as part of the **CodeAlpha Artificial Intelligence Internship**.

## 📄 License

This project is created for educational and internship purposes.
