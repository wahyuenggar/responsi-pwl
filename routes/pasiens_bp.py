from flask import Blueprint
from controllers.PasienController import index, store, show, update, delete

pasiens_bp = Blueprint('pasiens_bp', __name__)

pasiens_bp.route('/', methods=['GET'])(index)
pasiens_bp.route('/', methods=['POST'])(store)
pasiens_bp.route('/<int:id_pasien>', methods=['GET'])(show)
pasiens_bp.route('/<int:id_pasien>', methods=['PUT'])(update)
pasiens_bp.route('/<int:id_pasien>', methods=['DELETE'])(delete)