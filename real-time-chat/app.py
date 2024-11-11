from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
socketio = SocketIO(app)

users = {}


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if username in users:
            error = "نام کاربری قبلا ثبت شده است !"
        elif password != confirm_password:
            error = "پسورد ها مطایقت ندارند !"
        else:
            users[username] = {
                'username': username,
                'password': password,
            }
            return redirect(url_for('login'))

        return render_template('register.html', error=error)

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('index'))

        error = 'نام کاربری یا پسورد اشتباه است !'
        return render_template('login.html', error=error)

    return render_template('login.html')



if __name__ == '__main__':
    app.secret_key = 'adlwqje234FJEDOWEedwsflwhj5i4353ioh645'
    socketio.run(app, debug=True)
