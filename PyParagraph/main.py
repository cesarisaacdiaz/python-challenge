import os
import re

imputfile = os.path.join("paragraph_2.txt")
outputfile = os.path.join("output.txt")

paragraph = ""

with open(imputfile) as data:
    paragraph = data.read().replace("\n"," ")

word_by_word = paragraph.split(" ")
print(word_by_word)

word_count = len(word_by_word)
print(word_count)

letter_counter = []

for word in word_by_word:
    letter_counter.append(len(word))

avg_letter = sum(letter_counter)/float(len(letter_counter))

sentences_div = re.split("(?<=[.!?]) + ", paragraph)
print(sentences_div)
sentences_counter = len(sentences_div)

word_per_sentence = []

for sentence in sentences_div:
    word_per_sentence.append(len(sentence.split(" ")))

avg_sentence_len=(sum(word_per_sentence)/float(len(word_per_sentence)))

salida = (f"\nParagraph Analysis\n"
          f"--------------------\n"
          f"Aproximate Word Count: {word_count}\n"
          f"Aproximate Sentences Count: {sentences_counter}\n"
          f"Average Letter Count: {avg_letter}\n"
          f"Average Sentence Length: {avg_sentence_len}"
         )

print(salida)

with open(outputfile,"a") as data:
    data.write(salida)