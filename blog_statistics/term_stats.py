

import math
import numpy
#PARAMS:
#     seen: list of 2 dictionaries, corresponding to female and male respectively
#	     	Each dict of the form {word:count}, 
#		 	where all of the words are associated
#   	 	with their respective counts of appearence
#	     	aggregated over all of that gender's blog posts
#
#		 n: number of significant "male heavy" or "female heavy" 
#    		words to print
		
#Normalizes word frequencies for male and female labeled blog posts
#Computing the z-score for each, then determines "significance"
#to be the ratio of male z-score : female z-score

#ADDITIONALLY
#This writes the largest and smallest male:female z-scores
#to the file "significant_words.txt" in the data folder

def term_stats(seen,n):
	#Normalizing words
	##################
	#get total number of words by males and females
	f_vals = seen[0].values()
	m_vals = seen[1].values()
	tot_f = sum(f_vals)
	tot_m = sum(m_vals)

	mean_f = numpy.mean(f_vals)
	std_f = numpy.std(f_vals)

	mean_m = numpy.mean(m_vals)
	std_m = numpy.std(m_vals)

	print("Female Mean word frequency: %.2f"%mean_f)
	print("Male Mean word frequency: %.2f"%mean_m)
	print("Female Standard Deviation: %.2f"%std_f)
	print("Male Standard Deviation: %.2f"%std_m)
	print("")
	#Divide word counts by number of words males/females used
	seen[1] = {key:(val-mean_m)/std_m for key,val in seen[1].items()}
	seen[0] = {key:(val-mean_f)/std_f for key,val in seen[0].items()}
	##################
	#Seen words now normalized as % frequency that they appear


	top_male   = sorted(seen[1].items(),key=lambda x:x[1],reverse=True)
	top_female = sorted(seen[0].items(),key=lambda x:x[1],reverse=True)



	top_diffs = []
	for key,val in top_male:
		if key in seen[0]:
			diff = term_diff(val,seen[0][key])
			top_diffs.append((key,diff))



	top_diffs = sorted(top_diffs,key=lambda x:x[1])
	#column width spacer for words
	col_width = max(len(word[0]) for word in top_diffs)-12
	#Column width spacer for numbers
	w=23


	#output = open("../data/significant_words.txt","w")

	print("Male Dominant Words")
	print("High Male:Female Z-Score Ratio")
	print("___________________")
	print("Words: ".ljust(col_width)+"(Male:Female)".ljust(w)+"Z-Male".ljust(w)+"Z-Female")
	for word in sorted(top_diffs[-n:],key=lambda x:x[1],reverse=True):
		label = word[0].ljust(col_width)
		diff =   ("%.3f"%word[1]).ljust(w)
		male =   ("%.3f"%seen[1][word[0]]).ljust(w)
		female = ("%.3f"%seen[0][word[0]])
		print(label+diff+male+female)
		#output.write(word[0]+"\n")


	print("")
	print("Female Dominant Words")
	print("Low Male:Female Z-Score Ratio")
	print("___________________")
	print("Words: ".ljust(col_width)+"(Male:Female)".ljust(w)+"Z-Male".ljust(w)+"Z-Female")
	for word in sorted(top_diffs[0:n],key=lambda x:x[1]):
		label = word[0].ljust(col_width)
		diff =   ("%.3f"%word[1]).ljust(w)
		male =   ("%.3f"%seen[1][word[0]]).ljust(w)
		female = ("%.3f"%seen[0][word[0]])
		print(label+diff+male+female)
		#output.write(word[0]+"\n")

	#output.close()


	count1 = 0
	count2 = 0
	count3 = 0
	for item,count in seen[0].items():
		if count < 0:
			count1+=1
		if count > 0:
			count2+=1
		count3 += 1
	print(count1/float(count3))
	print(count2/float(count3))
	return top_diffs



#TRY CHANGING ME
#try changing to differences in z-score, ratio, transformations, etc. etc. 


#PARAMS male z-score of word frequencies
#		female """""
#RETURNS ratio/difference/comparison between the two
def term_diff(male_val,female_val):


	#if both are negative, these 
	#are too uncommon to be significant
	if male_val < 0:
		male_val = .01 

	if female_val < 0:
		female_val = .01
	

	return round(male_val/female_val,3)


