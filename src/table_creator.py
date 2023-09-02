import pandas as pd

class TableCreator:
    def create_table(self, table_name):
        if table_name == 'wallet':
            columns = ['Wallet Address', 'ADA Spent', 'Token Id', 'Amount', 'Is Inflow', 'Transaction Hash FK']
        elif table_name == 'transaction':
            columns = ['Transaction Hash', 'Block', 'Epoch', 'Slot', 'Absolute Slot', 'Timestamp', 'Total Fees', 'Total Output', 'TTL']
        elif table_name == 'token':
            columns = ['Id', 'Fingerprint', 'Asset Name', 'Created On']
        else:
            raise ValueError("Invalid table name.")
        return pd.DataFrame(columns=columns)

    def load_csv_for_table(self, table_name, scenario_name):
        file_path = f"data/{scenario_name}_{table_name}_data.csv"
        return pd.read_csv(file_path)

    def create_and_populate_table(self, table_name, scenario_name=None, load_from_csv=False):
        if load_from_csv and scenario_name:
            return self.load_csv_for_table(table_name, scenario_name)
        else:
            return self.create_table(table_name)
        