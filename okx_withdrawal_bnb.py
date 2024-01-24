import okx.Funding as Funding
from config import *



def initialize_api(apikey, secretkey, passphrase, flag="0"):
    return Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)


fundingAPI = initialize_api(OKX_API_KEY, OKX_SECRET_KEY, OKX_PASSPHRASE)


def handle_make_withdrawal(response, to_address, amount):
    if response.get('code') == '0':
        log.success(f"{to_address} | {amount} BNB | successfully withdrawal")
        return True
    else:
        log.error(f"{to_address} | {amount} BNB | {response.get('msg')} | error code: {response.get('code')}")
        return False


def make_withdrawal(to_address):
    api = fundingAPI
    okx_amount_bnb = random.uniform(MIN_AMOUNT_BNB, MAX_AMOUNT_BNB)
    result = api.withdrawal(ccy=currency,
                            toAddr=to_address,
                            amt=okx_amount_bnb,
                            fee=okx_fee,
                            dest=destination,
                            chain=chain)
    return handle_make_withdrawal(result, to_address, okx_amount_bnb)

