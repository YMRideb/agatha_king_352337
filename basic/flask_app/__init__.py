from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key="foorikoori"
# DATABASE = #table1 and table2 schema > table(s)