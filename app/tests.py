from django.test import TestCase
from web3 import Web3
import json
# Create your tests here.

ABI = json.loads(ABI_json)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/d4e80746cb23423ab837fce195de1cf5'))
print(w3.isConnected())

contract_address = '0x83053843161Ef9fe5b44211a56d2ADf201BeDEF9'

contract = w3.eth.contract(contract_address, abi=ABI)
holder = Web3.toChecksumAddress('0x703dfcc029cb05d5f929a75e0dcc0c6bb292edb6')
raw_balance = contract.functions.balanceOf(holder).call()
print(raw_balance)