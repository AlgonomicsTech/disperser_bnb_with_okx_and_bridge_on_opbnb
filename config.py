import os
import random
from pathlib import Path
from loguru import logger as log

log.add("logger.log", format="{time:YYYY-MM-DD | HH:mm:ss.SSS} | {level} \t| {line}:{function} | {message}")

min_time_sleep = 10
max_time_sleep = 30

directory_path = Path(__file__).parent

absolute_path = directory_path.absolute()

ABIS_DIR = os.path.join(absolute_path, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
BRIDGE_ABI = os.path.join(ABIS_DIR, 'bridge.json')

amount_bnb = random.uniform(0.001, 0.0015)