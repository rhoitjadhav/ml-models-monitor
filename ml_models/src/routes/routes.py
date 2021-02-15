# Packages
from flask.json import jsonify
from flask import Blueprint, request

# Modules
from src.usecases.usecases import Usecases
from src.models.local_database import LocalDatabase


usecase = Usecases(LocalDatabase())

bp = Blueprint('', __name__, url_prefix='/')


# Models Details
@bp.route('/models', methods=['GET'])
def models():
    models = usecase.get_all_models()
    return jsonify(models)


# Performance Metrics
@bp.route('/performance-metrics', methods=['GET'])
def performance_metrics():
    model_id = request.args.get('modelId', False)
    if model_id:
        performance_metrics = usecase.get_performance_metrics(model_id)
        return jsonify(performance_metrics)
    
    else:
        return jsonify({
            'success': False,
            'message': 'modelId not in request parameters'
        }), 400


