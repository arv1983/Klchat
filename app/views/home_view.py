from flask import Blueprint, redirect


bp = Blueprint("bp_home", __name__)


@bp.get("/")
def home_page():
    return redirect("https://andersonvaler.github.io/documentation-capstone/")
