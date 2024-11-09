# Archivo: backup_manager/config.py
# Ruta: /config.py
# Descripción: Configuración de la aplicación

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Configuración básica
    SECRET_KEY = os.getenv("SECRET_KEY") or "dev-key-very-secret"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de DigitalOcean Spaces
    SPACES_KEY = os.getenv("SPACES_KEY")
    SPACES_SECRET = os.getenv("SPACES_SECRET")
    SPACES_BUCKET = os.getenv("SPACES_BUCKET")
    SPACES_REGION = os.getenv("SPACES_REGION")

    # Configuración de Stripe
    STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY")
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

    # Planes de precio (los IDs los obtendremos de Stripe más adelante)
    STRIPE_PRICE_BASIC = os.getenv("STRIPE_PRICE_BASIC")
    STRIPE_PRICE_PRO = os.getenv("STRIPE_PRICE_PRO")
