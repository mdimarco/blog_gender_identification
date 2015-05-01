
from collections import defaultdict  # available in Python 2.5 and newer

#Taking stats on significant words between males and females
def track_sig_words(clean,condense,data):


	word_file = open("../data/significant_words.txt","r")
	significant_words = set({})
	for word in word_file.readlines():
		significant_words.add(word[0:-1])


	significant_counter = defaultdict(int)
	num_with_sig = 0 #number of blog posts with a.l. 1 significant word


	#Reformatted blog posts as bag of significant words
	posts_as_sig = []

	for datapoint in data:
		blog_post = clean(datapoint[1])

		blog_words = []

		for word in blog_post.split():
			word = condense(word)
			
			if word in significant_words:
				blog_words.append(word)

		has_sig_word = 0

		for sig_word in set.intersection(set(blog_words),significant_words):
			has_sig_word+=1
			significant_counter[sig_word] += 1

		if has_sig_word >= 5:
			num_with_sig += 1

		posts_as_sig.append([datapoint[0]," ".join(blog_words)])


	num_posts = len(data)
	print("%.2f%% of posts contain at least 5 significant words" % (100.0*num_with_sig/num_posts) )

	return posts_as_sig
