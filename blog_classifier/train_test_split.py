from random import shuffle
import argparse
import csv
#Takes in a blog data file, shuffles it, 
#and splits it into 90% train, 10% test
parser = argparse.ArgumentParser()
parser.add_argument('-data', required=True, help='Labeled csv text to split')
opts = parser.parse_args()


with open(opts.data, 'rU') as f:
		reader = csv.reader(f)
		data = list(reader)

shuffle(data)


num_posts = len(data)

with open("../data/train.csv","w") as out_train:
	train_writer = csv.writer(out_train,quoting=csv.QUOTE_ALL)
	for row in data[len(data)/10:]:
		train_writer.writerow(row)

with open("../data/test.csv","w") as out_test:
	test_writer = csv.writer(out_test,quoting=csv.QUOTE_ALL)
	for row in data[0:len(data)/10]:
		test_writer.writerow(row)

