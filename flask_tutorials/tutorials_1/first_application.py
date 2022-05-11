from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is our first flask"


if __name__ == '_main_':
    app.run(debug=True)