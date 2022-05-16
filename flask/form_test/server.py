from flask import Flask, render_template, request, redirect, session #added session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for sevcurity purposes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=(['POST']))
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # NEVER RENDER A TEMPLATE ON A POST REQUEST
    # Instead we will redirect to our index route
    return redirect('/show')

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=['useremail'])

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
