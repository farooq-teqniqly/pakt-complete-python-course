from flask import Flask
import flask_lesson.db as db
import json

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world!"


@app.route("/posts/<int:post_id>")
def get_post(post_id: int):
    post = db.posts.get(post_id)

    return json.dumps(post)


if __name__ == "__main__":
    app.run(debug=True)
