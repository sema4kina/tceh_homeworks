from flask import Flask, json, request, abort, jsonify
import locale
from wtforms import StringField, validators, ValidationError, PasswordField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'This is a secret key',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})


def password_validator(form, field):
    if field.data != form.data['password']:
        raise ValidationError('You entered incorrect password. Try one mor time.')


class UserForm(FlaskForm):
    email = StringField(validators=[
        validators.Email(),
        validators.InputRequired(message='This field can\t be empty')
    ])
    password = PasswordField(validators=[
        validators.InputRequired(message='This field can\t be empty'),
        validators.length(min=6)
    ])
    password_confirmation = StringField(validators=[
        password_validator
    ])


# Task 1 - work with locales

@app.route('/locales')
def print_locales():
    first_list = ['ru', 'en', 'it']
    result_dict = {}
    alias = locale.locale_alias
    for element in first_list:
        if element in alias.keys():
            result_dict.update({element: alias[element]})
    return json.dumps(result_dict, sort_keys=True, indent=4)


# Task 2 - sum of two arguments

@app.route('/sum/<int:first>/<int:second>')
def summing(first, second):
    return str(first + second)


# Task 3 - greet user

@app.route('/greet/<user_name>')
def greet_user(user_name):
    return 'Hello, %s' % user_name


# Task 4 - user form

@app.route('/form/user', methods=['POST'])
def post_data():
    if request.method == 'POST':
        user_form = UserForm(request.form)
        if user_form.validate():
            return jsonify({'status': 0, 'errors': user_form.errors})
        else:
            return jsonify({'status': 1, 'errors': user_form.errors})


# 5 Get file content

@app.route('/serve/<path:filename>', methods=['GET'])
def get_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run()
