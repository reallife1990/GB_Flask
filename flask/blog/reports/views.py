from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
reports_app = Blueprint("reports_app", __name__, url_prefix="reports", static_folder="../static")
#(  имя приложения, имя файла текущего)
REPORTS = {1: {"name":"Jas", "text":"text by Jas"},
    2: {"name":"Brian", "text":"text by Brian"},
    3: {"name":"Peter", "text":"text by Peter"},
    }


@reports_app.route("/")
def reports_list():
    return render_template("reports/list.html", reports=REPORTS )

@reports_app.route("/<int:report_id>/", endpoint="details")
def user_details(report_id: int):
    try:
        report_txt = REPORTS[report_id].get("text")
        author = REPORTS[report_id].get("name")
    except KeyError:
        raise NotFound(f"Report #{report_id} doesn't exist!")
    return render_template('reports/details.html',author=author, report_id=report_id,report_txt=report_txt)