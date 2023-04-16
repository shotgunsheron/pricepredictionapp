from Categorizer import Categorizer
from Model import Model

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


def getPrice(sentence: str, price: float, stars: int) -> tuple[str, float]:
	data_file_path_2 = './data_2.csv'
	data_2 = pd.read_csv(data_file_path_2)[['product_name', 'category']]
	#print(data)
	model_2 = Categorizer(data_2)
	#model_2.train()
	model_2.load()
	category = model_2.predict(sentence)

	data_file_path_1 = './data_1.csv'
	data_1 = pd.read_csv(data_file_path_1)

	model_1 = Model(data_1)
	# model_1.train()
	model_1.load()
	return category, model_1.predict([[category, price, stars]])[0]


#input list
#Category, Manufacturing Price, Rating out of 5 stars
