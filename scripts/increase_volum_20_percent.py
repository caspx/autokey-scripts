#!/usr/bin/env  python3

import subprocess

# warning! this will boost the volume above 100%
subprocess.run('pactl set-sink-volume @DEFAULT_SINK@ +20%', shell=True)
