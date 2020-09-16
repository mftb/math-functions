class SingleParamValidator():
    @staticmethod
    def valid(data):
        if not isinstance(data, dict):
            return False
        if 'n' not in data:
            return False
        if not isinstance(data['n'], int):
            return False
        return data['n'] >= 0


class DualParamValidator():
    @staticmethod
    def valid(data):
        if not isinstance(data, dict):
            return False
        if 'n' not in data:
            return False
        if not isinstance(data['n'], int):
            return False
        if 'm' not in data:
            return False
        if not isinstance(data['m'], int):
            return False
        return data['n'] >= 0 and data['m'] >= 0
