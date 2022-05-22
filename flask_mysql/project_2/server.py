from users_crud2 import app
from flask import Flask

if __name__ == "__main__":
    app.run(debug=True)






# @app.route("/new")
# def create_new_user():

#     return render_template("new.html" )



# @app.route('/new/create_user', methods=["POST"])
# def create_user():
#     data = {
#         "fname": request.form["fname"],
#         "lname": request.form["lname"],
#         "email": request.form["email"]
#     }

#     User.save(data)
#     return redirect('/')

