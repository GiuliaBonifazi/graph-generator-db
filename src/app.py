from flask import Flask, jsonify
from flask_cors import CORS
from db import populate_all, get_database, \
  GraphType, Criterion, select_all_criteria, \
  criterion_to_json, select_all_reports, report_to_json

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = get_database()
db.init_app(app)

@app.cli.command('init-db')
def init_db():
  db.create_all()
  populate_all()

@app.route("/")
def hello_world():
  return f"""
<p>{GraphType.query.all()}yay</p>
<p>{Criterion.query.all()}</p>
"""

@app.route("/get_criteria")
def get_criteria():
  criteria = select_all_criteria()
  return jsonify([criterion_to_json(c) for c in criteria])

@app.route("/get_reports")
def get_reports():
  reports = select_all_reports()
  return jsonify([report_to_json(r) for r in reports])

@app.route("/add_reports")
def add_reports():
  return