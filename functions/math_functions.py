from adapters.validators.request_validator import RequestValidator
from adapters.validators.param_validator import SingleParamValidator
from adapters.validators.param_validator import DualParamValidator
from adapters.validators.function_type_validator import FunctionTypeValidator
from core.fibonacci import fibonacci, fibonacci_naive
from core.factorial import factorial


def math(request):
    # response headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true',
        'Content-Type': 'application/json'
    }

    # grabs request payload
    payload = request.json

    # request payload validation
    if not RequestValidator.valid(payload):
        return {'error': 'invalid request payload'}, 400, headers
    f_type = payload['function']
    if not FunctionTypeValidator.valid(f_type):
        return {'error': 'invalid function type'}, 400, headers

    # data and function params validations and calculation
    params = payload['data']
    result = 0
    if f_type == 'fibonacci':
        if not SingleParamValidator(params):
            return {'error': 'invalid function params'}, 400, headers
        result = fibonacci(params['n'])
    elif f_type == 'fibonacci_naive':
        if not SingleParamValidator(params):
            return {'error': 'invalid function params'}, 400, headers
        result = fibonacci_naive(params['n'])
    elif f_type == 'factorial':
        if not SingleParamValidator(params):
            return {'error': 'invalid function params'}, 400, headers
        result = factorial(params['n'])
    elif f_type == 'ackermann':
        if not DualParamValidator(params):
            return {'error': 'invalid function params'}, 400, headers
        result = fibonacci(params['n'])
    else:
        if not DualParamValidator(params):
            return {'error': 'invalid function params'}, 400, headers
        result = fibonacci(params['n'])

    return {'result': result}, 200, headers
