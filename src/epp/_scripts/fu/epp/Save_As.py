#!/usr/bin/env python
#coding=utf-8

'''
Save_As.py
####################################

Launcher for epp Save As

:copyright: 2013 by eyeon Software Inc., see AUTHORS for more details
:license: Some rights reserved, see LICENSE for more details
'''

import os
import subprocess

epp_root = os.environ.get("EPP_ROOT", None)

if epp_root is not None:

    epp_launcher = os.path.join(epp_root, "bin", "launcher.exe")

    if os.path.isfile(epp_launcher):

        # Gen doesn't like guests
        process = subprocess.Popen([epp_launcher, "save_as"], shell=True)
