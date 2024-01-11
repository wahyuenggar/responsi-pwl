from flask import Blueprint
from controllers.DokterController import index, store, show, update, delete

dokters_bp = Blueprint('dokters_bp', __name__)

dokters_bp.route('/', methods=['GET'])(index)
dokters_bp.route('/', methods=['POST'])(store)
dokters_bp.route('/<int:npm_dokter>', methods=['GET'])(show)
dokters_bp.route('/<int:npm_dokter>', methods=['PUT'])(update)
dokters_bp.route('/<int:npm_dokter>', methods=['DELETE'])(delete)