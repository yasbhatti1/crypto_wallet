# Import dependencies
import subprocess
import json
import os
from dotenv import load_dotenv
from bit import wif_to_key
from web3 import Web3
from eth_account import Account
from pprint import pprint

# Conn to local network using web3
conn = Web3.HTTPProvider("http://127.0.0.1:8545")
w3 = Web3(conn)

# Load and set environment variables for mnemonic_phrase
load_dotenv()
mnemonic_key=os.getenv("mnemonic_key")

# Import constants.py to use in the functions
from constants import *

# Create function called `derive_wallets` that will convert mnemonic to keys 
def derive_wallets(coin):
    command = f'./derive -g --mnemonic="{mnemonic_key}" --cols=address,index,path,privkey,pubkey,pubkeyhash,xprv,xpub --coin="{coin}" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create dictionary object called coins to store the output from `derive_wallets`
coins = {BTCTEST : (derive_wallets(BTCTEST)) , ETH : (derive_wallets(ETH))}
#pprint(coins)

# convert BTC and ETH private key strings to account objects
key_btc = wif_to_key(coins['btc-test'][0]['privkey'])
key_eth = Account.from_key(coins['eth'][0]['privkey'])
add_btc = coins['btc-test'][0]['address']

#pprint(add_btc)

# Create function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(account, recipient, amount):
    gasestimates = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
        )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice, 
        "gas": gasestimates,
        "nonce": w3.eth.getTransactionCount(account.address)
        }

# Create a function called `send_eth_tx` that calls `create_tx`, signs and sends the transaction.
def send_eth_tx(account, recipient, amount):
        tx = create_tx(account, recipient, amount)
        signed_tx = account.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("My Transaction")
        print(result.hex())
        return result.hex()
#----------------------------------------------------------------------------------
# For running Ethereum coin
#----------------------------------------------------------------------------------
send_eth_tx(key_eth, "0x3576D690dFb33D53EbEF25192bcaE85A81Ba4D16", 7777777777777)
#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------
# For running BTC coin
#----------------------------------------------------------------------------------

# Please uncommnent (remove hash#) in the code below
addresses = [add_btc, "mi9KYkf1aZzDts8tMyTbjKcQjqEVr8gotN"]
outputs = []
for address in addresses:
    outputs.append((address, 0.00001, 'btc'))
#print(key_btc.send(outputs))
#print("")
#print("")
#print(key_btc.get_balance("btc"))
#print(key_btc.get_balance("usd"))
#print("My transactions")      
#print(key_btc.get_transactions())
#----------------------------------------------------------------------------------



