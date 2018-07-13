from flask import Flask
from controllers.jedis import jediB
from controllers.siths import sithB


def create_application():
    flask_app = Flask(__name__)

    flask_app.register_blueprint(jediB, url_prefix="/jedi")
    flask_app.register_blueprint(sithB, url_prefix="/sith")

    return flask_app





# jedi_blueprint = Blueprint('jedis', __name__)
# jedis.init_app(jedi_blueprint)

# flask_app.register_blueprint(jedi_blueprint)


# flask_app = Flask(__name__)
# flask_app.config.update(config or {})
# flask_app.config['ENVIRONMENT'] = environment
#
# rest_api_blueprint = Blueprint('api', __name__, url_prefix='/api')
#
# flask_app.register_blueprint(rest_api_blueprint)

# @flask_app.route('/')
# def get_home():
#     return 'Welcome'
#
# @flask_app.route('/jedi')
# def get_all_jedi():
#     jedi = [
#         {"name": "Qui-Gon Jinn", "id": 1},
#         {"name": "Obi-Wan Kenobi", "id": 2},
#         {"name": "Anakin Skywalker", "id": 3},
#         {"name": "Mace Windu", "id": 4}
#     ]
#     return jsonify({'jedi': jedi})
#
# @flask_app.route('/jedi/<jedi_id>')
# def get_jedi(jedi_id):
#     jedi = [
#         {"name": "Qui-Gon Jinn", "id": 1},
#         {"name": "Obi-Wan Kenobi", "id": 2},
#         {"name": "Anakin Skywalker", "id": 3},
#         {"name": "Mace Windu", "id": 4}
#     ]
#
#     for j in jedi:
#         if j["id"] == int(jedi_id):
#             return jsonify({'jedi': j})
#
#     return jsonify({'jedi': jedi})
#
# @flask_app.route('/jedi', methods=["POST"])
# def post_jedi():
#
#     print(request)
#
#     # jedi_name = request.name
#
#     jedi = [
#         {"name": "Qui-Gon Jinn", "id": 1},
#         {"name": "Obi-Wan Kenobi", "id": 2},
#         {"name": "Anakin Skywalker", "id": 3},
#         {"name": "Mace Windu", "id": 4}
#     ]
#
#     count = len(jedi) + 1
#
#     # jedi.append({"name": jedi_name, "id": count})
#
#     print(count)
#
#     return jsonify({'jedi': jedi})
#
