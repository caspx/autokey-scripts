#!/usr/bin/env python3

import os
from os import walk
from os.path import join


# very simple logger
# def log(line):
#     system.exec_command('echo "{}" >> /tmp/autokey.log'.format(line))
#

# autokey data dir - You can set it manually
USER = os.getenv('USER')
AUTOKEY_DATA_DIR = f'/home/{USER}/.config/autokey/data'

# list all phrases and scripts located in autokey directory
autokey_data_files = []
for (dirpath, dirnames, filenames) in walk(AUTOKEY_DATA_DIR):
    files = [join(dirpath, f) for f in filenames if f.endswith(('.txt', '.py'))]
    autokey_data_files.extend(files)

# Autokey scripting API: https://autokey.github.io/lib.scripting-module.html
# Zenity: https://linux.die.net/man/1/zenity
while True:
    ret_code, phrase_name = dialog.input_dialog(title="Search",
                                                message='Enter a phrase name')
    if ret_code != 0:
        exit(1)

    # currently check phrase_name against file path and name only
    candidates = {}
    phrase_name = phrase_name.lower()
    for f in autokey_data_files:
        if phrase_name in f.lower():
            path = f
            name = os.path.basename(f).split('.')[0]
            # known issue - may run over a phrase with the same name
            candidates[name] = path

    # show a list of matching phrases
    choices = candidates.keys()
    ret_code, choice = dialog.list_menu(choices,
                                        title='Search',
                                        text='Results',
                                        height="500",
                                        width="400")

    # printing the selected phrase
    if ret_code == 0:
        path = candidates[choice]
        try:
            with open(path) as f:
                phrase = f.read()
            keyboard.send_keys(phrase)
        except Exception as e:
            pass

        exit(0)
    # keep the search dialog open
    else:
        continue
