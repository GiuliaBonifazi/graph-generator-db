from flask import Flask
from db import populate_all, get_database, GraphType, Criterion
app = Flask(__name__)
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