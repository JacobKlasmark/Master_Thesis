import os
import time
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import dump_svmlight_file
from numpy import savetxt

vectorizer = TfidfVectorizer(input='filename', ngram_range=(4,4), analyzer = 'char', norm = 'l1', max_features=20000)

corpus_file = []
directory = '/home/kali/Master_Thesis/Obfuscated_out/'

translation_table = open('/home/kali/Master_Thesis/dataset2/4_4_20k_dataset/class_translation', "a")
feature_table = open('/home/kali/Master_Thesis/dataset2/4_4_20k_dataset/feature_table', "w")

classification_array = []
classification = 0

t0 = time.time()
for root in os.listdir(directory):
    dir = os.path.join(directory, root)
    print(root)
    translation_table.write(root + "," + str(classification) + "\n")
    print(dir)
    for filename in os.listdir(dir):
        print(filename)
        f = os.path.join(dir, filename)
        corpus_file.append(f)
        classification_array.append(classification)
    classification = classification + 1
translation_table.close()
del(translation_table)

t2 = time.time()
print(t2-t0)

X = vectorizer.fit_transform(corpus_file)

t1 = time.time()
print(t1-t2)


pickle.dump(vectorizer.vocabulary_, feature_table)

feature_table.close()
del(feature_table)

test_out_svm = '/home/kali/Master_Thesis/dataset2/4_4_20k_dataset/4_4_20k_svm'
dump_svmlight_file(X, classification_array, test_out_svm)
