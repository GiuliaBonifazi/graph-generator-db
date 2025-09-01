from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from db import populate_all, get_database, \
  Report, select_all_criteria, \
  criterion_to_json, select_all_reports, report_to_json, \
  insert_report

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"])
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
<p>{Report.query.all()}</p>
"""

@app.route("/get_criteria")
def get_criteria():
  criteria = select_all_criteria()
  return jsonify([criterion_to_json(c) for c in criteria])

@app.route("/get_reports")
def get_reports():
  reports = select_all_reports()
  return jsonify([report_to_json(r) for r in reports])

@app.route("/add_reports", methods = ["POST"])
@cross_origin(origin='http://localhost:5173')
def add_reports():
  data = request.get_json()
  for report in data:
    insert_report(report)
  return jsonify({'message': data})