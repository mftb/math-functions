class RequestValidator():
    @staticmethod
    def valid(payload):
        if not isinstance(payload, dict):
            return False
        if 'function' not in payload:
            return False
        if isinstance(payload['function'], str):
            return False
        if 'data' not in payload:
            return False
        if isinstance(payload['data'], dict):
            return False
        return True
