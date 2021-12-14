from flask import request, jsonify


def upload():
    data = request.get_json(silent=True)
    try:
        print("noitce:", data)
        return jsonify({'code': 200, 'msg': 'success'})
    except:
        return jsonify({'code': 400, 'msg': 'error'})
