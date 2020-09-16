from entities.function_type import FunctionType


class FunctionTypeValidator():
    @staticmethod
    def valid(f_type):
        return FunctionType.check_type(f_type)
