#!/usr/bin/env  python3

try:
    import webbrowser
except ImportError:
    err_msg = '"webbrowser" must be installed'
    dialog.info_dialog(title='Error', message=err_msg)
    exit(1)

# get copied phrase
phrase = clipboard.get_selection()
phrase = phrase.strip()

# https://www.morfix.co.il/{phrase}
translate_url = f'https://www.morfix.co.il/{phrase}'

# shoot
webbrowser.open_new_tab(translate_url)
