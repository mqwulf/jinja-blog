from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
all_posts = response.json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<num>')
def get_post(num):
    return render_template("post.html", posts=all_posts, num=int(num))

if __name__ == "__main__":
    app.run(port=6500, debug=True)
