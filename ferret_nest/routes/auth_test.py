from flask import (
    Blueprint, Flask, request, jsonify
)
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from decouple import config

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = config('SUPABASE_JWT_SECRET')


jwt = JWTManager(app)


auth_test = Blueprint('auth_test', __name__)


@auth_test.route('/auth-test', methods=['GET'])
@jwt_required()
def protected_resource():

    user_identity = get_jwt_identity()

    print(user_identity)

    return jsonify(message="This is a protected resource!", user=user_identity), 200


if __name__ == '__main__':
    app.run(debug=True)
