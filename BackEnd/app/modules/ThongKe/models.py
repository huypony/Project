from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HoaDon(db.Model):
    __tablename__ = 'HoaDon'

    HoaDonID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, unique=True, nullable=False)
    SoHoaDon = db.Column(db.String(50))
    NgayXuatHoaDon = db.Column(db.Date)
    TongTienTruocGiam = db.Column(db.Numeric)
    TongTienSauGiam = db.Column(db.Numeric)
    KhuyenMaiID = db.Column(db.Integer, unique=True)
    TrangThai = db.Column(db.String)