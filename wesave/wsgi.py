# Archivo: backup_manager/wsgi.py
# Ruta: /wsgi.py
# Descripción: Punto de entrada para la aplicación

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
