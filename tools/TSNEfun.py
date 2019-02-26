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
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk
import pandas as pd


'''
Write a function to perform the pre processing steps on the entire dataset
'''
def lemmatize_stemming(text):
    stemmer= SnowballStemmer("english")
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

# Tokenize and lemmatize
def preprocess(text):
    result=[]
    for token in gensim.utils.simple_preprocess(text) :
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
            
    return result

def main():
	
	# Fetching train and testing data using sklearn's API

	newsgroups_train = fetch_20newsgroups(subset='train')
	newsgroups_test = fetch_20newsgroups(subset='test')
	nltk.download('wordnet')
	
	
	
	
	#Preprocessing the training data
	processed_docs = []
	
	for doc in newsgroups_train.data:
		processed_docs.append(preprocess(doc))

	print(processed_docs[0])	

	





























if __name__ == "__main__":
	main()	