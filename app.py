from flask import Flask, render_template
import db_controller

app = Flask(__name__)

active_database_connection = None
TEST_COLLECTION = "TEST"
ZILLOW_COLLECTION = "ZILLOW"


@app.route('/')
def hello_world():
    global active_database_connection
    db_controller.connect_to_database()
    active_database_connection = db_controller.get_db_connection()
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run()
