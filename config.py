import os
import random
from pathlib import Path
from loguru import logger as log

log.add("logger.log", format="{time:YYYY-MM-DD | HH:mm:ss.SSS} | {level} \t| {line}:{function} | {message}")

min_time_sleep = 15
max_time_sleep = 45

# OKX
OKX_API_KEY = ''
OKX_SECRET_KEY = ''
OKX_PASSPHRASE = ''

okx_fee = "0.002"
MIN_AMOUNT_BNB = 0.002
MAX_AMOUNT_BNB = 0.0025

chain = "BNB-BSC"
currency = "BNB"
destination = "4"

directory_path = Path(__file__).parent

absolute_path = directory_path.absolute()

ABIS_DIR = os.path.join(absolute_path, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
BRIDGE_ABI = os.path.join(ABIS_DIR, 'bridge.json')

MIN_AMOUNT_OPBNB = 0.0013
MAX_AMOUNT_OPBNB = 0.0018