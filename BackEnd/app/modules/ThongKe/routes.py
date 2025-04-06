from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .controllers import thong_ke_doanh_thu

thongke_bp = Blueprint("thongke", __name__)

@thongke_bp.route("/doanh-thu", methods=["GET"])
@jwt_required()
def get_doanh_thu():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"message": "Bạn không có quyền thực hiện thao tác này"}), 403
    return thong_ke_doanh_thu()

@thongke_bp.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "Mô-đun ThongKe hoạt động bình thường"})