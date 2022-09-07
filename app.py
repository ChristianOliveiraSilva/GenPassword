from flask import Flask, render_template
from config import app_config, app_active

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html'), 404

    return app
