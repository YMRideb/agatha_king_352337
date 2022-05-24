from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.survey_dojos_model import DOJO
# from flask_app.models.ninjas_model import Ninja


@app.route('/')
def index():
    print("show me the money")
    return render_template("index.html")


@app.route('/create_new', methods=['POST'])
def create_new():
    session['dojo_name'] = request.form['dojo_name']
    session['dojo_location'] = request.form['dojo_location']
    session['dojo_language'] = request.form['dojo_language']
    session['dojo_comments'] = request.form['dojo_comments']
    session['created_at'] = request.form['created_at']
    session['updated_at'] = request.form['updated_at']
    # print("show me the money")
    return redirect('/show')

d
@app.route("/show")
def show_user():
    data = {
        "name": session['user_name'],
        "location": session['user_location'],
        "fav_lang": session['user_fav_lang'],
        "comments": session['user_comments']
    }
    # print("show me the money")
    return render_template("show.html", data=data)






@app.route("/")
def dojos():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all()
    # print(friends)
    return render_template("dojos.html", dojos=dojos)


@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        "id": id
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

    return render_template('show_dojo.html')
