# checklist
- create a new assignment folder
- navigate ```into``` which assignment you will be working on
- create your virtual env
```py
python -m pipenv install flask #Every time you open that new project folder
```
**WARNING** Your directory needs to contain ```Pipfile.lock``` and ```Pipfile``` 
**WARNING** otherwise your shell will not build or run

- navigate CMD Terminal into virtualenv
```
python -m pipenv shell
```
- Folder Structure or project directory structure
    -"Pipfile"
    -"Pipfile.lock"
    -"server.py"
    -templates  <!-- This is a directory -->
        "index.html"
    -static <!-- This is also a directory -->
        -css <!-- This is a another directory -->
            -"styles.css"
        -js <!-- Can you guess what this is -->
        -img <!-- And the last one you'll need here -->
*******************************************************************************
-server.py file
```py
    from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# This will change locations in the future

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
```

*******************************************************************************            
`
            <!-- based on the folder structure on the right -->
            <!-- linking a css style sheet -->
            <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style.css') }}">
            <!-- linking a javascript file -->
            <script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
            <!-- linking an image -->
            <img src="{{ url_for('static', filename='my_img.png') }}">
            ```
*******************************************************************************
    this is for mySQL
    ```py
    python -m pipenv install PyMySQL flask
    ```

C R U D
r e p e
e a d l
a d a e
t   t t
e   e e

or Create
   Read
   Update
   Delete
   Always want to use WHERE and id = #
    / -> Create
    INSERT INTO table_name (column_names,) VALUES (actual_values,);
    / -> Read
    SELECT columns FROM table_name WHERE?;
    SELECT * FROM users;
    / -> Update
    UPDATE table_name SET column_name = new_value,  column_name1 = new_value2;
    UPDATE table_name SET first_name = "yuki", last_name = 'kazuma';
    / -> DELETE FROM table_name WHERE id =  

