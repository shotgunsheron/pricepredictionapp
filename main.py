from flask import Flask, render_template, request
from allTheML import getPrice

app = Flask(__name__)

USD_TO_INR_CONVERSION = 81.85
INR_TO_USD_CONVERSION = 0.012


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
	print(request.form.to_dict())

	# category = request.form.to_dict()['category']  #sentence about the category
	# rating = request.form.to_dict()['rating']  # number from 0-5
	# mPrice = request.form.to_dict()['mPrice']  # price in USD
	data = request.get_json(force=True)
	
	category = data['category']
	rating = data['rating']
	mPrice = data['mPrice']
	
	rating = int(rating)

	assert rating >= 0 and rating <= 5

	mPrice = round(float(mPrice) * USD_TO_INR_CONVERSION, 2)

	assert mPrice >= 0

	print(category, rating, mPrice)

	# process_form(category, rating, mPrice)
	res = getPrice(category,mPrice, rating)
	return str(
	 round(res[1] * INR_TO_USD_CONVERSION, 2)) + ',' + res[0]


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
