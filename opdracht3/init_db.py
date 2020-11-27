from sqlalchemy_utils import drop_database, create_database
from models import db, app

create_database(app.config['SQLALCHEMY_DATABASE_URI'])
db.create_all()