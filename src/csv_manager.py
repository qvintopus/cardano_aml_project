# src/config_manager.py
import csv

class CardanoCSVManager:
    def __init__(self):
        # Your code here
        pass
    def __init__(self):
        self.wallet_data = []
        self.token_data = []
        self.address_transactions_data = []
        self.transaction_details_data = []
        
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
    
    def add_address_transactions(self, address, transactions, output_amounts):
        for tx in transactions:
            for output in output_amounts:
                row = [
                    address,
                    tx['tx_hash'],
                    tx['tx_index'],
                    tx['block_height'],
                    tx['block_time'],
                    output['unit'],
                    output['quantity']
                ]
                self.address_transactions_data.append(row)

    def add_transaction_details(self, tx_hash, transaction_details):
        row = [
            tx_hash,
            transaction_details['block'],
            transaction_details['block_height'],
            transaction_details['block_time'],
            transaction_details['slot'],
            transaction_details['fees'],
            transaction_details['deposit'],
            transaction_details['size'],
            transaction_details['valid_contract']
        ]
        self.transaction_details_data.append(row)

    def save_to_csv(self, filename, data, headers):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
    
    def save_all(self):
        self.save_to_csv('wallet_address.csv', self.wallet_data, ["address", "unit", "quantity", "stake_address", "type", "script"])
        self.save_to_csv('token.csv', self.token_data, ["asset", "policy_id", "asset_name", "quantity", "name", "description", "ticker"])
        self.save_to_csv('address_transactions.csv', self.address_transactions_data, ["address", "tx_hash", "tx_index", "block_height", "block_time", "unit", "quantity"])
        self.save_to_csv('transaction_details.csv', self.transaction_details_data, ["tx_hash", "block", "block_height", "block_time", "slot", "fees", "deposit", "size", "valid_contract"])


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


