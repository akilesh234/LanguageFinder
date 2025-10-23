# Language Identifier

## Overview

The **Language Identifier** is a Python-based GUI application that detects the language, country, and language family of a given word or character. It uses Python’s built-in **unicodedata** module to analyze Unicode character names and classify them according to their script and linguistic origin. The GUI is implemented using **Tkinter** and **ttk**.

This project was developed as part of a **B.Tech. in Artificial Intelligence and Data Science** program at **PSG Institute of Technology and Applied Research, Coimbatore**, affiliated with **Anna University, Chennai**.

---

## Authors

* Akilesh J S (715522243004)
* Nitesh Kumar N S (715522243034)
* Abishek S (715522243002)
* Harish P (715522243019)

---

## Objective

The goal of this project is to build a Python application that:

* Identifies the **language**, **country**, and **language family** of the input text.
* Displays the **pronunciation** of each character.
* Provides a simple graphical interface for user input.

---

## Abstract

This project identifies the script and origin of characters by processing their Unicode names. Using the `unicodedata` module, each character is normalized and analyzed through a set of conditional checks to map it to its respective language and region.

The program supports multiple writing systems, including Arabic, Bengali, Cyrillic, Devanagari, Greek, Tamil, Telugu, Malayalam, Thai, Tibetan, and many others. A graphical interface built with Tkinter makes it easy for users to enter text and view the results.

---

## Implementation

The program defines a core function, `get_language_family(char)`, that processes Unicode characters and returns a tuple containing:

* Language family
* Country
* Larger language family
* Unicode name
* Pronunciation

It uses the following modules:

* **unicodedata**: For Unicode normalization and name extraction.
* **tkinter** and **ttk**: For creating the GUI.

### Example Output

```
Input: தமிழ்

Output:
The word 'தமிழ்' belongs to the Tamil script,
which is used in India.
The Tamil language belongs to the Dravidian language family.

The pronunciation for the character 'த' is tha
The pronunciation for the character 'ம' is ma
```

---

## Modules Used

### unicodedata

The `unicodedata` module provides access to the Unicode Character Database, which defines character names and properties.

**Key Features:**

* Supports multilingual text.
* Provides consistent encoding across platforms.
* Enables easy text classification by script.

### tkinter

`tkinter` is the standard GUI library for Python, offering tools to build cross-platform applications with ease.

**Advantages:**

* Simple to use and bundled with Python.
* Cross-platform support (Windows, macOS, Linux).
* Allows event-driven programming for interactive applications.

---

## How to Run

1. Ensure **Python 3.8+** is installed.
2. Clone or download the project repository.
3. Open a terminal in the project folder.
4. Run the program using:

   ```bash
   python language_identifier.py
   ```
5. Enter a word or character in the text box and click **Get Info**.

---

## Applications

* Language learning and pronunciation tools.
* Linguistic and script analysis.
* Multilingual software development and localization.
* Unicode and text-processing demonstrations.

---

## Example Use Case

**Input:** こんにちは
**Output:**

* Script: Hiragana
* Country: Japan
* Language Family: Japonic
* Pronunciations: ko, n, ni, chi, wa

---

## References

* [Langid.py - Python Language Identifier](https://pypi.org/project/langid/)
* [FastText Language Identification](https://fasttext.cc/docs/en/language-identification.html)
* [DetectLanguage API](https://detectlanguage.com/)
* [Google Cloud Translation API](https://cloud.google.com/translate/docs/languages)
* [IBM Watson Language Translator](https://www.ibm.com/cloud/watson-language-translator)
* [NLTK Language Identification](https://www.nltk.org/book/ch06.html#language-identification)
* [Apache Tika Language Detection](https://cwiki.apache.org/confluence/display/TIKA/Language+Detection)

---

## Conclusion

This project demonstrates how Python’s Unicode handling and Tkinter GUI capabilities can be combined to build a functional **Language Identifier**. It effectively classifies scripts, determines language families, and provides pronunciation hints. The system can serve as a base for more advanced multilingual or AI-based linguistic tools.

---

## License

This project was created for academic purposes and does not currently include an open-source license. You may add one if needed for future development or distribution.
