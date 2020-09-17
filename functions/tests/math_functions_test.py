from unittest import TestCase, mock
from functions.math_functions import math


class MathFunctionsTest(TestCase):
    def test_fib_happy_path(self):
        request = mock.MagicMock()
        payload = {
            'function': 'fibonacci',
            'data': {
                'n': 4
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 200

    def test_fib_naive_happy_path(self):
        request = mock.MagicMock()
        payload = {
            'function': 'fibonacci_naive',
            'data': {
                'n': 4
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 200

    def test_fact_happy_path(self):
        request = mock.MagicMock()
        payload = {
            'function': 'factorial',
            'data': {
                'n': 4
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 200

    def test_ack_happy_path(self):
        request = mock.MagicMock()
        payload = {
            'function': 'ackermann',
            'data': {
                'm': 2,
                'n': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 200

    def test_ack_naive_happy_path(self):
        request = mock.MagicMock()
        payload = {
            'function': 'ackermann_naive',
            'data': {
                'm': 2,
                'n': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 200

    def test_ack_bad_param(self):
        request = mock.MagicMock()
        payload = {
            'function': 'ackermann',
            'data': {
                'n': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 400

    def test_ack_naive_bad_param(self):
        request = mock.MagicMock()
        payload = {
            'function': 'ackermann_naive',
            'data': {
                'n': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 400

    def test_fib_naive_bad_param(self):
        request = mock.MagicMock()
        payload = {
            'function': 'fibonacci_naive',
            'data': {
                'm': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 400

    def test_fib_bad_param(self):
        request = mock.MagicMock()
        payload = {
            'function': 'fibonacci',
            'data': {
                'm': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 400

    def test_fact_bad_param(self):
        request = mock.MagicMock()
        payload = {
            'function': 'factorial',
            'data': {
                'm': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 400

    def test_invalid_function(self):
        request = mock.MagicMock()
        payload = {
            'function': 'zeta',
            'data': {
                'm': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 400

    def test_invalid_payload(self):
        request = mock.MagicMock()
        payload = {
            'data': {
                'm': 1
            }
        }
        request.json = payload
        request.method = 'POST'
        response = math(request)
        assert response[1] == 400
