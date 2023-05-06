from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# список публикаций
publications = []


class PublicationForm(FlaskForm):
	title = StringField('Заголовок', validators=[DataRequired()])
	content = TextAreaField('Текст', validators=[DataRequired()])
	image = FileField('Изображение')
	submit = SubmitField('Опубликовать')


@app.route('/', methods=['GET', 'POST'])
def index():
	form = PublicationForm()
	if form.validate_on_submit():
		# сохраняем изображение на сервере
		image = form.image.data
		if image:
			filename = image.filename
			image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			image_url = f'/static/images/{filename}'
		else:
			image_url = None

		# создаем новую публикацию
		publication = {'title': form.title.data, 'content': form.content.data, 'image': image_url}

		# добавляем публикацию в список
		publications.append(publication)

		# перенаправляем на главную страницу
		return redirect('/')
	return render_template('index.html', form=form, publications=publications)


if __name__ == '__main__':
	app.run()

# from utils import get_news, search_movie, get_weather_data
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home_page():  # put application's code here
	return render_template('home.html')
@app.route('/shoes')
def shoes_page():
	return render_template('shoes.html')
@app.route('/account')
def account_page():
	return render_template('account.html')
@app.route('/entrance')
def entrance_page():
	return render_template('entrance.html')
@app.route('/registration')
def registration_page():
	return render_template('registration.html')
@app.route('/newbalance')
def newbalance_page():
	return render_template('nb990.html')


@app.route('/submit', methods=['POST'])
def submit():
	email = request.form['email']
	password = request.form['password']

	data = {
		'email': email,
		'password': password
	}

	with open('data.json', 'w') as f:
		json.dump(data, f)

	return f'Привет, {email}! Ваш password - {password} сохранены в json'



# Входит pользователь
@app.route('/entry', methods=['POST'])
def entry_app():
	email = request.form['email']
	password = request.form['password']

	admin_email = 'admin@gmail.com'
	admin_password = 'admin12345'

	with open('data.json', 'r') as f:
		saved_data = json.load(f)

	if email == admin_email and password == admin_password:
		# return 'Вы вошли как админ)'
		return redirect(url_for('home_page'))
	elif email == saved_data['email'] and password == saved_data['password']:
		return 'Вы вошли как пользователь'
	else:
		return 'Данные не совпадают'

if __name__ == '__main__':
	app.run(debug=True)
