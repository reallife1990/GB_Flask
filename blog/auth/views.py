from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash
from blog.forms.user import UserLoginForm
from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')


# @auth.route('/login', methods=('GET',))
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('user.profile', pk=current_user.id))
#
#     return render_template(
#         'auth/login.html',
#     )
#
#
# @auth.route('/login', methods=('POST',))
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')
#
#     user = User.query.filter_by(email=email).first()
#
#     if not user or not check_password_hash(user.password, password):
#         flash('Check your login details')
#         return redirect(url_for('.login'))
#
#     login_user(user)
#     return redirect(url_for('user.profile', pk=user.id))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserLoginForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not check_password_hash(user.password, form.password.data):
            flash('Check your login details')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(url_for('user.profile', pk=user.id))

        # if User.query.filter_by(email=form.email.data).count():
        #     form.email.errors.append('email already exists')
        #     return render_template('users/register.html', form=form)

        # _user = User(
        #     email=form.email.data,
        #     first_name=form.first_name.data,
        #     last_name=form.last_name.data,
        #     password=generate_password_hash(form.password.data),
        # )

        # db.session.add(_user)
        # db.session.commit()
        #
        # login_user(_user)

    return render_template(
        'auth/login.html',
        form=form,
        errors=errors,
    )



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
