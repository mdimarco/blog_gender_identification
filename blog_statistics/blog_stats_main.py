
import argparse
from collections import defaultdict  # available in Python 2.5 and newer
import csv
import re

#Arguments Stuff
parser = argparse.ArgumentParser()
parser.add_argument('-data', required=True, help='Labeled csv text to run analysis on')
parser.add_argument('-n', help='Number of male/female result to show')

opts = parser.parse_args()



import blog_stat_helpers
from aggregate_stats import aggregate_stats

with open(opts.data, 'rU') as f:
		reader = csv.reader(f)
		data = list(reader)



####################################
#Code in punctuation_stats.py
#UNCOMMENT FOR PUNCTUATION STATS
from punctuation_stats import punctuation_frequencies
punctuation_frequencies(data)
####################################





#Found in blog_stat_helpers.py
word_cleaner = blog_stat_helpers.clean
word_condenser = blog_stat_helpers.condense_word




stats = aggregate_stats(word_cleaner,word_condenser,data)
#Average word lengths aggregated into buckets
avg_len_buckets = stats["avg_len_buckets"]
#Counts aggregated across ALL male/female blog posts
#[{words_in_male_blogs:count}, {words_in_female_blogs:count}]
seen = stats["seen"]



#[{possessive_words_in_male_blogs:count},{sameforfemale:count}]
#Possessive words defined as ending in 's or s'
#Counts aggregated across ALL male/female blog posts
#EX: [{john's:1,mary's:10}, {people's:100, 'jesus':15}]

####################################
#UNCOMMENT FOR POSSESSIVE STATISTICS
possess = stats["possessives"]
from possessive_stats import print_possessive_info
print_possessive_info(possess)
####################################





#compares terms based on frequency in
#male vs. female blogs
####################################
####################################
#UNCOMMENT FOR TERM STATISTICS

#Number of words to compare in terms of
#how often they appear MALE vs FEMALE
if not opts.n:
	n = 10
else:
	n=int(opts.n)
from term_stats import term_stats
top_diffs = term_stats(seen,n)
####################################
####################################


#Uses what term_stats has deemed the most significant
#(and has saved in data/significant_words.txt) to write
#A new version of the blog posts that only contains features
#deemed significant by z-score ratios

####################################
####################################
#UNCOMMENT FOR TRACKING SIGNIFICANT WORDS
#from significant_word_stats import track_sig_words
#blog_as_significant = track_sig_words(word_cleaner,word_condenser,data)

####################################
####################################

with open("../data/blog-significant-words.csv","w") as blog_file:
	sig_writer = csv.writer(blog_file,quoting=csv.QUOTE_ALL)
	for row in blog_as_significant:
		sig_writer.writerow(row)

