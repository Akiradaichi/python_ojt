import profile
import pymysql
from sqlalchemy import Integer
from app import app
from db import mysql
from flask_bcrypt import Bcrypt
from flask import flash, jsonify
from flask import render_template, request, Flask, request, redirect, url_for, session
from flask_restx import Api
from wtforms import Form, StringField,  PasswordField, validators , DateTimeField
from werkzeug.security import generate_password_hash
app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' \
                            in request.form:
        email = request.form['username']
        password1 = request.form['password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        result = cursor.execute('SELECT * FROM users WHERE email = %s ',
                                (email))
        if result > 0:
            account = cursor.fetchone()
            password = account['password']
            if bcrypt.check_password_hash(password, password1) is True:
                session['login'] = True
                session['id'] = account['id']
                session['username'] = account['name']
                session['type'] = account['type']
                if session['type'] == "0":
                    return redirect(url_for('admin'))
                elif session['type'] == "1":
                    return redirect(url_for('user'))
            else:
                flash("worng password or user", 'danger')
                return redirect("login")
    return render_template('index.html')

@app.route('/pythonlogin/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    type = StringField('type')
    phone = StringField('phone')
    address = StringField('address')
    dob = DateTimeField('dob')


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['name']
        email = request.form['email']
        password = form.password.data
        type = request.form['type']
        phone = request.form['phone']
        address = request.form['address']
        dob = request.form['dob']
        return name, email, password, type, phone, address, dob
    return render_template('user_create.html', form=form)


@app.route('/add', methods=['POST'])
def add_user():
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _password = _json['pwd']
        # validate the received values
        if _name and _email and _password and request.method == 'POST':
            #do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)"
            data = (_name, _email, _hashed_password,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/users')
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT  id user_id,name user_name ,email user_email ,password user_password  FROM users")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/users/<int:id>')
def userid(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id user_id ,name user_name ,email user_email ,password user_password  FROM users WHERE id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['PUT'])
def update_user():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _password = _json['pwd']
        # validate the received values
        if _name and _email and _password and _id and request.method == 'PUT':
            #do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "UPDATE usesr SET name=%s, email=%s, password=%s WHERE id=%s"
            data = (_name, _email, _hashed_password, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(debug=True)