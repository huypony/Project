from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, TaiKhoan
from flask_jwt_extended import create_access_token

def dang_ky():
    data = request.get_json()
    if TaiKhoan.query.filter_by(TenDangNhap=data["TenDangNhap"]).first():
        return jsonify({"message": "Tên đăng nhập đã tồn tại"}), 400
    
    
    hashed_password= generate_password_hash(data["MatKhau"], method='pbkdf2:sha256')
    #tao khach hang 
    new_user = TaiKhoan(
        CustomerID=data["CustomerID"],
        TenDangNhap=data["TenDangNhap"],
        MatKhau=hashed_password,
        Role="user"
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "Đăng ký thành công"}), 201

def dang_nhap():
    data = request.get_json()
    user = TaiKhoan.query.filter_by(TenDangNhap=data["TenDangNhap"]).first()
    
    if not user or not check_password_hash(user.MatKhau, data["MatKhau"]):
        return jsonify({"message": "Tên đăng nhập hoặc mật khẩu không đúng"}), 401

    if not user.TrangThai:
        return jsonify({"message": "Tài khoản của bạn đã bị khóa"}), 403
    
    access_token = create_access_token(identity={"id": user.TaiKhoanID, "role": user.Role})
    return jsonify({"access_token": access_token}), 200

def khoa_tai_khoan(user_id):
    user = TaiKhoan.query.get(user_id)
    if not user:
        return jsonify({"message": "Không tìm thấy tài khoản"}), 404
    
    user.TrangThai = False
    db.session.commit()
    return jsonify({"message": "Tài khoản đã bị khóa"}), 200
