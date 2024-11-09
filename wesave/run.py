# Archivo: backup_manager/run.py
# Ruta: /run.py
# Descripción: Punto de entrada principal de la aplicación

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
