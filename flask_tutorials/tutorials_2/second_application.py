from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/welcome/<name>')
def welcome(name):
    return 'welcome %s' % name


@app.route('/Unauthorized')
def Unauthorized():
    return 'Unauthorized User'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        if user == "mth":
            return redirect(url_for('welcome', name=user))
        else:
            return redirect(url_for('Unauthorized'))


if __name__ == '__main__':
    app.run(debug=True)
