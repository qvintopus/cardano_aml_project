import pandas as pd
import json
import os
from datetime import datetime

class AmlScenarios:
    
    def save_report_as_json(self, report_list: list):
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
        
    def generate_warning(self, config: dict, message: str):
        return {
                "status" : "Warning",
                "name" : config.get("name"),
                "type" : config.get("type"),
                "config" : config,
                "message" : message
            }
      
    def test_scenarios(self, wallet_df : pd.DataFrame, utxo_df : pd.DataFrame, token_df : pd.DataFrame, transaction_df : pd.DataFrame, config_list: list):
        # cache functions for wallet scenarios
        wallet_functions = {
            "numeric_threshold" : self.numeric_threshold,
            "wallet_linked_addresses" : self.wallet_linked_addresses,
            "numeric_aggregated" : self.numeric_aggregated,
            "text_match" : self.text_match,
            "wallet_list_match" : self.wallet_list_match,
            "smart_contract" : self.smart_contract,
            "anomaly_detection" : self.anomaly_detection,
            "multi_signature" : self.multi_signature,
            "token_swap" : self.token_swap,
        }
        
        # cache functions for utxo scenarios
        utxo_functions = {
            "utxo_list_match" : self.utxo_list_match,
            "utxo_linked_addresses" : self.utxo_linked_addresses,
            "time_restriction" : self.time_restriction,
            "geo_restriction" : self.geo_restriction,
            "speed_threshold" : self.speed_threshold,
            "nested_transactions" : self.nested_transactions,
            "regulatory_list" : self.regulatory_list,
            
        }
        # cache functions for token scenarios
        token_functions = {
            "token_list_match" : self.token_list_match,
        }
        
        # cache functions for transaction scenarios
        transaction_functions = {
            "fee_threshold" : self.fee_threshold,
            "transaction_list_match" : self.transaction_list_match,
            "frequency" : self.frequency,
        }
        
        
        report_list = []
        for config in config_list:
            key_type = config.get("type")
            print(config.get("name"))
            if key_type == None:
                print("ERROR: no type ", config)
                continue
           
            function_call = wallet_functions.get(key_type)
            
            # TODO: better implementation for data matching
            # WALLET
            if function_call != None:
                report = function_call(wallet_df, config)
            else:
                function_call = utxo_functions.get(key_type)
            
                # UTXO
                if function_call != None:
                    report = function_call(utxo_df, config)
                else:
                    function_call = token_functions.get(key_type)
            
                    # TOKEN
                    if function_call != None:
                        report = function_call(token_df, config)
                    else:
                        function_call = transaction_functions.get(key_type)
                        
                        # TRANSACTION
                        if function_call != None:
                            report = function_call(transaction_df, config)
                        else:
                            print("ERROR: ", key_type, " scenario isn't implemented or registered")
                            continue
            
            # TODO: pre-process what is needed
            report_list.append(report)
        
        # Save the report_list as a JSON object
        self.save_report_as_json(report_list)
                
    def numeric_threshold(self, utxo_df : pd.DataFrame, config: dict):
        # Retrieve parameters from config
        specific_volume_threshold = config["threshold"]
        specific_unit = config["unit"]  # example: "lovelace"

        # Filter the DataFrame to only include rows with the specified unit
        df_filtered = utxo_df[utxo_df['unit'] == specific_unit]

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

    def wallet_linked_addresses(self, wallet_df : pd.DataFrame, config: dict):
        # Retrieve parameters from config
        address_list = config["addresses"]

        # Filter the DataFrame to only include rows with the matching addresses
        filtered_df = wallet_df[wallet_df['address'].isin(address_list)]

        # Create the report
        report = {
            "status": "OK" if filtered_df.empty else "Alert",
            "name": config.get("name"),
            "type": config.get("type"),
            "matched_data": filtered_df.to_dict(),
            "config": config
        }

        return report

    def utxo_linked_addresses(self, utxo_df : pd.DataFrame, config: dict):
        # Retrieve parameters from config
        address_list = config["addresses"]

        # Filter the DataFrame to only include rows with the matching addresses
        filtered_df = utxo_df[utxo_df['address'].isin(address_list)]

        # Create the report
        report = {
            "status": "OK" if filtered_df.empty else "Alert",
            "name": config.get("name"),
            "type": config.get("type"),
            "matched_data": filtered_df.to_dict(),
            "config": config
        }

        return report
    
    def text_match(self, wallet_df : pd.DataFrame, config: dict):
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
            "list" : match_list.to_dict()
        }
        return report
    
    def wallet_list_match(self, wallet_df : pd.DataFrame, config: dict):
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
            "match" : matched_list.to_dict(),
            "config" : config
        }
        return report
    
    def utxo_list_match(self, utxo_df : pd.DataFrame, config: dict):
        # List of text for matching against some of the transaction table columns.
        # Example: Alert if a transaction involves tokens from a list of "High-Risk Tokens".
        
        column = config.get("column")
        values = config.get("values")
        
        if column not in utxo_df.columns:
            return self.generate_warning(config, "Column doesn't exist")
        
        matched_list = utxo_df[utxo_df[column].isin(values)]
        
        report = {
            "status" : "OK" if len(matched_list) < 1 else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "match" : matched_list.to_dict(),
            "config" : config
        }
        return report
    
    def token_list_match(self, token_df : pd.DataFrame, config: dict):
        # List of text for matching against some of the transaction table columns.
        # Example: Alert if a transaction involves tokens from a list of "High-Risk Tokens".
        
        column = config.get("column")
        values = config.get("values")
        
        if column not in token_df.columns:
            return self.generate_warning(config, "Column doesn't exist")
        
        matched_list = token_df[token_df[column].isin(values)]
        
        report = {
            "status" : "OK" if len(matched_list) < 1 else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "match" : matched_list.to_dict(),
            "config" : config
        }
        return report
    
    def transaction_list_match(self, transaction_df : pd.DataFrame, config: dict):
        # List of text for matching against some of the transaction table columns.
        # Example: Alert if a transaction involves tokens from a list of "High-Risk Tokens".
        
        column = config.get("column")
        values = config.get("values")
        
        if column not in transaction_df.columns:
            return self.generate_warning(config, "Column doesn't exist")
        
        matched_list = transaction_df[transaction_df[column].isin(values)]
        
        report = {
            "status" : "OK" if len(matched_list) < 1 else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "match" : matched_list.to_dict(),
            "config" : config
        }
        return report
    
    def fee_threshold(self, transaction_df : pd.DataFrame, config: dict):
        column = "fees"
        treshold = config.get("treshold")
        if column not in transaction_df.columns:
            return self.generate_warning(config, "Fees column doesn't exist in data")
        
        if config.get("is_max"):
            matched_list = transaction_df[transaction_df[column] >= treshold]
        else:
            matched_list = transaction_df[transaction_df[column] <= treshold]
        
        report = {
            "status" : "OK" if matched_list.empty else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "match" : matched_list.to_dict(),
            "config" : config
        }
        return report
    
    def numeric_aggregated(self, _df : pd.DataFrame, config: dict):
        # Numeric thresholds for matching against aggregated transaction amounts within a specific time frame.
        # Example: Alert if the total transactions from an address exceed 50,000 ADA in 24 hours.
        # TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def frequency(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def geo_restriction(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def time_restriction(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def smart_contract(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def speed_threshold(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def anomaly_detection(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def multi_signature(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def token_swap(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def regulatory_list(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def nested_transactions(self, _df : pd.DataFrame, config: dict):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "WIP",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    