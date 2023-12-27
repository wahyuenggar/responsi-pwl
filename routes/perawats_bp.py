from flask import Blueprint
from controllers.TasksController import index, store, show, update, delete

perawats_bp = Blueprint('perawats_bp', __name__)

perawats_bp.route('/', methods=['GET'])(index)
perawats_bp.route('/', methods=['POST'])(store)
perawats_bp.route('/<int:npm_perawat>', methods=['GET'])(show)
perawats_bp.route('/<int:npm_perawat>', methods=['PUT'])(update)
perawats_bp.route('/<int:npm_perawat>', methods=['DELETE'])(delete)