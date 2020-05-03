from flask import Flask, render_template, request, redirect, url_for

import flask_lesson.db as db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("welcome.html")


@app.route("/posts/<int:post_id>")
def get_post(post_id: int):
    post = db.posts.get(post_id)

    if not post:
        return render_template(
            "404.jinja2", msg="The post you requested was not found."
        )

    return render_template("post.jinja2", post=post)


@app.route("/posts/new")
def new_post():
    return render_template("new_post.jinja2")


@app.route("/posts/add", methods=["post"])
def add_post():
    title = request.form.get("title")
    content = request.form.get("content")
    post_id = len(db.posts)

    db.posts[post_id] = {"id": post_id, "title": title, "content": content}

    return redirect(url_for("get_post", post_id=post_id))


if __name__ == "__main__":
    app.run(debug=True)
