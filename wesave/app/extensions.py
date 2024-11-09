# Archivo: backup_manager/app/extensions.py
# Ruta: /app/extensions.py
# Descripción: Configuración de extensiones Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Inicializar extensiones
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
