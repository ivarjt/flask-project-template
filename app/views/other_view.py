from app import app
from flask import render_template

@app.route("/other_view_file")
def other():
    return "Just to show that you can have multiple view files. Good structuring practice to use multiple view files when you have a lot of routes."