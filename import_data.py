from src.csv_manager import CardanoCSVManager  # Replace with your actual import

# TODO: fetch data using >> from blockfrost import BlockFrostApi, ApiError, ApiUrls
# TODO: look below for sample to fetch all of the APIs


def main():
    # Example usage
    manager = CardanoCSVManager()


    # TODO: use >> address = api.address(address='addr1qx7tzh4qen0p50ntefz8yujwgqt7zulef6t6vrf7dq4xa82j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pqrkj6fh')
    # Add wallet, token, and transaction data (you would normally get this data from an API)
    manager.add_wallet({
        "address": "addr1qx...",
        "amount": [
            {"unit": "lovelace", "quantity": "42000000"},
            {"unit": "token_id", "quantity": "12"}
        ],
        "stake_address": "stake1ux...",
        "type": "shelley",
        "script": False
    })

    # TODO: use >> token = api.assets_policy(policy_id='qen0p50ntefz8yujwgqt7zule')
    manager.add_token({
        "asset": "asset_id",
        "policy_id": "policy_id",
        "asset_name": "asset_name",
        "quantity": "12000",
        "metadata": {
            "name": "nutcoin",
            "description": "The Nut Coin",
            "ticker": "nutc"
        }
    })
    
    # Add address transactions
    manager.add_address_transactions('addr1...', [
        {'tx_hash': 'hash1', 'tx_index': 6, 'block_height': 69, 'block_time': 1635505891},
        {'tx_hash': 'hash2', 'tx_index': 9, 'block_height': 4547, 'block_time': 1635505987}
    ], [
        {'unit': 'lovelace', 'quantity': '42000000'},
        {'unit': 'token1', 'quantity': '12'}
    ])

    # Add transaction details
    manager.add_transaction_details('hash1', {
        'block': 'block1',
        'block_height': 123456,
        'block_time': 1635505891,
        'slot': 42000000,
        'fees': '182485',
        'deposit': '0',
        'size': 433,
        'valid_contract': True
    })

    # Save all data to CSV files
    manager.save_all()

if __name__ == '__main__':
    main()







# api = BlockFrostApi(
#     project_id='mainnet9ZJfvUG00pAi98d52Nr2OUdLb3oCJYBm',  # or export environment variable BLOCKFROST_PROJECT_ID
#     # optional: pass base_url or export BLOCKFROST_API_URL to use testnet, defaults to ApiUrls.mainnet.value
#     base_url=ApiUrls.mainnet.value,
# )
# try:
#     health = api.health()
#     print(health)   # prints object:    HealthResponse(is_healthy=True)

#     address = api.address(address='addr1qx7tzh4qen0p50ntefz8yujwgqt7zulef6t6vrf7dq4xa82j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pqrkj6fh')
#     print(address.type)  # prints 'shelley'
#     print(object(address))
#     for amount in address.amount:
#         print("amount.unit",amount.unit)  # prints 'lovelace'

# except ApiError as e:
#     print("err:",e)

