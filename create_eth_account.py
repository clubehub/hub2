from eth_account import Account
import json

# Generate an Ethereum account
account = Account.create()

# Save the private key to a JSON file
private_key = account.key.hex
with open('private_key.json', 'w') as json_file:
    json.dump({'private_key': private_key}, json_file)
