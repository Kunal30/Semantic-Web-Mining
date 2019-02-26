# Code Author: Kunal Vinay Kumar Suthar
# ASU ID: 1215112535
# Course: CSE-573: Semantic Web Mining
# Project: Document Clustering and Visualization

# 1) ----> Data preprocessing(Tokenization, Stemming, Stopword Removal, Lematization) 
# 2) ----> Latent Dirichlet Allocation 
# 3) ----> TSNE 
# 4) ----> 2D Visualization 
# 5) ----> 3D Visualization


from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB

def main():
	
	newsgroups_train = fetch_20newsgroups(subset='train')
	newsgroups_test = fetch_20newsgroups(subset='test')
	
	





























if __name__ == "__main__":
	main()	