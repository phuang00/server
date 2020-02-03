#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/P0/")
sys.path.insert(0,"/var/www/P0/P0/")

import logging
logging.basicConfig(stream=sys.stderr)

from P0 import app as application
