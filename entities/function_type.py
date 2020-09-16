class FunctionType():
    _types = [
        'fibonacci',
        'fibonacci_naive',
        'factorial',
        'ackermann',
        'ackermann_naive'
    ]

    @staticmethod
    def check_type(f_type):
        return f_type in FunctionType._types
