# Archivo: backup_manager/app/__init__.py
# Ruta: /app/__init__.py
# Descripción: Inicialización de la aplicación Flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from wesave.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Registrar blueprints
    from app.auth import bp as auth_bp

    app.register_blueprint(auth_bp)

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app


from app import models  # Importar los modelos
