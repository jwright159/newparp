import json

from flask import g, render_template, request, redirect, url_for

from charat2.model.connections import use_db
#from charat2.blog import feed

@use_db
def home():
    posts = json.loads(feed())
    return render_template(
        "root/home.html",
        logged_in=g.user is not None,
        posts=posts
    )

