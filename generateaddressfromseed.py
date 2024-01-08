# Install the web3.py library
# pip install web3
from web3 import Web3
from eth_account import Account
from mnemonic import Mnemonic

def generate_ethereum_addresses(seed_phrase, num_addresses):
    m = Mnemonic("english")
    seed = m.to_seed(seed_phrase)

    addresses = []
    for i in range(num_addresses):
        private_key = Web3.soliditySha3(['bytes32', 'uint256'], [seed, i])
        account = Account.privateKeyToAccount(private_key.hex())
        address = account.address
        addresses.append(address)

    return addresses

if __name__ == "__main__":

    seed_phrase = "direst cutlass wrist mires heads open grates outgrow brutal mantled ageold babel"
    
    # Define the number of addresses you want to generate
    num_addresses = 10

    addresses = generate_ethereum_addresses(seed_phrase, num_addresses)

    print(f"Seed Phrase: {seed_phrase}\n")

    for i, address in enumerate(addresses, start=1):
        print(f"Address {i}: {address}")
