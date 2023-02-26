from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_app = Blueprint("users_app", __name__, url_prefix="users", static_folder="../static")
#(  имя приложения, имя файла текущего)
USERS = {1: "James",
    2: "Brian",
    3: "Peter",
    }


@users_app.route("/")
def users_list():
    return render_template("users/list.html", users=USERS )

@users_app.route("/<int:user_id>/", endpoint="details")
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f"Пользователя с id {user_id} не найдено. проверьте введённые данные")
    return render_template('users/details.html', user_id=user_id,user_name=user_name)