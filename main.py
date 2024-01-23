import time
from logo import print_ALGONOMICS
from os.path import exists
from config import *
from utils import *
from bridge_on_opbnb import bridge_main


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
        log.warning("In process development...")

    elif software_method == 2:
        for private_key in private_keys_list:
            if is_account_passed('data/success_bridge.txt', private_key):
                bridge_main(private_key)
            else:
                log.info("Account already use")
                print()
                log.info("Go to the next account")
                continue

    else:
        log.error("Unknown method, choose 1 or 2!")


    print()
    log.success('Work completed successfully')
    log.debug('Press Enter to exit...')
    input()


if __name__ == '__main__':
    main()
