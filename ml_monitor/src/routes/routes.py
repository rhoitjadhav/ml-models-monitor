# Packages
import requests
from flask.json import jsonify
from flask import current_app, request, Blueprint

bp = Blueprint('', __name__, url_prefix='/')


# Models Details
@bp.route('/models', methods=['GET'])
def models():
    url = f'http://{current_app.config["ML_MODELS_SERVER_NAME"]}/models'
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())

    else:
        return jsonify({
            'success': False,
            'message': 'Error while getting models details'
        })


# Performance Metrics
@bp.route('/performance-metrics', methods=['GET'])
def performance_metrics():
    url = f'http://{current_app.config["ML_MODELS_SERVER_NAME"]}/performance-metrics'
    model_id = request.args.get('modelId', False)

    if model_id:
        response = requests.get(url,  params={'modelId': model_id})

        if response.status_code == 200:
            return jsonify(response.json())

        else:
            return jsonify({
                'success': False,
                'message': 'Error while getting performance metrics'
            })

    else:
        return jsonify({
            'success': False,
            'message': 'modelId not in request parameters'
        }), 400
