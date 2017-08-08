from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("hello")
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run()
