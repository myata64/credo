from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home_page():  # put application's code here
	return render_template('home.html')

@app.route('/brends')
def shoes_page():
	return render_template('brends.html')


if __name__ == '__main__':
	app.run()
