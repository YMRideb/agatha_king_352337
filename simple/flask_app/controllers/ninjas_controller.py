from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos_model import Dojo

@app.route("/ninjas")
def ninjas():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all()
    # print(friends)
    return render_template("ninjas.html", dojos=dojos)


@app.route("/ninjas/<int:id>")
def show_ninja():
    data = {
        "id": id
    }
    dojos = Dojo.get_one(data)
    return render_template("dojos.html", dojos=dojos)


@app.route('/create_ninjas', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "first_name": request.form["first_name"],
        "first_name": request.form["first_name"],
        "first_name": request.form["first_name"],
    }
    Dojo.create(data)

    return redirect('/dojos')
