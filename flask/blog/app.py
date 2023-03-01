from blog.users.views import users_app
from blog.reports.views import reports_app
from flask import Flask, request, render_template
from blog.models.database import db
from blog.auth.views import login_manager, auth_app
import os
from blog.models import User

app = Flask(__name__)
app.config["SECRET_KEY"] = 'fdgfh78@#5?>gfhf89dx,v06k'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config.update(dict(DATABASE=os.path.join(app.root_path,'blog.db')))
db.init_app(app)



@app.route("/")
def index():
    return render_template("base.html")


@app.route("/<name>/")
def greet_name(name: str):
    return f"Hello {name}!"


@app.route("/sum/")
def read_user():
    first = request.args.get("first")
    second = request.args.get("second")
    try:
        result = int(first) + int(second)
        return f"Summ {first or '[no name]'} and  {second or '[no surname]'} = {result}"
    except:
        # if type(first) is int and type()
        return f"Concatenate {first or '[no name]'} and  {second or '[no surname]'} is {first + second}"


@app.route("/divide-by-zero/")
def do_zero_division():
    return 1 / 0


@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(error):
    print(error)  # prints str version of error: 'division by zero'
    app.logger.exception("Here's traceback for zero division error")
    return "Never divide by zero!", 400


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(reports_app, url_prefix="/reports")
app.register_blueprint(auth_app, url_prefix="/auth")
login_manager.init_app(app)
