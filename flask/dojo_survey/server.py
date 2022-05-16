from flask import Flask, render_template, request, session, redirect
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
app.secret_key='test'
print("show me the money")


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    # print("show me the money")
    return render_template("index.html")


@app.route('/submit_new', methods=['POST'])
def submit_new():
    session['user_name'] = request.form['user_name']
    session['user_location'] = request.form['user_location']
    session['user_fav_lang'] = request.form['user_fav_lang']
    session['user_comments'] = request.form['user_comments']
    # print("show me the money")
    return redirect('/show')


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


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
