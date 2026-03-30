from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    items = ["Apple", "Orange", "Pineapple"]
    return render_template("example.html", items=items)

@app.route('/user/<name>')
def user(name):
    return render_template("example.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)