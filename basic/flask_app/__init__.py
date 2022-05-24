from flask import Flask
app = Flask(__name__)
app.secret_key="foorikoori"

DATABASE = 'dojo_survey_schema'