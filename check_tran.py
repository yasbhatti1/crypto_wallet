from web3 import Web3
conn = Web3.HTTPProvider("http://127.0.0.1:8545")
w3 = Web3(conn)

print(w3.eth.getTransactionReceipt("0x881d27b33810fc02f4a483b70a9ee9f5f46c16a5f77dd473f3ec7e54612bbe54"))
