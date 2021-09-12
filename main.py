from flask import Flask
from schema import query_result, book_result

app = Flask(__name__)
# DB Config
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://user:password@hostname/database_name"


@app.get("/")
def index():
    return {"data": query_result.data}


@app.get("/book")
def get_book():
    return {"data": book_result.data}


@app.post("/")
def index_post():
    return "there we go"


if __name__ == "__main__":
    app.run()
