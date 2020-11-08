#!/usr/bin/env python3

try:
    import stringcase
except ImportError:
    err_msg = '"stringcase" must be installed'
    dialog.info_dialog(title='Error', message=err_msg)
    exit(1)


# very simple logger for debugging
# def log(line):
#     system.exec_command('echo "{}" >> /tmp/autokey.log'.format(line))

# Remove trailing or leading white space and find if there are multiple
# phrases.
try:
    phrase = clipboard.get_selection()
    phrase = phrase.strip()
except:
    err_msg = 'was not able to get selected text'
    dialog.info_dialog(title='Error', message=err_msg)
    exit(1)

choices = [
    'camelcase',
    'capitalcase',
    'constcase',
    'lowercase',
    'pascalcase',
    'pathcase',
    'sentencecase',
    'snakecase',
    'spinalcase',
    'titlecase',
    'trimcase',
    'uppercase',
    'alphanumcase']

ret_code, choice = dialog.list_menu(choices,
                                    title=phrase,
                                    text='Select Case',
                                    height="500",
                                    width="200")

if ret_code == 0:
    case_func = getattr(stringcase, choice)
    phrase_new_case = case_func(phrase)
    keyboard.send_keys(phrase_new_case)
    exit(0)


