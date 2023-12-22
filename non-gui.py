from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from deep_translator import GoogleTranslator

factory = StemmerFactory()
stemmer = factory.create_stemmer()

text = input("Masukkan Inputan : ")
translated = GoogleTranslator(source='jw', target='id').translate(text)

output   = stemmer.stem(translated)

bro = GoogleTranslator(source='id', target='jw').translate(output)

print("\n")
print("_____________Proses Yang Terjadi____________")
print("\n")
print("Translate Jawa --> Indo = " + translated)
print("Stemming sastrawi       = " + output)
print("Translate Indo --> Jawa = " + bro)