from flask import render_template, request, redirect
from users_crud2 import app
from users_crud2.models.todos import list_todos
from users_crud2.models.user import list_users


@app.route("/todos/new")
def display_todo_form():
    return render_template("todo.html", list_users=list_users)


@app.route("/todos/add", methods=['POST'])
def add_new_todo():
    print(request.form)
    new_todo = {
        "Description": request.form['todo_description'],
        "todo_status": request.form['todo_status'],
        "user_id": request.form['user_id'],
    }
    list_todos.append(new_todo)
    print(list_todos)
    return redirect("/users")
