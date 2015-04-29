
from collections import defaultdict  # available in Python 2.5 and newer


#PARAMS clean function (for regex stripping/replacing)
#		condense function (for grouping common words into themes)
#		data (in form of labeled blog post [ (gender_label,post_text) ])

#Returns aggregates of the average length of words for male/female
#		 seen words in male/female blog post (and the counts aggregated across all posts)
#		 possessive words found in male/female blog post (and the counts aggregated across all posts)

def aggregate_stats(clean,condense,data):
	#Average Lengths of Words [female_bucket,male_bucket]
	avg_len_buckets = [ {"0-3":0,"4-6":0,"7+":0},{"0-3":0,"4-6":0,"7+":0} ]
	#Words seen counter [{female_seen}, {male_seen}]
	#Each object form of {word:count}
	seen = [ defaultdict(int), defaultdict(int) ]

	#Possessive words
	possess = [ defaultdict(int), defaultdict(int) ]

	#Going through data to perform counts / aggregations, etc
	for datapoint in data:
		#0 for female, 1 for male, correspond to buckets/seen lists
		gender = int(datapoint[0])
		blog_post = clean(datapoint[1])

		for word in blog_post.split():

			#Condenses "a","an","the" into articles
			#Or "this","that" into demonstratives, etc
			word = condense(word)

			#Total Seen Words (1 for male, 0 for female)
			seen[gender][word] += 1

			#Push word lengths into buckets
			word_len = len(word)
			if 0 < word_len <= 3:
				avg_len_buckets[gender]["0-3"] += 1
			elif 4 <= word_len <= 6:
				avg_len_buckets[gender]["4-6"] += 1
			else:
				avg_len_buckets[gender]["7+"] += 1

			if "'s" in word or "s'" in word:
				possess[gender][word] += 1
	return {"seen":seen,"possessives":possess,"avg_len_buckets":avg_len_buckets}