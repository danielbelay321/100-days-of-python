from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    urls = 'https://api.npoint.io/30e19a1dcb30815b1025'
    response_link = requests.get(urls)
    response_link.raise_for_status()

    posts = response_link.json()
    return render_template("index.html", posts=posts)

@app.route('/post/<int:id>')
def post(id):
    urls = 'https://api.npoint.io/30e19a1dcb30815b1025'
    response_link = requests.get(urls)
    response_link.raise_for_status()

    posts = response_link.json()
    return render_template("post.html", posts=posts, id=id)

if __name__ == "__main__":
    app.run(debug=True)
