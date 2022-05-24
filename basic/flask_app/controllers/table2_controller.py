from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja
from flask_app.controllers import dojos_controller


@app.route("/ninjas")
def ninjas():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all()
    # print(friends)
    return render_template("ninjas.html", dojos=dojos)


# @app.route("/ninjas/<int:id>")
# def show_ninja():
#     data = {
#         "id": id
#     }
#     dojos = Dojo.get_one(data)
#     return render_template("dojos.html", dojos=dojos)


@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.create(data)
    print(request.form)
    return redirect('/')
