from core import core
from .sanitizer import IntInputSanitizer, PasswordInputSanitizer
__author__ = 'zz'




def run():


    print(format('sec-pass-gen', '-^50'))
    print('Author: zz')
    print('Never give up any chance to write English :)')
    print('\n'*2)


    max_length = IntInputSanitizer(default_value=core.DEFAULT_MAX_LENGTH).get_input(
        prompt='Please Input the max length of the output password(default {})'.format(core.DEFAULT_MAX_LENGTH),
        second_prompt='(Leave blank will use default) '
    )

    allow_char_mode = IntInputSanitizer(default_value=core.ALL,
                                        fall_prompt='expect 0-7').get_input(
        prompt='which char that password may contains? 5:exclude uppercase, 0:only digits, get more info from the docs, default is ALL (7)',
        second_prompt='Leave blank use default',
    )

    password1 = PasswordInputSanitizer(default_value=None,
                                       fall_prompt='Must input secret code').get_input(
        prompt='Your main secret code',
        password=True,
    )






if __name__ == '__main__':
    import sys
    sys.path.append('..')
    print(sys.path)
    run()
