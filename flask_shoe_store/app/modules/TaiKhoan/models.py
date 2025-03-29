from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class TaiKhoan(db.Model):
    __tablename__ = 'TaiKhoan'

    TaiKhoanID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, unique=True, nullable=False)
    TenDangNhap = db.Column(db.String(255), unique=True, nullable=False)
    MatKhau = db.Column(db.String(255), nullable=False)
    NgayTao = db.Column(db.DateTime, default=datetime.utcnow)
    Role = db.Column(db.String(50), default="user")
    TrangThai = db.Column(db.Boolean, default=True)  # True: active, False: blocked
