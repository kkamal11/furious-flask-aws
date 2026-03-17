import os
from flask import Flask, render_template
from dotenv import load_dotenv

from models.models import db, Book

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # creates tables
    app.run(debug=True)
