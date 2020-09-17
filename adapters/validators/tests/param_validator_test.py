from unittest import TestCase
from adapters.validators.param_validator import SingleParamValidator
from adapters.validators.param_validator import DualParamValidator


class ParamValidatorTest(TestCase):
    _valid_param = {
        "m": 1,
        "n": 1
    }

    _invalid_struct_param_xy = {
        "x": 1,
        "y": 2
    }

    _invalid_struct_param_ny = {
        "n": 1,
        "y": 2
    }

    _invalid_param_type_param = {
        "m": "1",
        "n": "1"
    }

    _invalid_param_m_type_param = {
        "m": "1",
        "n": 1
    }

    _invalid_struct_type = [1]

    def test_valid_sp(self):
        assert SingleParamValidator.valid(
            self._valid_param
        )

    def test_invalid_struct_sp(self):
        assert not SingleParamValidator.valid(
            self._invalid_struct_param_xy
        )

    def test_invalid_param_type_sp(self):
        assert not SingleParamValidator.valid(
            self._invalid_param_type_param
        )

    def test_invalid_sp_type(self):
        assert not SingleParamValidator.valid(
            self._invalid_struct_type
        )

    def test_valid_dp(self):
        assert DualParamValidator.valid(
            self._valid_param
        )

    def test_invalid_struct_dp(self):
        assert not DualParamValidator.valid(
            self._invalid_struct_param_xy
        )

    def test_invalid_param_type_dp(self):
        assert not DualParamValidator.valid(
            self._invalid_param_type_param
        )

    def test_invalid_dp_type(self):
        assert not DualParamValidator.valid(
            self._invalid_struct_type
        )

    def test_invalid_dp_m_type(self):
        assert not DualParamValidator.valid(
            self._invalid_param_m_type_param
        )

    def test_invalid_dp_no_m(self):
        assert not DualParamValidator.valid(
            self._invalid_struct_param_ny
        )
