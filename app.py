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


if __name__ == '__main__':
	app.run(debug=True)
