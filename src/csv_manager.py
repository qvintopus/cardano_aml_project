# src/config_manager.py
import csv
import pandas as pd

class CardanoCSVManager:
    def __init__(self):
        self.wallet_data = []
        self.token_data = []
        self.address_transactions_data = []
        self.transaction_details_data = []
        self.transaction_utxo_data = []
        
    def add_wallet(self, wallet_info):
        for amount in wallet_info.amount:
            row = [
                wallet_info.address,
                amount.unit,
                amount.quantity,
                getattr(wallet_info, 'stake_address', ''),  # Using getattr instead of get
                getattr(wallet_info, 'type', ''),
                getattr(wallet_info, 'script', '')
            ]
            self.wallet_data.append(row)
    
    def add_token_D(self, row):
        self.token_data.append(row)

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
    
    def add_transaction_D(self, row):
        self.address_transactions_data.append(row)

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

    def add_transaction_details_D(self, row):
        self.transaction_details_data.append(row)
    
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
        
    def add_transaction_UTXOs(self, transaction_json):
        # Convert Namespace to dictionary if needed
        transaction_json = vars(transaction_json)

        tx_hash = transaction_json['hash']
        
        # Handle inputs
        for input in transaction_json['inputs']:
            for amount in input.amount:
                row = [
                    tx_hash,
                    'input',
                    input.address,
                    amount.unit,
                    amount.quantity,
                    input.output_index,
                    input.data_hash,
                    input.inline_datum,
                    input.reference_script_hash,
                    input.collateral,
                    input.reference
                ]
                self.transaction_utxo_data.append(row)
        
        # Handle outputs
        for output in transaction_json['outputs']:
            for amount in output.amount:
                row = [
                    tx_hash,
                    'output',
                    output.address,
                    amount.unit,
                    amount.quantity,
                    output.output_index,
                    output.data_hash,
                    output.inline_datum,
                    output.reference_script_hash,
                    output.collateral
                ]
                self.transaction_utxo_data.append(row)

    def namespace_to_list(self, namespace_obj, attributes):
        return [getattr(namespace_obj, attr, '') for attr in attributes]

    def save_to_csv(self, filename, data, headers):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)  # Make sure data is a list of lists or some other iterable of iterables


    def save_all(self, scenario_name):
        print(f"saving scenario {scenario_name} to CSVs...")
        headers_transaction_details = ["hash", "block", "block_height", "block_time", "slot", "fees", "deposit", "size", "valid_contract"]
        headers_token = ["asset", "policy_id", "asset_name", "quantity", "name", "description", "ticker"]
        headers_transaction_utxo = ["tx_hash", "type", "address", "unit", "quantity", "output_index", "data_hash", "inline_datum", "reference_script_hash", "collateral", "reference"]
        headers_address_transactions = ["address", "tx_hash", "tx_index", "block_height", "block_time", "unit", "quantity"]
        headers_wallet = ["address", "unit", "quantity", "stake_address", "type", "script"]

        transaction_details_data_list = [self.namespace_to_list(namespace_obj, headers_transaction_details) for namespace_obj in self.transaction_details_data]
        token_data_list = [self.namespace_to_list(namespace_obj, headers_token) for namespace_obj in self.token_data]

        self.save_to_csv(f"data/{scenario_name}_wallet_address.csv", self.wallet_data, headers_wallet)
        self.save_to_csv(f"data/{scenario_name}_token.csv", token_data_list, headers_token)
        self.save_to_csv(f"data/{scenario_name}_address_transactions.csv", self.address_transactions_data, headers_address_transactions)
        self.save_to_csv(f"data/{scenario_name}_transaction_details.csv", transaction_details_data_list, headers_transaction_details)
        self.save_to_csv(f"data/{scenario_name}_transaction_utxos.csv", self.transaction_utxo_data, headers_transaction_utxo)

    # Method to load a CSV file into a Pandas DataFrame
    def load_csv_to_dataframe(self, scenario_name, table_name):
        file_path = f"data/{scenario_name}_{table_name}.csv"
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"No CSV file found at {file_path}.")


########################################################
########################################################
########################################################

