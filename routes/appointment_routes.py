from flask import Blueprint, request, g
from database import get_db
from auth_middleware import auth_middleware, admin_middleware
import sqlite3
appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointment')

connection=sqlite3.connect()
cursor=connection.cursor

@appointment_bp.route("/create", methods=["POST"])
@auth_middleware
def create_appointment():
    username = g.username
    id=g.id
    status=g.status
    appointment_data=g.appointment_data
    service=g.service
    notes=g.notes
    created_at=g.created_at
    json_data = request.get_json()
    sql_command = '''
    INSERT INTO appointments (id, username, appointment_date, service,notes,status,created_at)
    '''
    # TODO: Implement create appointment logic
    cursor.excecute(sql_command)
    pass


@appointment_bp.route("/read", methods=["GET"])
@auth_middleware
def read_appointments():
    # TODO: Implement read appointments logic
    db = get_db()
    username = g.username

    rows = db.execute(
        """
        SELECT id, username, appointment_date, service, notes, status, created_at
        FROM appointments
        WHERE username = ?
        ORDER BY appointment_date DESC
        """,
        (username,),
    ).fetchall()
    pass


@appointment_bp.route("/delete/<int:appointment_id>", methods=["DELETE"])
@auth_middleware
def delete_appointment(appointment_id):
    # TODO: Implement delete appointment logic
    db = get_db()
    username = g.username

    cur = db.execute(
        "DELETE FROM appointments WHERE id = ? AND username = ?",
        (appointment_id, username),
    )
    db.commit()
    pass


@appointment_bp.route("/admin/read", methods=["GET"])
@auth_middleware
@admin_middleware
def admin_read_appointments():
    
    # TODO: Implement admin read appointments logic
    db = get_db()

    rows = db.execute(
        """
        SELECT id, username, appointment_date, service, notes, status, created_at
        FROM appointments
        ORDER BY created_at DESC
        """
    ).fetchall()
    pass


@appointment_bp.route("/admin/edit/<int:appointment_id>", methods=["PUT"])
@auth_middleware
@admin_middleware
def admin_edit_appointment(appointment_id):
    json_data = request.get_json()
    
    # TODO: Implement admin edit appointment logic
    db = get_db()
    data = request.get_json() or {}
    appointment_date = data.get("appointment_date")
    service = data.get("service")
    notes = data.get("notes")
    status = data.get("status")

    cur = db.execute(
        """
        UPDATE appointments
        SET
            appointment_date = COALESCE(?, appointment_date),
            service = COALESCE(?, service),
            notes = COALESCE(?, notes),
            status = COALESCE(?, status)
        WHERE id = ?
        """,
        (appointment_date, service, notes, status, appointment_id),
    )
    db.commit()
    pass


@appointment_bp.route("/admin/delete/<int:appointment_id>", methods=["DELETE"])
@auth_middleware
@admin_middleware
def admin_delete_appointment(appointment_id):
    
    # TODO: Implement admin delete appointment logic
    db = get_db()

    cur = db.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
    db.commit()
    pass
