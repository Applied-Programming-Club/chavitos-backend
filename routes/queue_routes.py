from flask import Blueprint, request, g
from database import get_db
from auth_middleware import auth_middleware, admin_middleware

queue_bp = Blueprint('queue', __name__, url_prefix='/queue')

@queue_bp.route("/add", methods=["POST"])
@auth_middleware
def add_to_queue():
    username = g.username
    json_data = request.get_json() or {}
    
    # TODO: Implement add to queue logic
    
    pass


@queue_bp.route("/leave", methods=["POST"])
@auth_middleware
def leave_queue():
    username = g.username
    
    # TODO: Implement leave queue logic
    
    pass


@queue_bp.route("/status", methods=["GET"])
@auth_middleware
def get_queue_status():
    jwt = request.headers.get("Authorization", None)
    
    # TODO: Implement get queue status logic
    
    pass


@queue_bp.route("/admin/remove", methods=["POST"])
@auth_middleware
@admin_middleware
def admin_remove_from_queue():
    json_data = request.get_json()
    
    # TODO: Implement admin remove from queue logic
    
    pass


@queue_bp.route("/admin/add", methods=["POST"])
@auth_middleware
@admin_middleware
def admin_add_to_queue():
    json_data = request.get_json()
    
    # TODO: Implement admin add to queue logic
    
    pass


@queue_bp.route("/admin/list", methods=["GET"])
@auth_middleware
@admin_middleware
def admin_list_queue():
    
    # TODO: Implement admin list queue logic
    
    pass
