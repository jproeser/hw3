# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text



######### FINISHED ##########

print("START*******")
 	
import nltk
#import random
#nltk.download() -- used to download nltk initially
from nltk.book import *
#print(text2) -- used to find that the file is Sense and Sensibility by Jane Austen 1811 (file name is austen-sense.txt)
#nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize
import random
debug = False
# get file from user to make mad lib out of
if debug:
	print ("Getting information from file madlib_test.txt...\n")
para = text2[:151]
print("\nOriginal Text (first 150 tokens)-----> ", para)

tagtokens = nltk.pos_tag(para) 
#tags each token according to their part of speech
tagtokens = tagtokens[:151] 
#returns a list of tuples with corresponding part of speech tags

tagconversion = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","RB":"an adverb","JJ":"an adjective"}
sub_prob = {"NN":.15,"NNS":.15,"VB":.1,"RB":.1, "JJ":.1}

# print(sub_prob)
# print(tagconversion)

def spaced(word):
	if word in [",", ".", "?", "!", ":", "[", "]"]:
		return word
	else:
		return " " + word

final_words = []

print("\n")

for (word, tag) in tagtokens:
	if tag not in sub_prob or random.random() > sub_prob[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagconversion[tag]))
		final_words.append(spaced(new_word))
print("\nNEW TEXT-----> ","".join(final_words))
print("\n\nEND*******")








