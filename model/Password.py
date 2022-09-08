from flask_sqlalchemy import SQLAlchemy

# config
from config import app_config, app_active
config = app_config[app_active]

from model.Platform import Platform
db = SQLAlchemy(config.APP)

class Password(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  password = db.Column(db.String(255),nullable=False)
  plataform = db.Column(db.Integer,db.ForeignKey(Platform.id),nullable=False)