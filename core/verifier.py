__author__ = 'zz'


class BaseVerifier:
    def verify(self, value):
        raise NotImplementedError


class IntVerifier(BaseVerifier):
    def __index__(self, upper, bot):
        self.upper = upper
        self.bot = bot

    def verify(self, value):
        if isinstance(value, int):
            return False

        if not (self.bot <= value <= self.upper):
            return False

        return True


class StringNotEmptyVerifier(BaseVerifier):
    def verify(self, value):
        if str(value).strip():
            return True

        return False



