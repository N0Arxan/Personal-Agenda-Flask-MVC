import re
from flask import Blueprint, request, render_template, session, redirect, url_for
from src.models.user import User
from werkzeug.security import  check_password_hash

auth_bp = Blueprint('auth', __name__)

def validate_email_password(email,password):
    e_is_valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    p_is_vaild = re.match(r'.{4,}', password)
    if e_is_valid and p_is_vaild:
        return True
    return False

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not validate_email_password(email, password):
            return render_template('login.html',incorrect=True)


        user = User.find_by_email(email)
        if not user:
            User.create(email, password)  # In real app, implement proper registration
            print("not exist user created")
            return "user created successfully go back to  <a href='/'>login</a>"

        if check_password_hash(user['password'],request.form['password']):
            session['user_id'] = str(user['_id'])
            return redirect(url_for('dashboard.user_dash'))

        return render_template('login.html',incorrect=True)

    return render_template('login.html',incorrect=False)


