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
        return f'Meting({self.uuid},{self.lat},{self.lng},'
