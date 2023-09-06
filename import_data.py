from src.config_manager import CardanoCSVManager  # Replace with your actual import

# TODO: fetch data using >> from blockfrost import BlockFrostApi, ApiError, ApiUrls
# TODO: look below for sample to fetch all of the APIs

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

# TODO: use >> token = api.assets_policy(policy_id='qen0p50ntefz8yujwgqt7zule')
manager.add_transaction({
    "hash": "hash_value",
    "block": "block_value",
    "block_height": 123456,
    "block_time": 1635505891,
    "slot": 42000000,
    "fees": "182485",
    "size": 433
})

# Save all data to CSV files
manager.save_all()




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

