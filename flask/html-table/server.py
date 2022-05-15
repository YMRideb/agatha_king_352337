# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# This will change locations in the future


@app.route("/")
def home():
    first_name = "Amos"
    last_name = "Burton"

    users = [                                           # this is list containing all the dicts
        {'first_name': 'Michael', 'last_name': 'Choi'}, #each of the moustache braces contain a dict
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template("index.html", first_name = first_name, l_n = last_name, list_users = users)

@app.route('/users2')
def users2():
    users2 = [                                           # this is list containing all the dicts
        # each of the moustache braces contain a dict
        {'first_name': 'James', 'last_name': 'Holden', 'id': 987654},
        {'first_name': 'Chrisjen', 'last_name': 'Avasarala', 'id': 654321},
        {'first_name': 'Naomi', 'last_name': 'Nagata', 'id': 456789},
        {'first_name': 'Alex', 'last_name': 'Kamal', 'id': 234567},
        {'first_name': 'Beau', 'last_name': 'Currier', 'id': 756590},
        {'first_name': 'Danny', 'last_name': 'ONeal', 'id': 352826},
        {'first_name': 'Yukio', 'last_name': 'Rideb', 'id': 352337},
]
    return render_template("users2.html", users = users2)

@app.route('/html-table')
def html_table():
    users1 = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template("html_table.html", users = users1)


# # The "@" decorator associates this route with the function immediately following
# @app.route('/')
# def users_table():
#     users = users_table
#     return '<h1>Hello World!</h1>'  # Return the string 'Hello World!' as a response
#     print (users_table)
#     return users_table


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

