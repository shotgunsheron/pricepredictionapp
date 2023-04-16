import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV, StratifiedKFold
import joblib
import pickle


class Categorizer:

	def __init__(self, data):
		self.data = data

	def train(self):
		vectorizer = CountVectorizer()

		data = self.data
		# Split the data into training and testing sets
		train_data = data.sample(frac=0.8, random_state=1)
		test_data = data.drop(train_data.index)

		# Create a CountVectorizer to convert the text into a matrix of word counts

		# Fit the vectorizer on the training data
		vectorizer.fit(train_data['product_name'])

		# Transform the text data into feature vectors
		X_train = vectorizer.transform(train_data['product_name'])
		X_test = vectorizer.transform(test_data['product_name'])

		# Perform hyperparameter tuning with GridSearchCV
		parameters = {'alpha': [0.1, 1.0, 10.0]}
		cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
		clf = GridSearchCV(MultinomialNB(), parameters, cv=cv)
		clf.fit(X_train, train_data['category'])

		self.clf = clf.best_estimator_
		joblib.dump(self.clf, "./clf.joblib")
		self._vectorizer = vectorizer
		with open('vectorizer.pkl', 'wb') as fp:
			pickle.dump(self._vectorizer, fp)

	def load(self):
		self.clf = joblib.load('./clf.joblib')

	def predict(self, new_sentence):
		with open('vectorizer.pkl', 'rb') as fp:
			self._vectorizer = pickle.load(fp)
		self.clf = joblib.load('./clf.joblib')

		new_sentence_features = self._vectorizer.transform([new_sentence])
		prediction = self.clf.predict(new_sentence_features)
		return prediction[0]
