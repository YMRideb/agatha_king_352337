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
```python -m pipenv shell
```
- Folder Structure
    -Pipfile
    -Pipfile.lock
    -server.py
    -templates
    -static
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


*******************************************************************************
<!-- based on the folder structure on the right -->
<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">