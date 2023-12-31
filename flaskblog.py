
# hello world web page.

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/home")
@app.route("/")
def hello():
    return (render_template('home.html'))


@app.route("/about")
def about():
    return (render_template('about.html'))


if __name__ == '__main__':
    app.run(debug=True)
