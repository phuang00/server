#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/209.97.149.220/")
sys.path.insert(0,"/var/www/209.97.149.220/209.97.149.220/")

import logging
logging.basicConfig(stream=sys.stderr)

from 209.97.149.220 import app as application
