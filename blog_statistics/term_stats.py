


#PARAMS:
#     seen: list of 2 dictionaries, corresponding to female and male respectively
#	     	Each dict of the form {word:count}, 
#		 	where all of the words are associated
#   	 	with their respective counts of appearence
#	     	aggregated over all of that gender's blog posts
#
#		 n: number of significant "male heavy" or "female heavy" 
#    		words to print
		
#Finds the % occurance of all words, and then prints
#The words with the greatest difference in % between
#Male and Female blog posts

#TODO: Compute Z-Score on these words to normalize differences between them
#	  (Subtract each words % by the average words %, divide by the standard deviation)

def term_stats(seen,n):
	#Normalizing words
	##################
	#get total number of words by males and females
	tot_f = sum(seen[0].values())
	tot_m = sum(seen[1].values())



	#Divide word counts by number of words males/females used
	seen[1] = {key:100.0*val/tot_m for key,val in seen[1].items()}
	seen[0] = {key:100.0*val/tot_f for key,val in seen[0].items()}
	##################
	#Seen words now normalized as % frequency that they appear

	top_male   = sorted(seen[1].items(),key=lambda x:x[1],reverse=True)
	top_female = sorted(seen[0].items(),key=lambda x:x[1],reverse=True)

	top_diffs = []
	for key,val in top_male:
		if key in seen[0]:
			diff = round(val-seen[0][key],3)
			top_diffs.append( (key,diff) )


	top_diffs = sorted(top_diffs,key=lambda x:x[1])
	#column width spacer for words
	col_width = max(len(word[0]) for word in top_diffs)-12
	#Column width spacer for numbers
	w=23


	print("Male Dominant Words")
	print("Difference in Percentage of Occurance")
	print("___________________")
	print("Words: ".ljust(col_width)+"(Male-Female)".ljust(w)+"Male".ljust(w)+"Female")
	for word in sorted(top_diffs[-n:],key=lambda x:x[1],reverse=True):
		label = word[0].ljust(col_width)
		diff =   ("%.3f%%"%word[1]).ljust(w)
		male =   ("%.3f%%"%seen[1][word[0]]).ljust(w)
		female = ("%.3f%%"%seen[0][word[0]])
		print(label+diff+male+female)


	print("")
	print("Female Dominant Words")
	print("Difference in Percentage of Occurance")
	print("___________________")
	print("Words: ".ljust(col_width)+"(Male-Female)".ljust(w)+"Male".ljust(w)+"Female")
	for word in sorted(top_diffs[0:n],key=lambda x:x[1]):
		label = word[0].ljust(col_width)
		diff =   ("%.3f%%"%word[1]).ljust(w)
		male =   ("%.3f%%"%seen[1][word[0]]).ljust(w)
		female = ("%.3f%%"%seen[0][word[0]])
		print(label+diff+male+female)
