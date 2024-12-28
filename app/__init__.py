from flask import Flask 
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect 

from config import config

mysql = MySQL

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    mysql.init_app(app)
    CSRFProtect(app)

    # blueprints 

    return app
