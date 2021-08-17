import re
import nltk
from nltk.corpus import words
nltk.download('words',quiet=True)
nltk.download('names',quiet=True)

words_list=words.words()

def encrypt(string,shift):
    cipher=''
    for character in string:
        new_character=character
        if new_character.isalpha():
            offset= 97 if character.islower() else 65
            new_character=chr((ord(character)+shift-offset)%26 + offset)
        cipher+=new_character
    return cipher

def decrypt(string,shift):
    return encrypt(string,shift*-1)

def crack(string):
    if not string:
        return None
    most_like=""
    max_percent=50

    for shift in range(0,26):
        decrypted_word=decrypt(string,shift)
        words=decrypted_word.split()

        english_words_count=0
        for word in words:
            checked_word = re.sub(r"[^a-zA-Z]+"," ",word).lower()
            if checked_word in words_list:
                english_words_count+=1
        english_percent=int(english_words_count/len(words)*100)

        if english_percent>max_percent:
            max_percent=english_percent
            most_like=decrypted_word
    return most_like

if __name__=="__main__":
   sara="Sara like python 3"
   print(encrypt(sara,3))
   print(crack(encrypt(sara,3)))
   print(decrypt(encrypt(sara,3),3))