# Archivo: backup_manager/app/models.py
# Ruta: /app/models.py
# Descripción: Modelos de la base de datos

from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    name = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    subscription_type = db.Column(db.String(20), default="free")  # free, basic, pro

    # Relaciones
    databases = db.relationship("ClientDatabase", backref="owner", lazy=True)
    backups = db.relationship("Backup", backref="owner", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class ClientDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # mysql, mongodb, postgres
    host = db.Column(db.String(200), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    database_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)  # Debería estar encriptado
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_backup = db.Column(db.DateTime)

    # Relaciones
    backups = db.relationship("Backup", backref="database", lazy=True)


class Backup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    database_id = db.Column(
        db.Integer, db.ForeignKey("client_database.id"), nullable=False
    )
    filename = db.Column(db.String(200), nullable=False)
    size = db.Column(db.Integer)  # tamaño en bytes
    status = db.Column(
        db.String(20), default="pending"
    )  # pending, running, completed, failed
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    space_path = db.Column(db.String(500))  # ruta en DigitalOcean Spaces
    error_message = db.Column(db.Text)


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    stripe_customer_id = db.Column(db.String(100), unique=True)
    stripe_subscription_id = db.Column(db.String(100), unique=True)
    plan_type = db.Column(db.String(20), nullable=False)  # basic, pro
    status = db.Column(db.String(20), default="active")  # active, cancelled, past_due
    current_period_end = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
