from flask import Flask, render_template, request, redirect, session  # added session

app = Flask(__name__)
app.secret_key = "temp_key"


@app.route('/')
def index():
    if not 'count' in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['count'] += 1
    return redirect('/')



# @app.route('/add_two')
# def add_two():
#     session['count'] += 1
#     return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

# # set a secret key for sevcurity purposes
# app.secret_key = 'keep it secret, keep it safe'


# @app.route('/')
# def index():
#     if 'count' in session:
#         session['count'] += 1
#     else:
#         session['count'] = 0
#     return render_template("index.html")
#     # return redirect('/')

# # @app.route('/add_two')




# # @app.route('/users', methods=(['POST']))
# # def create_user():
# #     print("Got Post Info")
# #     session['username'] = request.form['name']
# #     session['useremail'] = request.form['email']
# #     return redirect('/show')


# # @app.route("/show")
# # def show_user():
# #     return render_template("show.html", name_on_template=session['username'], email_on_template=['useremail'])
    
# # @app.route("/counter")
# # def click_btn()
    
# #     # print("Showing the User Info From the Form")
# #     # print(request.form)


# if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
#     app.run(debug=True)    # Run the app in debug mode.
