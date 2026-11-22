from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Utilisateur(UserMixin, db.Model):
    __tablename__ = "utilisateur"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    mdp_hache = db.Column(db.String(255), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    niveau_etude = db.Column(db.String(100))

    matieres = db.relationship(
        "Matiere", backref="utilisateur", cascade="all, delete-orphan"
    )

    def set_password(self, password):
        self.mdp_hache = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.mdp_hache, password)


class Matiere(db.Model):
    __tablename__ = "matiere"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    coefficient = db.Column(db.Integer, default=1)
    difficulte = db.Column(db.String(20))
    nbr_cours_total = db.Column(db.Integer, default=0)
    nbr_cours_fait = db.Column(db.Integer, default=0)
    pourcentage_maitrise = db.Column(db.Integer, default=0)
    heure_semaine = db.Column(db.Float, default=0)

    id_utilisateur = db.Column(
        db.Integer, db.ForeignKey("utilisateur.id"), nullable=False
    )
