from unittest import TestCase
from adapters.validators.request_validator import RequestValidator


class RequestValidatorTest(TestCase):
    _valid_request = {
        "function": "fibonacci",
        "data": {
            "n": 1
        }
    }

    _invalid_request_missing_function = {
        "data": {
            "n": 1
        }
    }

    _invalid_request_missing_data = {
        "function": "fibonacci"
    }

    _invalid_request_f_type = {
        "function": 1,
        "data": {
            "n": 1
        }
    }

    _invalid_request_d_type = {
        "function": "fibonacci",
        "data": 1
    }

    _invalid_request_type = [1]

    def test_valid_request(self):
        assert RequestValidator.valid(
            self._valid_request
        )

    def test_invalid_request_type(self):
        assert not RequestValidator.valid(
            self._invalid_request_type
        )

    def test_invalid_request_d_type(self):
        assert not RequestValidator.valid(
            self._invalid_request_d_type
        )

    def test_invalid_request_f_type(self):
        assert not RequestValidator.valid(
            self._invalid_request_f_type
        )

    def test_invalid_request_no_f(self):
        assert not RequestValidator.valid(
            self._invalid_request_missing_function
        )

    def test_invalid_request_no_d(self):
        assert not RequestValidator.valid(
            self._invalid_request_missing_data
        )
