from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import SelectField, validators
from flask.json import jsonify

app = Flask(__name__)
app.debug = True

class ContactForm(FlaskForm):
    name = SelectField(validators=[validators.Length(min=4, max=25)])
    email = SelectField(validators=[validators.Length(min=6,max=35),validators.Email])


# Не мое решение (так как вообще задачу не понял) 
@app.route('/locales', methods =['GET', 'POST'])
def my_dict():
    my_locale = {'ru': 'russian', 'en': 'english', 'it': 'italian'}
    return jsonify(my_locale)





@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('Всё забись', 200)
        else:
            return ('ОШИБКА', 400)

    if request.method == 'GET':
        return 'HELLO MOTHERFUCKER', 200


@app.route('/serve/<path:filename>')
def patch(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.readlines()
            return str(text)

    except Exception as error:
        return 'Ошибка: {}'.format(error)




@app.route('/summ/<int:first>/<znak>/<int:second>')
def summ(first, second, znak):
    sum = eval('{}{}{}'.format(first, znak, second))
    return 'Сумма ваших чисел равна {}'.format(sum)



#Задание 3
@app.route('/greet/<user_name>')
def hello(user_name):
    return 'Hello {} '.format(user_name)

app.run()