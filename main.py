from flask import Flask
from schema import query_result, book_result

app = Flask(__name__)


@app.get("/")
def index():
    return {"data": query_result.data}


@app.get("/book")
def get_book():
    return {"data": book_result.data}


if __name__ == "__main__":
    app.run()
