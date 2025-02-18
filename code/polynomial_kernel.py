# -*- coding: utf-8 -*-
"""polynomial_kernel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KV94H7jBxg2qubbN7JlhjSo-MimthCav
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
from sklearn import svm, preprocessing
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from joblib import dump, load
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

X_train = np.load('/content/drive/MyDrive/828C/proj2/part1/data/MNIST/X_train.npy')
y_train = np.load('/content/drive/MyDrive/828C/proj2/part1/data/MNIST/y_train.npy')
X_test = np.load('/content/drive/MyDrive/828C/proj2/part1/data/MNIST/X_test.npy')
y_test = np.load('/content/drive/MyDrive/828C/proj2/part1/data/MNIST/y_test.npy')

degree_list = list(range(1,11))
train_accuracy = []
test_accuracy = []

for degree_ in degree_list:
  svclassifier = svm.SVC(kernel='poly', degree=degree_)
  svclassifier.fit(X_train, y_train)
  train_acc = svclassifier.score(X_train, y_train)
  train_accuracy.append(train_acc)
  print('Train accuracy: ', train_acc)

  test_acc = svclassifier.score(X_test, y_test)
  test_accuracy.append(test_acc)
  print('Test accuracy: ', test_acc)

plt.plot(degree_list, train_accuracy, color='b', label='Training accuracy')
plt.plot(degree_list, test_accuracy, color='r', label='Test accuracy')
plt.xlabel('Degree of polynomial')
plt.ylabel('Accuracy')
plt.title('Polynomial kernel - Vanilla - Accuracy vs Degree')
plt.legend()
plt.savefig('/content/drive/MyDrive/828C/proj2/part1/plots/polynomial_kernel_vanilla.png')
plt.show()

svclassifier = svm.SVC(kernel='poly', degree=2)
svclassifier.fit(X_train, y_train)  
vanilla_train_acc = svclassifier.score(X_train, y_train)
vanilla_test_acc = svclassifier.score(X_test, y_test)

n_components_list = [0.5, 0.6, 0.7, 0.8, 0.9]
train_accuracy = []
test_accuracy = []
components = []

for n_components_ in n_components_list:
  pca = PCA(n_components=n_components_, svd_solver="full")
  X_train_pca = pca.fit_transform(X_train)
  components.append(X_train_pca.shape[1])
  X_test_pca = pca.transform(X_test)

  svclassifier.fit(X_train_pca, y_train)  

  train_acc = svclassifier.score(X_train_pca, y_train)
  print('Train accuracy: ', train_acc)
  train_accuracy.append(train_acc)

  test_acc = svclassifier.score(X_test_pca, y_test)
  print('Test accuracy: ', test_acc)
  test_accuracy.append(test_acc)

plt.plot(components, train_accuracy, color='b', label='Training accuracy')
plt.plot(components, test_accuracy, color='g', label='Test accuracy')
plt.axhline(y = vanilla_train_acc, color = 'r', label='Vanilla training accuracy')
plt.axhline(y = vanilla_test_acc, color = 'c', label='Vanilla test accuracy')
plt.xlabel('Number of principal components')
plt.ylabel('Accuracy')
plt.title('Polynomial kernel - PCA - Accuracy vs No. of Principal Components')
plt.legend()
plt.savefig('/content/drive/MyDrive/828C/proj2/part1/plots/polynomial_kernel_pca.png')
plt.show()

n_components_list = list(range(2, 10))
train_accuracy = []
test_accuracy = []
components = []


for n_components_ in n_components_list:
  lda = LinearDiscriminantAnalysis(n_components=n_components_)  
  X_train_lda = lda.fit_transform(X_train, y_train)
  components.append(X_train_lda.shape[1])
  X_test_lda = lda.transform(X_test)

  svclassifier.fit(X_train_lda, y_train)

  # dump(linear_clf_lda, '/content/drive/MyDrive/828C/proj2/models/linear_kernel_svm_lda_' + str(n_components_) + '.joblib') 
  # y_pred = linear_clf_lda.predict(X_test_lda)
  train_acc = svclassifier.score(X_train_lda, y_train)
  print('Train accuracy: ', train_acc)
  train_accuracy.append(train_acc)

  test_acc = svclassifier.score(X_test_lda, y_test)
  print('Test accuracy: ', test_acc)
  test_accuracy.append(test_acc)

plt.plot(components, train_accuracy, color='b', label='Training accuracy')
plt.plot(components, test_accuracy, color='g', label='Test accuracy')
plt.axhline(y = vanilla_train_acc, color = 'r', label='Vanilla training accuracy')
plt.axhline(y = vanilla_test_acc, color = 'c', label='Vanilla testing accuracy')
plt.xlabel('Number of linear discriminants')
plt.ylabel('Accuracy')
plt.title('Polynomial kernel - LDA - Accuracy vs Linear Discriminants')
plt.legend()
plt.savefig('/content/drive/MyDrive/828C/proj2/part1/plots/polynomial_kernel_lda.png')
plt.show()