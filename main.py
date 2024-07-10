from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def home_page():
    data = requests.get("https://api.npoint.io/7d06d7fce65882965a4a").json()
    author = "Ken Muiruri"
    return render_template("index.html", all_posts=data, author=author)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")
@app.route('/home/blog/<num>')
def get_blog(num):
    data = requests.get("https://api.npoint.io/7d06d7fce65882965a4a").json()
    return render_template("post.html", post=data[int(num) - 1])


if __name__ == "__main__":
    app.run(debug=True)
