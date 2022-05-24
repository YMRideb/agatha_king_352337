from flask import render_template, redirect, request, session
from flask_app import app
# from flask_app.models.dojos_model import Dojo
# from flask_app.models.ninjas_model import Ninja


@app.route('/')
def hello_world():
    print("show me the money")
    return render_template("index.html")


@app.route('/submit_new', methods=['POST'])
def submit_new():
    session['user_name'] = request.form['user_name']
    session['user_location'] = request.form['user_location']
    session['user_fav_lang'] = request.form['user_fav_lang']
    session['user_comments'] = request.form['user_comments']
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
