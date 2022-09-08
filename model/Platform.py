from flask_sqlalchemy import SQLAlchemy

# config
from config import app_config, app_active
config = app_config[app_active]

db = SQLAlchemy(config.APP)

class Platform(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(255),unique=True,nullable=False)
