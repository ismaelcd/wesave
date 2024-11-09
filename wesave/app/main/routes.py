# Archivo: backup_manager/app/main/routes.py
# Ruta: /app/main/routes.py
# Descripción: Rutas principales

from flask import render_template
from app.main import bp


@bp.route("/")
def index():
    return render_template("main/index.html")
