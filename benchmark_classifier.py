import pickle
import os
import numpy as np
import time
from sklearn.feature_extraction.text import TfidfVectorizer

model_file = "/home/kali/Master_Thesis/saved_models/3_3_20k_RandomForest.sav"
inPath = "/home/kali/Master_Thesis/dest_files/"
feature_file = open('/home/kali/Master_Thesis/dataset2/3_3_20k_dataset/feature_table', 'rb')

start = time.time()
vocabulary = pickle.load(feature_file)

vectorizer = TfidfVectorizer(input='filename', ngram_range=(3,3), analyzer = 'char', norm = 'l1', vocabulary=vocabulary) #, max_features=20000
clf = pickle.load(open(model_file, 'rb'))

corpus_file = []

for filename in os.listdir(inPath):
    print(filename)
    f = os.path.join(inPath, filename)
    corpus_file.append(f)

X = vectorizer.fit_transform(corpus_file)


y_pred = clf.predict(X)
end = time.time()

total_time = end-start
print("Total time for classification of 20,000 samples:")
print(total_time)
print("Time per sample:")
print(total_time/20000)
