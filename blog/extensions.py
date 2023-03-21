from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_admin import Admin
from blog.admin.views import CustomAdminIndexView
from flask_combo_jsonapi import Api


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
admin = Admin(index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4',)
api = Api()
