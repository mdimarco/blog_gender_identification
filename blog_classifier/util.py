from __future__ import division
from collections import defaultdict
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc


def plot_roc_curve(labels, predict_proba):
	# Compute ROC curve and area the curve
	fpr, tpr, thresholds = roc_curve(labels, predict_proba[:, 1])
	roc_auc = auc(fpr, tpr)
	print("Area under the ROC curve : %f" % roc_auc)

	# Plot ROC curve
	plt.clf()
	plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
	plt.plot([0, 1], [0, 1], 'k--')
	plt.xlim([0.0, 1.0])
	plt.ylim([0.0, 1.0])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('Receiver operating characteristic example')
	plt.legend(loc="lower right")
	plt.show()


def print_most_informative_features(classifier_type, vectorizer, classifier, n=10):
	if classifier_type == 'nb':
		print_most_informative_features_using_prob(vectorizer, classifier, n)
	elif (classifier_type == 'log') or (classifier_type == 'svm'):
		print_most_informative_features_using_coef(vectorizer, classifier, n)
	else:
		raise Exception('Unrecognized classifier!')

def print_most_informative_features_using_prob(vectorizer, classifier, n=10):
	""" 
	-- nltk style
	Return a list of the 'most informative' features used by this 
	classifier.  For the purpose of this function, the 
	informativeness of a feature C{(fname,fval)} is equal to the 
	highest value of P(fname=fval|label), for any label, divided by 
	the lowest value of P(fname=fval|label), for any label:: 

	max[ P(fname=fval|label1) / P(fname=fval|label2) ] 
	""" 
	# The set of (fname, fval) pairs used by this classifier. 
	features = set() 
	# The max & min probability associated w/ each (fname, fval) 
	# pair.  Maps (fname,fval) -> float. 
	maxprob = defaultdict(lambda: 0.0) 
	minprob = defaultdict(lambda: 1.0) 
	
	for probdist in classifier.feature_log_prob_:
		probdist = numpy.e**(probdist)
		for (i, p) in enumerate(probdist):
			feature = i
			features.add(feature)
			maxprob[feature] = max(p, maxprob[feature])
			minprob[feature] = min(p, minprob[feature])
			if minprob[feature] == 0:
				features.discard(feature)

	# Convert features to a list, & sort it by how informative features are. 
	features = sorted(features, key=lambda feature: minprob[feature]/maxprob[feature])
	feature_names = vectorizer.get_feature_names()
	n0 = n1 = 0
	v0 = []
	v1 = []
	for i in features:
		if (n0 >= n) and (n1 >= n):
			break
		p0 = numpy.e**(classifier.feature_log_prob_[0][i])
		p1 = numpy.e**(classifier.feature_log_prob_[1][i])
		if p0 == 0:
			continue
		else:
			ratio = round(p1 / p0, 4)
		if ratio < 1:
			if n0 >= n:
				continue
			n0 += 1
			v0.append((-1/ratio, feature_names[i]))
		else:
			if n1 >= n:
				continue
			n1 += 1
			v1.append((ratio, feature_names[i]))

	top = zip(v0, v1)
	for (c1,f1),(c2,f2) in top:
		print "\t%.4f\t%-15s\t\t%.4f\t%-15s" % (c1,f1,c2,f2)

def print_most_informative_features_using_coef(vectorizer, classifier, n=10):
	c_f = sorted(zip(classifier.coef_[0], vectorizer.get_feature_names()))
	top = zip(c_f[:n], c_f[:-(n+1):-1])
	for (c1,f1),(c2,f2) in top:
		print "\t%.4f\t%-15s\t\t%.4f\t%-15s" % (c1,f1,c2,f2)
