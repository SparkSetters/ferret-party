from flask import (
    Blueprint, Flask
)

app = Flask(__name__)

bp = Blueprint('test_route', __name__, url_prefix='/test')


@bp.route("/hello")
def hello_world():
    return "<p>routedHello</p>"
