from unittest import TestCase
from adapters.validators.function_type_validator import FunctionTypeValidator


class FunctionTypeValidatorTest(TestCase):
    def test_found_f(self):
        assert FunctionTypeValidator.valid('fibonacci')

    def test_not_found_f(self):
        assert not FunctionTypeValidator.valid('zeta')
