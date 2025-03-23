from flask import Blueprint, request, render_template, session, redirect, url_for, flash
from bson import ObjectId
from bson.errors import InvalidId
from src.models.event import Event
from src.models.user import User
from datetime import datetime
dashboard_bp = Blueprint('dashboard', __name__)


def get_current_user_id():
    try:
        user_id = ObjectId(session.get('user_id'))
        return user_id
    except (InvalidId, TypeError):
        session.clear()
        return None


def list_events(user_id):
    return list(Event.find_by_user_id(user_id))

def change_date_format(str_date):
    try:
        date_solo = datetime.strptime(str_date, "%Y-%m-%d").date()
    except ValueError:
        return None
    return datetime.combine(date_solo, datetime.min.time())



@dashboard_bp.route('/dash')
def user_dash():
    user_id = get_current_user_id()
    if user_id is None:
        return redirect(url_for('auth.login'))

    user = User.find_by_id(user_id)
    if user:
        events = list_events(user_id)
        return render_template("dashboard.html", email=user['email'], events=events)

    return redirect(url_for('auth.login'))


@dashboard_bp.route("/dash/addEvent", methods=['POST'])
def add_event():
    user_id = get_current_user_id()
    if user_id is None:
        return redirect(url_for('auth.login'))

    title = request.form.get('title')
    detail = request.form.get('detail')
    date = change_date_format(request.form.get('date'))
    if date is None:
        return redirect(url_for('dashboard.user_dash'))

    Event.create(user_id, title, detail, date)
    return redirect(url_for('dashboard.user_dash'))


@dashboard_bp.route("/dash/deleteEvent/<event_id>", methods=['POST'])
def delete_event(event_id):
    user_id = get_current_user_id()
    if user_id is None:
        return redirect(url_for('auth.login'))

    try:
        event_oid = ObjectId(event_id)
    except InvalidId:
        flash("Invalid event ID.", "error")
        return redirect(url_for('dashboard.user_dash'))

    Event.delete_by_user_id_and_id(user_id, event_oid)
    return redirect(url_for('dashboard.user_dash'))


@dashboard_bp.route("/dash/completeEvent/<event_id>", methods=['POST'])
def complete_event(event_id):
    user_id = get_current_user_id()
    if user_id is None:
        return redirect(url_for('auth.login'))

    try:
        event_oid = ObjectId(event_id)
    except InvalidId:
        flash("Invalid event ID.", "error")
        return redirect(url_for('dashboard.user_dash'))

    Event.complete_event(user_id, event_oid)
    return redirect(url_for('dashboard.user_dash'))


@dashboard_bp.route("/dash/logout", methods=['POST'])
def log_out():
    session.clear()
    return redirect(url_for('dashboard.user_dash'))

@dashboard_bp.route("/dash/deleteUser", methods=['POST'])
def delete_user():
    user_id = get_current_user_id()
    if user_id is None:
        return redirect(url_for('auth.login'))
    User.delete_by_id(user_id)
    return redirect(url_for('dashboard.user_dash'))