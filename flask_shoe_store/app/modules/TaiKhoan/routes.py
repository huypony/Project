from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .controllers import dang_ky, dang_nhap, khoa_tai_khoan

tai_khoan_bp = Blueprint("tai_khoan", __name__) #Tạo blueprint

@tai_khoan_bp.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "Test route hoạt động"})

@tai_khoan_bp.route("/", methods=["GET"])  
def get_all_accounts():
    return jsonify({"message": "API hoạt động bình thường"})


@tai_khoan_bp.route("/dang-ky", methods=["POST"])
def register():
    return dang_ky()

@tai_khoan_bp.route("/dang-nhap", methods=["POST"])
def login():
    return dang_nhap()

@tai_khoan_bp.route("/khoa-tai-khoan/<int:user_id>", methods=["PUT"])
@jwt_required()
def lock_user(user_id):
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return {"message": "Bạn không có quyền thực hiện thao tác này"}, 403
    return khoa_tai_khoan(user_id)
