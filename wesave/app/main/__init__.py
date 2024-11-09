# Archivo: backup_manager/app/main/__init__.py
# Ruta: /app/main/__init__.py
# Descripción: Blueprint principal

from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main import routes
