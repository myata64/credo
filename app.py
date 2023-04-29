from flask import Flask, render_template, request, redirect, url_for
import json
# from utils import get_news, search_movie, get_weather_data
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
	return render_template('home.html')

@app.route('/brends')
def shoes_page():
	return render_template('shoes.html')

@app.route('/account')
def account_page():
	return render_template('account.html')
@app.route('/newbalance')
def newbalance_page():
	return render_template('nb990.html')
@app.route('/submit', methods=['POST'])
def submit():
	name = request.form['name']
	password = request.form['password']

	data = {
		'name': name,
		'password': password
	}
	with open('data.json', 'w') as f:
		json.dump(data, f)

	return f'Привет, {name}! Ваш password - {password} сохранены в json'



if __name__ == '__main__':
	app.run(debug=True)
