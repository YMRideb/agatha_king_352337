from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja


@app.route("/")
def dojos():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all()
    # print(friends)
    return render_template("dojos.html", dojos=dojos)

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        "id" : id
    }
    dojos = Dojo.get_all()
    ninjas = Ninja.get_ninjas_in_dojo(data)
    return render_template("show_dojo.html", dojos=dojos, ninjas=ninjas)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.create(data)

    return render_template('/')
