from flask import Flask, render_template

import flask_lesson.db as db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("welcome.html")


@app.route("/posts/<int:post_id>")
def get_post(post_id: int):
    post = db.posts.get(post_id)

    if post is None:
        return render_template("404.html")

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
