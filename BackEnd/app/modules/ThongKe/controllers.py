from flask import request, jsonify
from sqlalchemy import extract, func
from .models import db, HoaDon

def thong_ke_doanh_thu():
    # Lấy tham số từ query string (nếu có)
    start_date = request.args.get('start_date')  # Ví dụ: 2025-01-01
    end_date = request.args.get('end_date')      # Ví dụ: 2025-12-31
    group_by_month = request.args.get('group_by_month', 'false').lower() == 'true'

    # Truy vấn cơ bản
    query = db.session.query(func.sum(HoaDon.TongTienSauGiam).label('TongDoanhThu'))\
                     .filter(HoaDon.TrangThai == 'DaXuat')

    # Nếu có khoảng thời gian
    if start_date and end_date:
        query = query.filter(HoaDon.NgayXuatHoaDon.between(start_date, end_date))

    # Nếu muốn nhóm theo tháng
    if group_by_month:
        query = db.session.query(
            extract('year', HoaDon.NgayXuatHoaDon).label('Nam'),
            extract('month', HoaDon.NgayXuatHoaDon).label('Thang'),
            func.sum(HoaDon.TongTienSauGiam).label('DoanhThu')
        ).filter(HoaDon.TrangThai == 'DaXuat')\
         .group_by(extract('year', HoaDon.NgayXuatHoaDon), extract('month', HoaDon.NgayXuatHoaDon))\
         .order_by('Nam', 'Thang')

        # Trả về danh sách doanh thu theo tháng
        result = query.all()
        doanh_thu_list = [
            {"Nam": int(nam), "Thang": int(thang), "DoanhThu": float(doanh_thu)}
            for nam, thang, doanh_thu in result
        ]
        return jsonify({"doanh_thu_theo_thang": doanh_thu_list}), 200

    # Nếu không nhóm theo tháng, trả về tổng doanh thu
    result = query.scalar()
    if result is None:
        result = 0  # Nếu không có dữ liệu, trả về 0
    return jsonify({"TongDoanhThu": float(result)}), 200