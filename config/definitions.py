import os
from datetime import datetime

TODAY_DATE = datetime.today().strftime('%Y-%m-%d')
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
