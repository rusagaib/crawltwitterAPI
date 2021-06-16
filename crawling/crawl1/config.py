import os
from os.path import join, dirname
from dotenv import load_dotenv
import sys

# dotenv_path = join(dirname(__file__), '.env')
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONSUMER_KEY=os.getenv('API_KEY')
CONSUMER_SECRET=os.getenv('API_secret')
ACCESS_TOKEN=os.getenv('Access_token')
ACCESS_TOKEN_SECRET=os.getenv('Access_token_secret')

# CONSUMER_KEY=os.environ.get("API_KEY")
# CONSUMER_SECRET=os.environ.get('API_secret')
# ACCESS_TOKEN=os.environ.get('Access_token')
# ACCESS_TOKEN_SECRET=os.environ.get('Access_token_secret')

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben
