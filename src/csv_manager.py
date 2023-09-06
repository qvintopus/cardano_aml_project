# src/config_manager.py
import csv

class CardanoCSVManager:
    def __init__(self):
        # Your code here
        pass
    def __init__(self):
        self.wallet_data = []
        self.token_data = []
        self.transaction_data = []
        
    def add_wallet(self, wallet_info):
        for amount in wallet_info['amount']:
            row = [
                wallet_info['address'],
                amount['unit'],
                amount['quantity'],
                wallet_info.get('stake_address', ''),
                wallet_info.get('type', ''),
                wallet_info.get('script', '')
            ]
            self.wallet_data.append(row)
    
    def add_token(self, token_info):
        row = [
            token_info['asset'],
            token_info['policy_id'],
            token_info['asset_name'],
            token_info['quantity'],
            token_info['metadata'].get('name', ''),
            token_info['metadata'].get('description', ''),
            token_info['metadata'].get('ticker', '')
        ]
        self.token_data.append(row)
    
    def add_transaction(self, transaction_info):
        row = [
            transaction_info['hash'],
            transaction_info['block'],
            transaction_info['block_height'],
            transaction_info['block_time'],
            transaction_info['slot'],
            transaction_info['fees'],
            transaction_info['size']
        ]
        self.transaction_data.append(row)
    
    def save_to_csv(self, filename, data, headers):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
    
    def save_all(self):
        self.save_to_csv('wallet_address.csv', self.wallet_data, ["address", "unit", "quantity", "stake_address", "type", "script"])
        self.save_to_csv('token.csv', self.token_data, ["asset", "policy_id", "asset_name", "quantity", "name", "description", "ticker"])
        self.save_to_csv('transactions.csv', self.transaction_data, ["hash", "block", "block_height", "block_time", "slot", "fees", "size"])

########################################################
########################################################
########################################################


# # Example usage
# manager = CardanoCSVManager()

# # Add wallet, token, and transaction data (you would normally get this data from an API)
# manager.add_wallet({
#     "address": "addr1qx...",
#     "amount": [
#         {"unit": "lovelace", "quantity": "42000000"},
#         {"unit": "token_id", "quantity": "12"}
#     ],
#     "stake_address": "stake1ux...",
#     "type": "shelley",
#     "script": False
# })

# manager.add_token({
#     "asset": "asset_id",
#     "policy_id": "policy_id",
#     "asset_name": "asset_name",
#     "quantity": "12000",
#     "metadata": {
#         "name": "nutcoin",
#         "description": "The Nut Coin",
#         "ticker": "nutc"
#     }
# })

# manager.add_transaction({
#     "hash": "hash_value",
#     "block": "block_value",
#     "block_height": 123456,
#     "block_time": 1635505891,
#     "slot": 42000000,
#     "fees": "182485",
#     "size": 433
# })

# # Save all data to CSV files
# manager.save_all()


