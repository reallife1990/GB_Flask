from flask import Blueprint, render_template
from flask_login import login_required

from werkzeug.exceptions import NotFound

from blog.auth.views import login_manager
from blog.models.user import User

users_app = Blueprint("users_app", __name__, url_prefix="users", static_folder="../static")
#(  имя приложения, имя файла текущего)
# USERS = {1: "James",
#     2: "Brian",
#     3: "Peter",
#     }


@users_app.route("/")
def users_list():
    users = User.query.all()
    return render_template("users/list.html", users=users)

@users_app.route("/<int:user_id>/", endpoint="details")
@login_required
def user_details(user_id: int):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template("users/details.html", user=user)
    # try:
    #     user_name = USERS[user_id]
    # except KeyError:
    #     raise NotFound(f"Пользователя с id {user_id} не найдено. проверьте введённые данные")
    # return render_template('users/details.html', user_id=user_id,user_name=user_name)