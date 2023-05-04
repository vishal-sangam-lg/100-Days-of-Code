# Using sqlite3 and sql without any package

# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # Books schema cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,
# # author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# # Adding a row
# # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# # db.commit()


# flask_sqlalchemy CRUD operations

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
with app.app_context():
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        # Optional: this will allow each book object to be identified by its title when printed.
        def __repr__(self):
            return f'<Book {self.title}>'


    # db.create_all()

    # CREATE RECORD
    # new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # db.session.add(new_book)
    # db.session.commit()

    # # Read operations
    # all_books = db.session.query(Book).all()
    # print(all_books)
    # book = Book.query.filter_by(title="Harry Potter").first()
    # print(book)

    # # Update operations
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()
    # print(db.session.query(Book).all())
    # book_id = 1
    # book_to_update = Book.query.filter_by(id=book_id).first()
    # book_to_update.title = "Harry Potter and the Goblet of Fire"
    # db.session.commit()
    # print(db.session.query(Book).all())

    # Delete Operations
    # book_id = 1
    # book_to_delete = Book.query.filter_by(id=book_id).first()
    # db.session.delete(book_to_delete)
    # db.session.commit()
    # print(db.session.query(Book).all())

