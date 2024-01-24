import time

from web3 import Web3
from loguru import logger as log
from BlockchainTools.client import Client
from utils import *
from config import *
from models import TokenAmount
from models import BSC
from BlockchainTools.geth_poa import geth_poa_middleware


options = {'count_min': 1, 'count_max': 1}


class Bridge:

    def __init__(self, client: Client):
        self.client = client

        if self.client.network == BSC:
            self.router_address = Web3.to_checksum_address('0xF05F0e4362859c3331Cb9395CBC201E3Fa6757Ea')
            self.decimals = 18

    router_abi = read_json(BRIDGE_ABI)

    def bridge_to_opBNB(self, value: [int | float | str]):
        contract = self.client.w3.eth.contract(
            abi=Bridge.router_abi,
            address=self.router_address
        )
        amount = TokenAmount(value)
        try:
            tx = self.client.send_transaction(
                to=self.router_address,
                data=contract.encodeABI('depositETH',
                                        args=(
                                            1,
                                            '0x'
                                        )),
                value=amount.Wei
            )

            success_tx = self.client.verif_tx(tx)
            time.sleep(2)

            if success_tx:
                log.info(f"https://bscscan.com/tx/{tx.hex()}")
                log.success(f'{self.client.address} | Successfully bridge to opBNB')
                save_data('data/success_bridge.txt', self.client.private_key)
                time.sleep(2)
                print()
            else:
                log.error(f'{self.client.address} | bridge error to opBNB')
                time.sleep(2)
                print()
        except Exception as err:
            log.error(f'{self.client.address} | bridge error to opBNB: {type(err).__name__} {err}')


def bridge_main(key):
    bridge_amount_bnb = random.uniform(MIN_AMOUNT_OPBNB, MAX_AMOUNT_OPBNB)
    client = Client(private_key=key, network=BSC)
    client.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    bridge_instance = Bridge(client=client)
    bridge_instance.bridge_to_opBNB(value=bridge_amount_bnb)

