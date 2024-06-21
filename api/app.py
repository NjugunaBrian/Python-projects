from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    { "id": 1, "title": "To kill a mockingbird", "author": "Harper Lee"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]

#GET route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

#GET route to get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)

    return jsonify({"error": "Book not found"}), 404

#POST route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    new_book['id'] = max(book['id'] for book in books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)


         