from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#define the book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "created_at": self.created_at.isoformat()
        }

#create the database tables
with app.app_context():
    db.create_all()

#GET route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

#GET route to get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

#POST route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

#PUT route to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    db.session.commit()
    return jsonify(book.to_dict())

#DELETE route to delete an existing book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)


         