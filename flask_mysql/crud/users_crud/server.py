from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    # print(friends)
    return render_template("index.html", users=users)

@app.route("/new")
def create_new_user():
    
    return render_template("new.html" )



@app.route('/new/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    User.save(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
