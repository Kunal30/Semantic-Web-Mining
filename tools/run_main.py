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
from sklearn.manifold import TSNE
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk
import pandas as pd
from sklearn.manifold import TSNE
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
# from tsne import tsne

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

	#newsgroups_train = fetch_20newsgroups(subset='train')
	#newsgroups_test = fetch_20newsgroups(subset='test')
	##number_of_test_docs=len(newsgroups_test.data)
	#nltk.download('wordnet')
				
	##Preprocessing the training data
	#processed_docs = []
	#i=0

	#for doc in newsgroups_train.data:
	#	#i=i+1
	#	processed_docs.append(preprocess(doc))
	#	#if i>=5:
	#	#	break
	
	##i=0
	##entiretestdata=""
	##for doc in newsgroups_test.data:
	##	#i=i+1
	##	entiretestdata = entiretestdata + doc
	##	#if i==1:
	##		#break
	##entiretestdata = preprocess(entiretestdata)
	##entiretestdata=np.unique(entiretestdata)
	##np.save("newfile",entiretestdata)

	#'''
	#Create a dictionary from 'processed_docs' containing the number of times a word appears 
	#in the training set using gensim.corpora.Dictionary and call it 'dictionary'
	#'''
	#dictionary = gensim.corpora.Dictionary(processed_docs)

	## '''
	## Checking dictionary created
	## '''
	## count = 0
	## for k, v in dictionary.iteritems():
	##     print(k, v)
	##     count += 1
	##     if count > 10:
	##         break

	#'''
	#Create the Bag-of-words model for each document i.e for each document we create a dictionary reporting how many
	#words and how many times those words appear. Save this to 'bow_corpus'
	#'''
	#bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
	
	#'''
	#Preview BOW for our sample preprocessed document
	#'''
	## document_num = 20
	## bow_doc_x = bow_corpus[document_num]

	## for i in range(len(bow_doc_x)):
	##     print("Word {} (\"{}\") appears {} time.".format(bow_doc_x[i][0], 
	##                                                      dictionary[bow_doc_x[i][0]], 
	##                                                      bow_doc_x[i][1]))        
	
	#'''
	#Train your lda model using gensim.models.LdaMulticore and save it to 'lda_model'
	#'''
	## TODO
	#lda_model = []
	#try:
	#	lda_model = gensim.models.LdaModel.load('lda.model')
	#except:
	#	lda_model =  gensim.models.LdaMulticore(bow_corpus, 
	#									num_topics = 20, 
	#									id2word = dictionary,
	#									passes = 10,
	#									workers = 2)

	#	lda_model.save('lda.model')
	#'''
	#For each topic, we will explore the words occuring in that topic and its relative weight
	#'''
	#for idx, topic in lda_model.print_topics(-1):
	#	#print(type(topic))
	#	print("Topic: {} \nWords: {}".format(idx, topic ))
	#	print("\n")



	# #num = 100
	#unseen_documents=[]
	
	# #for i in range(0,len(newsgroups_test.data)):
	##for i in range(0,10):
	##	unseen_documents.append(newsgroups_test.data[i])
	
	##print(unseen_documents)    

	# #Data preprocessing step for the unseen document
	

	
	## Now passing the Topic-Document Matrix to the TSNE MODULE:

	##all_test_words=np.load("newfile.npy")
	##number_of_test_words=len(all_test_words)
	##feature_vectors=[]
	##print(type(feature_vectors))
	#feature_vectors=np.array([])
	##print(type(feature_vectors))

	#i=0

	#for doc in newsgroups_test.data:
	#	#i=i+1
	#	bow_vector = dictionary.doc2bow(preprocess(doc))
	#	#print("*********************************************************************")
	#	#print(doc)
		
	#	#print(lda_model[bow_vector])
	#	#print("*********************************************************************")          
	#	distribution=lda_model.get_document_topics(bow_vector, minimum_probability=0.0, minimum_phi_value=None, per_word_topics=False)
	#	onerow=[]
	#	for j in range(20):
	#		onerow.append(distribution[j][1])
	#	onerow=np.array(onerow)f

	#	#print(type(feature_vectors))
	#	if(feature_vectors.size==0):
	#		feature_vectors=onerow
	#	else:
	#		feature_vectors=np.vstack((feature_vectors,onerow))

	#	del onerow
	#	#for index, score in sorted(lda_model[bow_vector], key=lambda tup: -1*tup[1]):
	#	#	#print(index)
	#	#	#print("Scojre: {}\t Topic: {}".format(score, lda_model.print_topic(index)))
 # #          list_of_prob=lda_model.show_topic(index, len(bow_vector))
 # #          k
	#	#	print(len(bow_vector))
	#	#	print(len(lda_model.show_topic(index, len(bow_vector))))
	#	#	print(lda_model.show_topic(index, len(bow_vector)))
	#	#if i>=3:
	#	#	break

	##print(feature_vectors)
	#print(feature_vectors.shape)
	#np.save("input2tsne",feature_vectors)


    #input2tsne is a matrix of nxd where n is the number of documents and d is the number of topics (=20). Each cell in the matrix corresponds to probability a specific document belongs to that topic.
    feature_vectors=np.load("input2tsne.npy")
	##3-dimensional=manifold.tsne(n_components=2, perplexity=30.0, early_exaggeration=12.0, learning_rate=200.0, n_iter=1000, n_iter_without_progress=300, min_grad_norm=1e-07, metric='euclidean', init='random', verbose=0, random_state=none, method='barnes_hut', angle=0.5).fit_transform(feature_vectors)
	
    #three_dimensional is the output of TSNE (it is a matrix of nX3 where n is the number of documents
    three_dimensional=tsne(n_components=3).fit_transform(feature_vectors)
	for k in range(10):
        #printing feature vectors of only first 10 documents (in 3 dimensions)
		print(three_dimensional[k])

        #below code is just an example of how to plot a 3-D graph 
    #fig = plt.figure(figsize=plt.figaspect(0.5))
    #randnums= np.random.rand(10,3)
    #print(randnums)
    #x=randnums[:,0]
    #y=randnums[:,1]
    #z=randnums[:,2]
    #triang = mtri.Triangulation(x, y)
    #xmid = x[triang.triangles].mean(axis=1)
    #ymid = y[triang.triangles].mean(axis=1)
    #min_radius = 0.25
    #mask = np.where(xmid**2 + ymid**2 < min_radius**2, 1, 0)
    #triang.set_mask(mask)
    #ax = fig.add_subplot(1, 2, 2, projection='3d')
    #ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
    #plt.show()



if __name__ == "__main__":
	main()	