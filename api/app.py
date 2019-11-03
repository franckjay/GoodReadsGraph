from flask import Blueprint, jsonify, request

from GoodReadsGraph import BuildGraph

main = Blueprint('main', __name__)

BigGraph, titles_dict = BuildGraph()

@main.route('/recommend_book', methods=['POST'])
def recommend_book():
    # We get a request from our React App
    _book = request.get_json()
    # We extract the title from our JSON
    try:
        _book_title = _book["title"]
        # We use our dictionary to pull out a book Object
        _book_object = titles_dict[_book_title.lower()]
        # Grab the first entry, return it
        book_list = BigGraph._book2book(_book_object, N=1)
        book = book_list[0]
        # Return the image URL to be displayed on our app
        return jsonify({"image_url": book.image_url})
    except Exception as e:
        return "Error: ", 400
