from life import app, path_image
from life.models import Category, Post
from flask import render_template

@app.context_processor
def category_context():
    category_list=Category.query.all()
    return dict(category_list=category_list)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/topics/<namecat>')
def category_post(namecat):
    category=Category.query.filter(Category.slug_category==namecat).first()
    post_list=category.posts.all()
    category_name=category.category_name
    return render_template("post_list.html", post_list=post_list, namecat=namecat, category_name=category_name, path_image=path_image)

@app.route('/topics/<namecat>/<post_title>')
def post(post_title, namecat):
    category=Category.query.filter(Category.slug_category==namecat).first()
    post_one=category.posts.filter(Post.title==post_title).first()
    return render_template("post.html", post=post_one)
