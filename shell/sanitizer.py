from getpass import getpass
__author__ = 'zz'


class BaseInputSanitizer:
    default_fall_prompt = ''

    def __init__(self, default_value, fall_prompt=None):
        self._fall_prompt = fall_prompt
        self.default_value = default_value

    @property
    def fall_prompt(self):
        if self._fall_prompt:
            return self._fall_prompt
        return self.default_fall_prompt

    def clean(self, value):
        raise NotImplementedError

    def get_input(self, prompt, second_prompt='', password=False):
        print(prompt)
        while True:

            if not password:
                val = input(second_prompt)
            else:
                val = getpass()

            ret, success = self.clean(val)
            if success:
                break
            else:
                print(self.fall_prompt)

        return ret


class IntInputSanitizer(BaseInputSanitizer):
    except_type = int
    default_fall_prompt = 'Sorry, expect integer'

    def clean(self, value):
        if value.strip() is '':
            return self.default_value, True

        try:
            result = self.except_type(value)
        except ValueError:
            return None, False

        return result, True


class PasswordInputSanitizer(BaseInputSanitizer):
    def clean(self, value):
        if value.strip() is '':
            return None, False
        else:
            return value, True