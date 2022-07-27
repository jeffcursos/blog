
from flask import Flask, render_template, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy (app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now) 

db.create_all()
    

@app.route("/")
def index():
    # Busca no Banco os posts
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/login")
def login():
    posts = Post.query.all()
    return render_template("login.html", posts=posts)

#inserir 2 textos no blog
@app.route("/populate")
def populate():
    post1 = Post(title="Post 1", body="texto do post",author="jef")
    post2 = Post(title="Post 2", body="texto do post2",author="jef")
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    return redirect("/")