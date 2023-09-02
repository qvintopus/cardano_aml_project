import pandas as pd

class DataFetcher:
    def __init__(self, num_sample_records=1):
        self.num_sample_records = num_sample_records
    
    def _create_empty_table(self, columns):
        return pd.DataFrame(columns=columns)
    
    def _populate_sample_data(self, df, sample_data):
        for _ in range(self.num_sample_records):
            df = df.append(sample_data, ignore_index=True)
        return df
    
    def create_transaction_table(self):
        columns = [
            'Transaction Hash',
            'Block',
            'Epoch',
            'Slot',
            'Absolute Slot',
            'Timestamp',
            'Total Fees',
            'Total Output',
            'TTL'
        ]
        df_transactions = self._create_empty_table(columns)
        sample_data = {
            'Transaction Hash': "eb79...355ace",
            'Block': 9237581,
            'Epoch': 433,
            'Slot': 394738,
            'Absolute Slot': 102087538,
            'Timestamp': "09/02/2023 2:23:49 PM",
            'Total Fees': 0.426062,
            'Total Output': 430.638247,
            'TTL': 102088426
        }
        return self._populate_sample_data(df_transactions, sample_data)
    
    def create_wallet_table(self):
        columns = [
            'Wallet Address',
            'ADA Spent',
            'Sent Token Id',
            'Sent Token Amount',
            'Transaction Hash FK'
        ]
        df_wallet = self._create_empty_table(columns)
        sample_data = {
            'Wallet Address': "stake1...t49h6",
            'ADA Spent': -1.31886,
            'Sent Token Id': "285c...8f4",
            'Sent Token Amount': 1.31,
            'Transaction Hash FK': "eb79...355ace"
        }
        return self._populate_sample_data(df_wallet, sample_data)
    
    def create_token_table(self):
        columns = [
            'Id',
            'Fingerprint',
            'Asset Name',
            'Created On'
        ]
        df_token = self._create_empty_table(columns)
        sample_data = {
            'Id': "285c...8f4",
            'Fingerprint': "asset1...w5sm",
            'Asset Name': "Toolhead5336",
            'Created On': "08/30/2023 7:24:46 PM"
        }
        return self._populate_sample_data(df_token, sample_data)
