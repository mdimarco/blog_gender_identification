
from collections import defaultdict  # available in Python 2.5 and newer

#Takes in RAW TRAINING DATA (From the csv)

#Prints the % of male text that is punctuation
#   vs. the % of female text that is punctuation
def punctuation_frequencies(train_data):
	male = []
	female = []
	punct = {'!','?',',','.',"'",'"',"-"}


	#Number of Punctuation
	#For each blog post
	for blog_post in train_data:
		punc_dict = defaultdict(int)
		char_count = 0

		#Count up punctuation characters
		for c in blog_post[1]:
			if c in punct:
				punc_dict[c] += 1
			char_count+=1


		punc_dict["Total_punc"] = float(sum(punc_dict.values()))
		punc_dict["Total_chars"] = float(char_count)
		#Append to associated gender list
		if blog_post[0] == '1':
			male.append(punc_dict)
		else:
			female.append(punc_dict)

	male_usage = {}
	female_usage = {}
	print("")
	print("Percent Usage of punctuation in body of text, Male vs. Female")
	for punc in punct:
		male_usage[punc] =   sum( [ x[punc]/x["Total_chars"] for x in male]   )/len(male)
		female_usage[punc] = sum( [ y[punc]/y["Total_chars"] for y in female] )/len(female)

		#print("Punct:   %s   \t M: %.2f%% F: %.2f%%" % (punc,male_usage[punc]*100,female_usage[punc]*100) )

	#Total Punctuation Counters
	male_total = sum(   [ x["Total_punc"]/x["Total_chars"] for x in male]   )/len(male)
	female_total = sum( [ y["Total_punc"]/y["Total_chars"] for y in female] )/len(female)


	print("Total Punct: \t M: %.2f%% F: %.2f%%" %(male_total*100,female_total*100))
	print("")
