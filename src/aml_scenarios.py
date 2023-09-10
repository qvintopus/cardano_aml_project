import pandas as pd
import json
import os
from datetime import datetime

class AmlScenarios:
    
    def save_report_as_json(self, report_list):
        # Create 'reports' directory if it doesn't exist
        if not os.path.exists('reports'):
            os.makedirs('reports')

        # Get the current date and time to use in the filename
        current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'report_{current_date}.json'

        # Define the path and filename
        path = os.path.join('reports', filename)

        # Write the JSON object to the file
        with open(path, 'w') as f:
            json.dump(report_list, f, indent=4)
        
        print("reports saved in file:", filename)
        
    def generate_warning(self, config, message):
        return {
                "status" : "Warning",
                "name" : config.get("name"),
                "type" : config.get("type"),
                "config" : config,
                "message" : message
            }
      
    def test_wallet(self, df_trnx_utxo, config_list):
        # cache function references
        function_dict = {
            "numeric_threshold" : self.numeric_threshold,
            "linked_addresses" : self.linked_addresses,
            "numeric_aggregated" : self.numeric_aggregated,
            "frequency" : self.frequency,
            "text_match" : self.text_match,
            "column_list_match" : self.column_list_match,
            "geo_restriction" : self.geo_restriction,
            "time_restriction" : self.time_restriction,
            "smart_contract" : self.smart_contract,
            "fee_threshold" : self.fee_threshold,
            "speed_threshold" : self.speed_threshold,
            "anomaly_detection" : self.anomaly_detection,
            "multi_signature" : self.multi_signature,
            "token_swap" : self.token_swap,
            "regulatory_list" : self.regulatory_list,
            "nested_transactions" : self.nested_transactions,
        }
        
        report_list = []
        for config in config_list:
            key_type = config.get("type")
            if key_type == None:
                print("ERROR: no type ", config)
                continue
           
            function_call = function_dict.get(key_type)
            if function_call == None:
                print("ERROR: ", key_type, " scenario isn't implemented or registered")
                continue
            print("Scenario: ", key_type)
            report = function_call(df_trnx_utxo, config)
            
            # TODO: pre-process what is needed
            report_list.append(report)
        
        # Save the report_list as a JSON object
        self.save_report_as_json(report_list)
                
    def numeric_threshold(self, df_trnx_utxo, config):
        # Retrieve parameters from config
        specific_volume_threshold = config["threshold"]
        specific_unit = config["unit"]  # example: "lovelace"

        # Filter the DataFrame to only include rows with the specified unit
        df_filtered = df_trnx_utxo[df_trnx_utxo['unit'] == specific_unit]

        # Group by 'address' and sum the 'quantity' for each group
        address_spent_group = df_filtered.groupby('address')['quantity'].sum()

        # Identify suspicious wallets
        suspicious_wallets = []
        for address, total_volume in address_spent_group.items():
            if total_volume > specific_volume_threshold:
                suspicious_wallets.append(address)

        # Create the report
        report = {
            "status": "OK" if len(suspicious_wallets) < 1 else "Alert",
            "name": config.get("name"),
            "type": config.get("type"),
            "threshold": specific_volume_threshold,
            "suspicious_wallets": suspicious_wallets,
            "config": config
        }

        return report

    def linked_addresses(self, df_trnx_utxo, config):
        # Retrieve parameters from config
        address_list = config["addresses"]

        # Initialize an empty list to store connected transaction hashes
        connected_tx_hashes = []

        # Loop through each address in the list
        for address in address_list:
            # Filter the DataFrame to only include rows with the specified address
            filtered_df = df_trnx_utxo[df_trnx_utxo['address'] == address]

            # Extract unique transaction hashes for the filtered DataFrame
            unique_tx_hashes = filtered_df['tx_hash'].unique().tolist()

            # Add the unique transaction hashes to the connected_tx_hashes list
            connected_tx_hashes.extend(unique_tx_hashes)

        # Remove duplicates from the connected_tx_hashes list
        connected_tx_hashes = list(set(connected_tx_hashes))

        # Create the report
        report = {
            "status": "OK" if len(connected_tx_hashes) < 1 else "Alert",
            "name": config.get("name"),
            "type": config.get("type"),
            "connected_tx_hashes": connected_tx_hashes,
            "config": config
        }

        return report
    
    def numeric_aggregated(self, _df, config):
        # Numeric thresholds for matching against aggregated transaction amounts within a specific time frame.
        # Example: Alert if the total transactions from an address exceed 50,000 ADA in 24 hours.
        # TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def frequency(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def text_match(self, wallet_df, config):
        # Text for matching against transaction table columns like transaction_type, status, etc.
        # Example: Alert if a transaction has a status of "Failed".
        
        column = config.get("column")
        value = config.get("value")
        
        if column not in wallet_df.columns:
            return self.generate_warning(config, "Column doesn't exist")
        
        match_list = wallet_df[wallet_df[column] == value]
        
        report = {
            "status" : "OK" if len(match_list) < 1 else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config,
            "list" : match_list
        }
        return report
    
    def column_list_match(self, wallet_df, config):
        # List of text for matching against some of the transaction table columns.
        # Example: Alert if a transaction involves tokens from a list of "High-Risk Tokens".
        
        column = config.get("column")
        values = config.get("values")
        
        if column not in wallet_df.columns:
            return self.generate_warning(config, "Column doesn't exist")
        
        matched_list = wallet_df[wallet_df[column].isin(values)]
        
        report = {
            "status" : "OK" if len(matched_list) < 1 else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "match" : matched_list,
            "config" : config
        }
        return report
    
    def geo_restriction(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def time_restriction(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def smart_contract(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def fee_threshold(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def speed_threshold(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def anomaly_detection(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def multi_signature(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def token_swap(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def regulatory_list(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def nested_transactions(self, _df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    