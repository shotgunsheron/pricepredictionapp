import pandas as pd
from Categorizer import Categorizer

data = pd.read_csv('data_2.csv')

categorizer = Categorizer(data)
categorizer.train()

new_sentence = "Samsung galaxy S22 Ultra Phone OLED"
prediction = categorizer.predict(new_sentence)
print(prediction)
