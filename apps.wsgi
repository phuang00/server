#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/apps/")
sys.path.insert(0,"/var/www/apps/apps/")

import logging
logging.basicConfig(stream=sys.stderr)

from apps import app as application
