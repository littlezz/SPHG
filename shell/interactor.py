from core import core
from .sanitizer import IntInputSanitizer, StrInputSanitizer
__author__ = 'zz'




def run():


    print(format('sec-pass-gen', '-^50'))
    print('Author: zz')
    print('Never give up any chance to write English :)')
    print('-'*50)
    print('\n')


    max_length = IntInputSanitizer(default_value=core.DEFAULT_MAX_LENGTH).get_input(
        prompt='Please Input the max length of the output password(default {})'.format(core.DEFAULT_MAX_LENGTH),
        second_prompt='Leave blank will use default (10) '
    )

    allow_char_mode = IntInputSanitizer(default_value=core.ALL,
                                        fall_prompt='expect 1-7').get_input(
        prompt='which char that password may contains? 5:exclude uppercase, 1:only digits, get more info from the docs, default is ALL (7)',
        second_prompt='Leave blank use default (7)',
    )

    password1 = StrInputSanitizer(default_value=None,
                                  fall_prompt='Must input secret code').get_input(
        prompt='Your main secret code',
        password=True,
    )


    generator = core.HashGenerator(password1=password1, max_length=max_length, allow_mode=allow_char_mode)

    identification = StrInputSanitizer(default_value=None,
                                       fall_prompt="input the identification for "
                                                   "example, the site's domain").get_input(
        prompt="identification, most use is site's domain, see the doc",
    )

    ret = generator.generate_password(identification)
    print('-'*40)
    print('generate password:', ret)


if __name__ == '__main__':
    import sys
    sys.path.append('..')
    print(sys.path)
    run()
