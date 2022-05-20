from flask import render_template
from users_crud2 import app
from users_crud2.models.user import list_users
from users_crud2.models.todos import list_todos

@app.route("/", methods=['GET'])
def home():
    first_name = "Josephus"
    last_name = "Miller"
    #list_nums = [10, 20, 30, 40, 50]
    return render_template("index.html", first_name=first_name, last_name=last_name,)


@app.route("'users", methods=["GET"])
def UsErS():
    return render_template("users.html", users=list_users)


@app.route("/users/<int:user_id>")
def get_user_by_id(user_id):
    for user in list_users:
        if user['id'] == user_id:
            current_Todos = []
            for todo in list_todos:
                if user_id == todo['user_id']:
                    current_Todos.append(todo)
                return render_template("userID.html", user=user, error_message=False, u_id=user_id, current_todos=current_Todos)
    return render_template("userID.html", user=user, error_message=True, u_id=user_id)
