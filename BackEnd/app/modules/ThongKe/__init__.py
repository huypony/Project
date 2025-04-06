from flask import Blueprint

thongke_bp = Blueprint('thongke', __name__)

from . import routes