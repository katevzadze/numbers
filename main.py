from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return ("Hello!")


@app.route("/div3")
def numbers():
    return render_template("numbers.html", title="вывод чисел")


if __name__ == '__main__':
    app.run()
