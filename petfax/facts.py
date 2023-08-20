from flask import (Blueprint, render_template)

bp = Blueprint('fact', __name__, url_prefix="/facts/new")

@bp.route('/', methods=["GET", "POST"])
def index():
    return render_template("facts.html")