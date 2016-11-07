# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
 	
import nltk
#import random
#nltk.download() -- used to download nltk initially
from nltk.book import *
#print(text2) -- used to find that the file is Sense and Sensibility by Jane Austen 1811 (file name is austen-sense.txt)
#nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize
debug = False
# get file from user to make mad lib out of
if debug:
	print ("Getting information from file madlib_test.txt...\n")
para = text2 
##You need to make a jump right here and turn para into a list of words
count=0
for i in para while count <= 250:
	print(i)
	count+=1

#comment


# from nltk.tokenize import sent_tokenize, word_tokenize

# text = "Hello students, how are you doing today? Have you recovered from the exam?  I hope you are feeling better.  Things will be fine."

# print(sent_tokenize(text))
# print(word_tokenize(text))

# for i in word_tokenize(text):
# 	print(i)






#nltk.corpus.gutenberg.fileids()





#f = open(fname, encoding="ISO-8859-1")
#f = open(fname, 'r')

#read each line
#with codecs.open(fname, "r",encoding='utf-8', errors='ignore') as fdata:
tokens = nltk.word_tokenize(para)
print("TOKENS")
print(tokens[:151])

# tokens = nltk.word_tokenize(para)
# print("TOKENS")
# print(tokens)
# tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print("TAGGED TOKENS")
# print(tagged_tokens)
# if debug:
# 	print ("First few tagged tokens are:")
# 	for tup in tagged_tokens[:5]:
# 		print (tup)

# tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
# substitution_probabilities = {"NN":.1,"NNS":.2,"VB":.25,"JJ":.25}

# def spaced(word):
# 	if word in [",", ".", "?", "!", ":"]:
# 		return word
# 	else:
# 		return " " + word

# final_words = []


# for (word, tag) in tagged_tokens:
# 	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
# 		final_words.append(spaced(word))
# 	else:
# 		new_word = input("Please enter %s:\n" % (tagmap[tag]))
# 		final_words.append(spaced(new_word))

# print ("".join(final_words))






print("\n\nEND*******")








