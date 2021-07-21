from app.models.categorias_model import Categorias
from app.models.status_model import Status

from flask import Blueprint, jsonify

bp = Blueprint("bp_categorias", __name__)


@bp.get("/categorias")
def ver_categorias():
    categorias = Categorias.query.all()
    return jsonify(categorias)

@bp.get("/status")
def ver_status():
    status = Status.query.all()
    return jsonify(status)
