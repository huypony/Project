from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config  
from .modules.TaiKhoan.models import db  
from .modules.TaiKhoan.routes import tai_khoan_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Khởi tạo SQLAlchemy
    jwt = JWTManager(app)

    app.register_blueprint(tai_khoan_bp, url_prefix="/api/tai-khoan")

    with app.app_context():
        db.create_all()  # Tạo bảng nếu chưa có

    return app
