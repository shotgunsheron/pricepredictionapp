from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

import joblib
import pandas as pd
import numpy as np

import pickle


class Model:

	def __init__(self, data):
		self.data = data

	def getEncoded(self, test_data):
		labelencoder_dict = self.labelencoder_dict
		onehotencoder_dict = self.onehotencoder_dict

		test_encoded_x = None
		for i in range(0, test_data.shape[1]):
			label_encoder = labelencoder_dict[i]
			feature = label_encoder.transform(test_data[:, i])
			feature = feature.reshape(test_data.shape[0], 1)
			onehot_encoder = onehotencoder_dict[i]
			feature = onehot_encoder.transform(feature)
			if test_encoded_x is None:
				test_encoded_x = feature
			else:
				test_encoded_x = np.concatenate((test_encoded_x, feature), axis=1)
		return test_encoded_x

	def train(self):
		data = self.data
		data = data.dropna(axis=0)
		# Choose target and features
		y = data.actual_price

		data

		data_features = [
		 'discounted_price', 'rating'
		]  #list of column names that we want to use as features other than category

		X = data[['category']]
		originalX = X
		self.labelencoder_dict = {}
		self.onehotencoder_dict = {}
		X_train = None

		for i in range(0, X.values.shape[1]):
			label_encoder = preprocessing.LabelEncoder()
			self.labelencoder_dict[i] = label_encoder
			feature = label_encoder.fit_transform(X.values[:, i])
			feature = feature.reshape(X.values.shape[0], 1)
			onehot_encoder = preprocessing.OneHotEncoder(sparse=False)
			feature = onehot_encoder.fit_transform(feature)
			self.onehotencoder_dict[i] = onehot_encoder
			if X_train is None:
				X_train = feature
			else:
				X_train = np.concatenate((X_train, feature), axis=1)
		with open('labelencoder_dict.pkl', 'wb') as fp:
			pickle.dump(self.labelencoder_dict, fp)
		with open('onehotencoder_dict.pkl', 'wb') as fp:
			pickle.dump(self.onehotencoder_dict, fp)

		#print(labelencoder_dict)
		#print(onehotencoder_dict)

		X = self.getEncoded(X.values)
		column_to_be_added = np.array(data[['discounted_price']])

		# Adding column to array using append() method
		X = np.append(X, column_to_be_added, axis=1)
		column_to_be_added = np.array(data[['rating']])

		X = np.append(X, column_to_be_added, axis=1)

		#print(X)
		# split data into training and validation data, for both features and target
		# The split is based on a random number generator. Supplying a numeric value to
		# the random_state argument guarantees we get the same split every time we
		# run this script.

		#train_X, val_X, train_y, val_y = train_test_split(originalX, y,random_state = 0)

		#val_X=getEncoded(val_X.values,labelencoder_dict,onehotencoder_dict)

		#val_X = val_X.values.tolist()
		#print(val_X)

		forest_model = RandomForestRegressor(random_state=1)
		forest_model.fit(X, y)
		#predictions = forest_model.predict(val_X)

		#print(predictions)
		#print(predictions)
		#print(mean_absolute_error(val_y, predictions))

		#print(data)
		import joblib
		joblib.dump(forest_model, "./model.joblib")

		self.forest_model = forest_model

	def predict(self, features):
		forest_model = self.forest_model
		data = pd.DataFrame(features,
		                    columns=['category', 'discounted_price', 'rating'])
		X = self.getEncoded(data[['category']].values)
		column_to_be_added = np.array(data[['discounted_price']])

		# Adding column to array using append() method
		X = np.append(X, column_to_be_added, axis=1)
		column_to_be_added = np.array(data[['rating']])

		X = np.append(X, column_to_be_added, axis=1)
		#print(X)
		prediction = forest_model.predict(X)
		return prediction

	def load(self):
		self.forest_model = joblib.load('./model.joblib')
		with open('labelencoder_dict.pkl', 'rb') as fp:
			self.labelencoder_dict = pickle.load(fp)
		with open('onehotencoder_dict.pkl', 'rb') as fp:
			self.onehotencoder_dict = pickle.load(fp)
