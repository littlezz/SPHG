from string import ascii_lowercase, ascii_uppercase, digits
import itertools
from hashlib import sha512


__author__ = 'zz'


# allow_letter_mode
# bit mean low, upper, digits
ALL = 7  # 111
EXCLUDE_UPPER = 5  # 101
ONLY_DIGITS = 1  # 001


DEFAULT_MAX_LENGTH = 10


class BaseGenerator:
    """
    hash the main password and identification 3 times, then combine them and hash it twice
    """
    def __init__(self, password1, max_length=DEFAULT_MAX_LENGTH, allow_mode=ALL):
        assert isinstance(allow_mode, int), 'allow_mode must be integer'
        assert  0 < allow_mode < 8, 'allow_mode exceed'
        assert max_length > 0, 'max_length exceed'

        self.max_length = max_length
        self.allow_mode = allow_mode
        self.password1 = self.hash(password1, times=3)

    def _get_allow_char_from_mode(self):
        _mode_stack = (ascii_lowercase, ascii_uppercase, digits)
        mode = list(int(i) for i in format(self.allow_mode, '0=3b'))
        return ''.join(itertools.compress(_mode_stack, mode))

    def get_allow_char(self):
        return self._get_allow_char_from_mode()

    @staticmethod
    def hash(val, times=1):
        """
        return sha512 hash bytes result
        :param val:
        :return:
        """
        if isinstance(val, str):
            temp = val.encode()
        else:
            temp = val

        for i in range(times):
            temp = sha512(temp).digest()
        return temp

    def _get_result_from_bytes(self, bytes_result):
        allow_chars = self.get_allow_char()
        mod = len(allow_chars)
        ret = []
        for b in bytes_result[:self.max_length]:
            ret.append(allow_chars[b % mod])

        return ''.join(ret)

    def generate_password(self,  identification):
        identification = self.hash(identification, times=3)
        byte_result = self.hash(self.password1+identification, times=2)

        result = self._get_result_from_bytes(byte_result)
        return result


class HashGenerator(BaseGenerator):
    pass



