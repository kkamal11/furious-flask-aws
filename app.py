import os
from flask import Flask, render_template, request, redirect, flash
from dotenv import load_dotenv

from models.models import db, Book

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = "0x375c24f60ec47eefed8df4a72332fbf4329a53'"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def root():
    books = Book.query.order_by(Book.id).all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    price = request.form["price"]

    new_book = Book(title, author, price)

    db.session.add(new_book)
    db.session.commit()

    flash(f"Book {title} added successfully!", "success")

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash(f"Book {book.title} deleted successfully", "danger")
    return redirect("/")


@app.route("/update/<int:id>", methods=["POST"])
def update_book(id):
    book = Book.query.get_or_404(id)

    book.title = request.form["title"]
    book.author = request.form["author"]
    book.price = request.form["price"]

    db.session.commit()

    flash(f"Book {book.title} updated successfully!", "info")

    return redirect("/")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # creates tables  info warning
    app.run(debug=True)
