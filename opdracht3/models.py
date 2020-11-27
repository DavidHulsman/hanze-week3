from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://nostradavid:ZXASqw12@localhost/iot_metingen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Meting(db.Model):
    __tablename__ = 'metingen'
    id = db.Column(db.Integer, primary_key=True)
    tijdstempel = db.Column(db.DateTime, nullable=False)
    uuid = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Meting {self.meetwaarde}'


class Test(db.Model):
    __tablename__ = 'testen'
    id = db.Column(db.Integer, primary_key=True)
    startdatum = db.Column(db.DateTime, nullable=False)
    einddatum = db.Column(db.DateTime, nullable=True)
    meting = db.relationship(Meting)
    meting_id = db.Column(db.Integer, db.ForeignKey('metingen.id'))
