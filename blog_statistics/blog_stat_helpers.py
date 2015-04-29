
import re


#Strips punctuations/urls on data
def clean(word):
	word = word.lower()
	word = re.sub("[\n,.;!?()\\\\]+","",word)
	word = re.sub("www.[^\s]+","URL",word)
	word = re.sub("http://[^\s]+","URL",word)
	word = re.sub("https://[^\s]+","URL",word)
	return word





#Condense words into buckets
#Based on common syntactic meaning
demonstratives = {"this","that","these","those"}
articles = {"a","an","the"}
prepositions = {"of","in","for","by","on","from","with","to"}
first_person = {"i","im","i'm","my","mine","me","am"}
second_person= {"you","your","youre"}
third_person = {"their","them","they"}
conjunction = {"and","or","but","because","so"}
male = {"he","his","him","dude","man","men","boy"}
female = {"she","her","gal","girl","woman","women"}

def condense_word(word):
	if word in demonstratives:
		return "DEMONSTRATIVE"
	elif word in articles:
		return "ARTICLE"
	elif word in prepositions:
		return "PREPOSITION"
	elif word in conjunction:
		return "CONJUNCTION"
	elif word in first_person:
		return "1ST_PERSON"
	elif word in second_person:
		return "2ND_PERSON"
	elif word in third_person:
		return "3RD_PERSON_NEUTRAL"
	elif word in male:
		return "MALE"
	elif word in female:
		return "FEMALE"
	else:
		return word