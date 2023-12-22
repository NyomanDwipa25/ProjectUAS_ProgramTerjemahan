import re
import pyttsx3
from jawa_to_indo_dict import jawa_to_indo_dict
from indo_to_jawa_dict import indo_to_jawa_dict


def preprocess(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text


def stemmer_sastrawi(word):

    suffixes = ['i', 'an', 'kan']
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]

    return word


def translate_jawa_to_indo(text):
    translated_text = ' '.join(jawa_to_indo_dict.get(word, word) for word in text.split())
    return translated_text


def translate_indo_to_jawa(text):
    translated_text = ' '.join(indo_to_jawa_dict.get(word, word) for word in text.split())
    return translated_text


def label_text(text):
    if 'kerja' in text:
        return 'Pekerjaan'
    elif 'belajar' in text:
        return 'Pendidikan'
    else:
        return 'Umum'

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    text = input("Masukkan Inputan : ")

    preprocessed_text = preprocess(text)

    translated_jawa_to_indo = translate_jawa_to_indo(preprocessed_text)

    stemmed_text = ' '.join((word) for word in translated_jawa_to_indo.split())

    translated_indo_to_jawa = translate_indo_to_jawa(stemmed_text)

    label = label_text(stemmed_text)

    print("\n")
    print("_____________Proses Yang Terjadi____________")
    print("\n")
    print("Preprocessed Text       = " + preprocessed_text)
    print("Translate Jawa --> Indo = " + translated_jawa_to_indo)
    print("Stemming sastrawi       = " + stemmed_text)
    print("Translate Indo --> Jawa = " + translated_indo_to_jawa)
    print("Label                   = " + label)
    speak(translated_indo_to_jawa)

if __name__ == "__main__":
    main()
