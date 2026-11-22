from flask import Flask
from models import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "change moi plus tard"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///studyplanner.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def accueil():
    return "study planner fonctionne !"


if __name__ == "__main__":
    app.run(debug=True)
