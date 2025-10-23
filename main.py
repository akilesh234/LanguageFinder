import tkinter as tk
import unicodedata
from tkinter import ttk
def get_language_family(char):
    char = unicodedata.normalize("NFC", char)
    name = ""
    lang = ""
    for c in char:
        if not unicodedata.category(c).startswith("M"):
            name = unicodedata.name(c)
            lang = unicodedata.name(c).split()[0]
            break
    pronunciation = name.replace("LETTER", "").replace("SIGN", "").lower()
    if pronunciation == name.lower():
        pronunciation = ""
    
   
    
    if  "GREEK" in name:
        family = "Greek"
        country = "Greece"
        larger_family = "Indo-European"
    elif "CYRILLIC" in name:
        family = "Cyrillic"
        country = "Bulgaria"
        larger_family = "Indo-European"
    elif "HIRAGANA"  in name:
        family = "Japanese"
        country = "Japan"
        larger_family = "Japonic"
    elif "HAN" in name:
        family = "Chinese"
        country = "China"
        larger_family = "Sino-Tibetan"
    elif "ARABIC" in name:
        family = "Arabic"
        country = "Arabian Peninsula"
        larger_family = "Afro-Asiatic"
    elif "AMHARIC" in name:
        family = "Amharic"
        country = "Ethiopia"
        larger_family = "Afro-Asiatic"
    elif "ARMENIAN" in name:
        family = "Armenian"
        country = "Armenia"
        larger_family = "Indo-European"
    elif "AVESTAN" in name:
        family = "Avestan"
        country = "Iran"
        larger_family = "Indo-Iranian"
    elif "BALINESE" in name:
        family = "Balinese"
        country = "Indonesia"
        larger_family = "Austronesian"
    elif "BATAK" in name:
        family = "Batak"
        country = "Indonesia"
        larger_family = "Austronesian"
    elif "BOPOMOFO" in name:
        family = "Bopomofo"
        country = "China"
        larger_family = "Sino-Tibetan"
    elif "BRAHMI" in name:
        family = "Brahmi"
        country = "India"
        larger_family = "Indo-European"
    elif "BUHID" in name:
        family = "Buhid"
        country = "Philippines"
        larger_family = "Austronesian"
    elif "CARIAN" in name:
        family = "Carian"
        country = "Ancient Anatolia"
        larger_family = "Indo-European"
    elif "CHAM" in name:
        family = "Cham"
        country = "Vietnam"
        larger_family = "Austronesian"
    elif "COPTIC" in name:
        family = "Coptic"
        country = "Egypt"
        larger_family = "Afro-Asiatic"
    elif any("\u4e00" <= c <= "\u9fff" for c in name):
        family = "Chinese"
        country="China,Japan"
        larger_family="Sino-Tibetian"
    elif "CJK" in name:
        family = "Chinese"
        country="China,Japan"
        larger_family="Sino-Tibetian"
    elif "CREE" in name:
        family = "Cree"
        country = "Canada"
        larger_family = "Algonquian"
    elif "MALAYALAM" in name:
        family = "Malayalam"
        country = "India"
        larger_family = "Dravidian"
    elif "CUNEIFORM" in name:
        family = "Cuneiform"
        country = "Ancient Mesopotamia"
        larger_family = "Afro-Asiatic"
    elif "CYPRIOT" in name:
        family = "Cypriot"
        country = "Cyprus"
        larger_family = "Indo-European"
    elif "DESERET" in name:
        family = "Deseret"
        country = "United States"
        larger_family = "Indo-European"
    elif "ELAMITE" in name:
        family = "Elamite"
        country = "Ancient Iran"
        larger_family = "Elamo-Dravidian"
    elif "GEORGIAN" in name:
        family = "Georgian"
        country = "Georgia"
        larger_family = "Kartvelian"
    elif "GLAGOLITIC" in name:
        family = "Glagolitic"
        country = "Eastern Europe"
        larger_family = "Indo-European"
    elif "GOTHIC" in name:
        family = "Gothic"
        country = "Ancient Germany"
        larger_family = "Indo-European"
    elif "GURMUKHI" in name:
         family = "Gurmukhi"
         country = "India"
         larger_family = "Indo-European"
    elif "HANUNOO" in name:
         family = "Hanunoo"
         country = "Philippines"
         larger_family = "Austronesian"
    elif "HEBREW" in name:
         family = "Hebrew"
         country = "Israel"
         larger_family = "Afro-Asiatic"
    elif "INUKTITUT" in name:
        family = "Inuktitut"
        country = "Canada"
        larger_family = "Eskimo-Aleut"
    elif "KANNADA" in name:
        family = "Kannada"
        country = "India"
        larger_family = "Dravidian"
    elif "JAVANESE" in name:
        family = "Javanese"
        country = "Indonesia"
        larger_family = "Austronesian"
    elif "KAITHI" in name:
        family = "Kaithi"
        country = "India"
        larger_family = "Indo-European"
    elif "KATAKANA" in name:
        family = "Katakana"
        country = "Japan"
        larger_family = "Japonic"
    elif "KAYAH LI" in name:
        family = "Kayah Li"
        country = "Myanmar"
        larger_family = "Sino-Tibetan"
    elif "KHAROSHTHI" in name:
        family = "Kharoshthi"
        country = "Ancient India and Pakistan"
        larger_family = "Indo-European"
    elif "KHUTSURI" in name:
        family = "Khutsuri"
        country = "Georgia"
        larger_family = "Kartvelian"
    elif "LIMBU" in name:
        family = "Limbu"
        country = "Nepal"
        larger_family = "Sino-Tibetan"
    elif "LISU" in name:
        family = "Lisu"
        country = "China"
        larger_family = "Sino-Tibetan"
    elif "LYCIAN" in name:
        family = "Lycian"
        country = "Ancient Anatolia"
        larger_family = "Indo-European"
    elif "LYDIAN" in name:
        family = "Lydian"
        country = "Ancient Anatolia"
        larger_family = "Indo-European"
    elif "MANDAIC" in name:
        family = "Mandaic"
        country = "Iraq"
        larger_family = "Afro-Asiatic"
    elif "MANICHAEAN" in name:
        family = "Manichaean"
        country = "Ancient Iran"
        larger_family = "Indo-European"
    elif "MEETEI MAYEK" in name:
        family = "Meetei Mayek"
        country = "India"
        larger_family = "Sino-Tibetan"
    elif "MONGOLIAN" in name:
        family = "Mongolian"
        country = "Mongolia"
        larger_family = "Mongolic"
    elif "MRO" in name:
        family = "Mro"
        country = "Bangladesh"
        larger_family = "Sino-Tibetan"
    elif "MULTANI" in name:
        family = "Multani"
        country = "India"
        larger_family = "Indo-European"
    elif "NANDINAGARI" in name:
        family = "Nandinagari"
        country = "India"
        larger_family = "Indo-European"
    elif "OGHAM" in name:
        family = "Ogham"
        country = "Ancient Ireland"
        larger_family = "Indo-European"
    elif "OLD ITALIC" in name:
        family = "Old Italic"
        country = "Ancient Italy"
        larger_family = "Indo-European"
    elif "OLD PERSIAN" in name:
        family = "Old Persian"
        country = "Ancient Iran"
        larger_family = "Indo-Iranian"
    elif "OLD SOUTH ARABIAN" in name:
        family = "Old South Arabian"
        country = "Yemen"
        larger_family = "Afro-Asiatic"
    elif "ORIYA" in name:
        family = "Oriya"
        country = "India"
        larger_family = "Indo-European"
    elif "PAHAWH HMONG" in name:
        family = "Pahawh Hmong"
        country = "China, Laos, Vietnam, and Thailand"
        larger_family = "Hmong-Mien"
    elif "PALMYRENE" in name:
        family = "Palmyrene"
        country = "Ancient Syria"
        larger_family="Afro-Asiatic"
    elif "PAU CIN HAU" in name:
        family = "Pau Cin Hau"
        country = "China"
        larger_family = "Sino-Tibetan"
    elif "PHAGS-PA" in name:
        family = "Phags-pa"
        country = "China"
        larger_family = "Sino-Tibetan"
    elif "PHOENICIAN" in name:
        family = "Phoenician"
        country = "Ancient Lebanon"
        larger_family = "Afro-Asiatic"
    elif "PSALTER PAHLAVI" in name:
        family = "Psalter Pahlavi"
        country = "Iran"
        larger_family = "Indo-Iranian"
    elif "REJANG" in name:
        family = "Rejang"
        country = "Indonesia"
        larger_family = "Austronesian"
    elif "RUNIC" in name:
        family = "Runic"
        country = "Northern Europe"
        larger_family = "Indo-European"
    elif "SAMARITAN" in name:
        family = "Samaritan"
        country = "Israel"
        larger_family = "Afro-Asiatic"
    elif "SAURASHTRA" in name:
        family = "Saurashtra"
        country = "India"
        larger_family = "Indo-European"
    elif "SHAVIAN" in name:
        family = "Shavian"
        country = "United Kingdom"
        larger_family = "Indo-European"
    elif "SHARADA" in name:
        family = "Sharada"
        country = "India"
        larger_family = "Indo-European"
    elif "SIDDHAM" in name:
        family = "Siddham"
        country = "India"
        larger_family = "Indo-European"
    elif "SINHALA" in name:
        family = "Sinhala"
        country = "Sri Lanka"
        larger_family = "Indo-European"
    elif "SORA SOMPENG" in name:
        family = "Sora Sompeng"
        country = "India"
        larger_family = "Indo-European"
    elif "SUNDANESE" in name:
        family = "Sundanese"
        country = "Indonesia"
        larger_family = "Austronesian"
    elif "SYLOTI NAGRI" in name:
        family = "Syloti Nagri"
        country = "Bangladesh"
        larger_family = "Indo-European"
    elif "SYRIAC" in name:
        family = "Syriac"
        country = "Syria"
        larger_family = "Afro-Asiatic"
    elif "TAGALOG" in name:
        family = "Tagalog"
        country = "Philippines"
        larger_family = "Austronesian"
    elif "TAGBANWA" in name:
        family = "Tagbanwa"
        country = "Philippines"
        larger_family = "Austronesian"
    elif "TAI LE" in name:
        family = "Tai Le"
        country = "China"
        larger_family = "Tai-Kadai"
    elif "TAI THAM" in name:
        family = "Tai Tham"
        country = "Thailand, Laos, and Burma"
        larger_family = "Tai-Kadai"
    elif "TAI VIET" in name:
        family = "Tai Viet"
        country = "Vietnam"
        larger_family = "Tai-Kadai"
    elif "TAMIL" in name:
        family = "Tamil"
        country = "India"
        larger_family = "Dravidian"
    elif "TELUGU" in name:
        family = "Telugu"
        country = "India"
        larger_family = "Dravidian"
    elif "THAANA" in name:
        family = "Thaana"
        country = "Maldives"
        larger_family = "Indo-European"
    elif "THAI" in name:
        family = "Thai"
        country = "Thailand"
        larger_family = "Tai-Kadai"
    elif "TIBETAN" in name:
        family = "Tibetan"
        country = "Tibet"
        larger_family = "Sino-Tibetan"
    elif "TIFINAGH" in name:
        family = "Tifinagh"
        country = "North Africa"
        larger_family = "Afro-Asiatic"
    elif "UGARITIC" in name:
        family = "Ugaritic"
        country = "Ancient Syria"
        larger_family = "Afro-Asiatic"
    elif "VAI" in name:
        family = "Vai"
        country = "Liberia and Sierra Leone"
        larger_family = "Niger-Congo"
    elif "WARANG CITI" in name:
        family = "Warang Citi"
        country = "India"
        larger_family = "Indo-European"
    else:
        family = "Latin"
        country = "USA, UK, Australia, New Zealand"
        larger_family = "Indo-European"
    pronunciation = name.replace("LETTER", "").replace("SIGN", "").lower()
    return (family, country, larger_family,name,pronunciation)

def get_info():
    
    word = entry.get()
    info_text = ""
    
    family, country, larger_family, name, _ = get_language_family(word[0])
    info_text += "The word '{}' belongs to the {} script,\n which is used in {}.\nThe {} language belongs to the {} language family.\n\n".format(word, family, country, family, larger_family)

    for char in word:
        _, _, _, _, pronunciation = get_language_family(char)
        info_text += "The pronounciation for the character '{}' is {}\n".format(char, pronunciation)
    
    
label.config(text=info_text)
root = tk.Tk()
root.title("Language Info")
root.geometry("400x300")
root.iconbitmap(r'C:\Users\ADMIN\Desktop\favicon.ico')


main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True)

input_frame = ttk.Frame(main_frame)
input_frame.pack(fill="x")

label = ttk.Label(input_frame, text="Enter a word or character:")
label.pack(side="left")

entry = ttk.Entry(input_frame, width=30)
entry.pack(side="left")

button = ttk.Button(main_frame, text="Get Info", command=get_info)
button.pack()
