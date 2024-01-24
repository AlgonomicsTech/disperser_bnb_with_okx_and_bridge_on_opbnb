import json
import time
import random
from tqdm import tqdm
from config import *
from typing import Optional


def read_json(path: str, encoding: Optional[str] = None) -> list | dict:
    return json.load(open(path, encoding=encoding))


def sleeping():
    x = random.randint(min_time_sleep, max_time_sleep)
    for _ in tqdm(range(x), desc='Sleeping', bar_format='{l_bar}%s{bar}%s{r_bar}' % ('\033[0m', '\033[0m')):
        time.sleep(1)


def save_data(file_path, data):
    data_line = f"{data}\n"

    if len(data) == 66:
        with open(file_path, 'a') as file:
            file.write(data_line)
        log.info(f" key save in {file_path}")

    else:
        with open(file_path, 'a') as file:
            file.write(data_line)
        log.info(f"{data}| save in {file_path}")


def is_account_passed(file_path, account):
    with open(file_path, 'r') as file:
        for line in file:
            if account in line.split():
                return False
    return True



















# with open('data/private_keys.txt', 'r') as keys_file:
#     private_keys = [line.strip() for line in keys_file.readlines()]
#
#
# with open('data/address.txt', 'r') as keys_file:
#     address = [line.strip() for line in keys_file.readlines()]
