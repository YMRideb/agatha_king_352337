from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.friends_model import Friend

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    # print(friends)
    return render_template("index.html", friends=friends)


@app.route("/test")
def test_route():
    friends = Friend.get_all()
    return render_template("test.html", friends=friends)

# relevant code snippet from server.py


@app.route("/users/<int:id>")
def show_user(id):
    data = {
        "id": id
    }
    friends = Friend.get_one(data)
    return render_template("users.html", friends=friends)





@app.route('/create_user', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name1": request.form["name1"],
        "name2": request.form["name2"],
        "email_address": request.form["email_address"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.create(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route('/update_user', methods=["POST"])
def user_update():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name1": request.form["name1"],
        "name2": request.form["name2"],
        "email_address": request.form["email_address"],
        "id": request.form["id"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.update(data)
    # Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route("/users/delete/<int:id>")
def delete_user(id):
    data = {
        "id": id
    }
    Friend.delete(data)
    return redirect('/')
