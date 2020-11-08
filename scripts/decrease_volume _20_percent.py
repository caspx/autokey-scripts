#!/usr/bin/env  python3

import subprocess

subprocess.run('pactl set-sink-volume @DEFAULT_SINK@ -20%', shell=True)