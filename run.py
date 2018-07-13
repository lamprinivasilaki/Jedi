from poc import create_application


def main():
    app = create_application()
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == "__main__":
    main()


# flask_app = Flask(__name__)
#
# jedi = Blueprint('jedi', __name__)


# , request
# from flask.json import jsonify
# from controllers import  jedis

# jedi = [
#     {"name": "Qui-Gon Jinn", "id": 1},
#     {"name": "Obi-Wan Kenobi", "id": 2},
#     {"name": "Anakin Skywalker", "id": 3},
#     {"name": "Mace Windu", "id": 4}
# ]
#
# sith_lords = [
#     {"id": 1, "name": "Darth Vader", "movie": "A New Hope"},
#     {"id": 2, "name": "Darth Bane", "movie": "The Clone Wars"},
#     {"id": 3, "name": "Darth Sidious", "movie": "A New Hope"},
# ]


# @flask_app.route('/')
# def get_home():
#     return 'Welcome'
#
#
# @flask_app.route('/jedi')
# def get_all_jedi():
#     return jsonify({'jedi': jedi})
#
#
# @flask_app.route('/jedi/<jedi_id>')
# def get_jedi(jedi_id):
#
#     for j in jedi:
#         if j["id"] == int(jedi_id):
#             return jsonify({'jedi': j})
#
#     return jsonify({'jedi': jedi})
#
#
# @flask_app.route('/siths')
# def get_sith():
#     sith_id = request.args.get("id")
#     movie = request.args.get("movie")
#
#     for sith in sith_lords:
#         if sith["id"] == int(sith_id) and sith["movie"] == movie:
#             return jsonify({'sith': sith})
#
#     return jsonify({'siths': sith_lords})
#
#
# @flask_app.route('/jedi', methods=["POST"])
# def post_jedi():
#     print(request)
#
#     jedi_name = request.get_json()["name"]
#
#     count = len(jedi) + 1
#
#     jedi.append({"name": jedi_name, "id": count})
#
#     print(count)
#
#     return jsonify({'jedi': jedi})