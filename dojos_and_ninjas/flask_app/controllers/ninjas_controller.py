from flask import render_template, redirect, request
from d_and_n import app
from d_and_n.models.dojos_model import Dojo
from d_and_n.models.dojos_model import Ninja


@app.route("/dojos")
def index():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all()
    # print(friends)
    return render_template("dojos.html", dojos=dojos)


@app.route("/dojos/<int:id>")
def show_dojo():
    data = {
        "id": id
    }
    dojos = Dojo.get_one(data)
    return render_template("dojos.html", dojos=dojos)


@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "dojo_new_name": request.form["dojo_new_name"],
    }
    Dojo.create(data)

    return redirect('/')
