import logging
import time
from logo import print_ALGONOMICS
from os.path import exists
from config import *
from utils import *
from bridge_on_opbnb import bridge_main
from okx_withdrawal_bnb import make_withdrawal


def main():

    if exists(path='data/address.txt'):
        with open(file='data/address.txt', mode='r', encoding='utf-8-sig') as file:
            address_list = [row.strip() for row in file]
    else:
        address_list = []

    if exists(path='data/private_keys.txt'):
        with open(file='data/private_keys.txt', mode='r', encoding='utf-8-sig') as file:
            private_keys_list = [row.strip() for row in file]
    else:
        private_keys_list = []


    print()
    print_ALGONOMICS("ALGONOMICS")
    time.sleep(2)
    print()

    log.success(f'Downloaded successfully {len(address_list)} address wallets | {len(private_keys_list)} keys wallets')
    log.info('💰 DONATION EVM ADDRESS: 0x4A080654795e526801954493BD0D712609d0ccEF')
    time.sleep(2)

    software_method = int(input('\n1. Disperser BNB with OKX \n'
                                '2. Bridge BNB on OpBNB\n'
                                'Make your choice:\n'))
    print()

    if software_method == 1:
        counter = 0
        for to_address in address_list:
            counter += 1
            log.info(f"work progress: {counter}/{len(address_list)} | in line: {len(address_list) - counter}")
            time.sleep(1)
            if is_account_passed('data/success_send.txt', to_address):
                if make_withdrawal(to_address):
                    save_data('data/success_send.txt', to_address)
                    time.sleep(1)
                    print()
            else:
                log.info(f"{to_address} | Account already use")
                time.sleep(1)
                print()
                log.info("Go to the next account")
                time.sleep(1)
                print()
                continue
            sleeping()
            print()
            print()


    elif software_method == 2:
        counter = 0
        for private_key in private_keys_list:
            counter += 1
            log.info(f"work progress: {counter}/{len(private_keys_list)} | in line: {len(private_keys_list) - counter} ")
            time.sleep(1)
            if is_account_passed('data/success_bridge.txt', private_key):
                bridge_main(private_key)
            else:
                log.info("Account already use")
                time.sleep(1)
                print()
                log.info("Go to the next account")
                print()
                continue
            sleeping()
            print()
            print()

    else:
        log.warning("Unknown method, choose 1 or 2!")

    print()
    log.debug('The work is completed..')


if __name__ == '__main__':
    main()
