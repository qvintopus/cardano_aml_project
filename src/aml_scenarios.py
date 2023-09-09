import pandas as pd

class AmlScenarios:
    
    def generate_warning(self, config, message):
        return {
                "status" : "Warning",
                "name" : config.get("name"),
                "type" : config.get("type"),
                "config" : config,
                "message" : message
            }
    
    def test_wallet(self, wallet_df, config_list):
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
            report = function_call(wallet_df, config)
            
            # TODO: pre-process what is needed
            report_list.append(report)
        
                
    def numeric_threshold(self, wallet_df, config):
        # Numeric threshold for matching against individual transaction amounts.
        # Example: Alert if any transaction is greater than 10,000 ADA.
        
        # Retrieve parameters from config
        specific_volume_threshold = config["threshold"]
        unit = config.get("unit") ## example: ADA

        # Logic to check if each wallet address has similar inflow and outflow
        address_spent_group = wallet_df.groupby('Wallet Address')['ADA Spent'].sum()
        suspicious_wallets = []
        for address, total_volume in address_spent_group.items():
            if total_volume > specific_volume_threshold:
                suspicious_wallets.append(address)
        
        
        report = {
            "status" : "OK" if len(suspicious_wallets) < 1 else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "treshold" : specific_volume_threshold,
            "suspicious_wallets" : suspicious_wallets,
            "config" : config
        }
        return report
    
    def linked_addresses(self, wallet_df, config):
        # Retrieve parameters from config
        adress_list = config["addresses"]

        # Logic to check if each inflow wallet is connected to a specific wallet address
        
        ## TODO: Double check the logic, maybe make explicit variables
        matched_list = wallet_df[wallet_df['Wallet Address'].isin(adress_list)]['Transaction Hash FK']
        inflow_wallets = wallet_df[wallet_df['Is Inflow'] == True]
        connected_wallets = inflow_wallets[inflow_wallets['Transaction Hash FK'].isin(matched_list)]
        
        report = {
            "status" : "OK" if len(connected_wallets) < 1 else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "connected_wallets" : connected_wallets,
            "config" : config
        }
        return report
    
    def numeric_aggregated(self, wallet_df, config):
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
    
    def frequency(self, wallet_df, config):
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
    
    def geo_restriction(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def time_restriction(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def smart_contract(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def fee_threshold(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def speed_threshold(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def anomaly_detection(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def multi_signature(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def token_swap(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def regulatory_list(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    def nested_transactions(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "config" : config
        }
        return report
    
    
    
    
    
    
    
    
    
    
    
    def scenario_one(self, wallet_df, config):
        # Retrieve parameters from config
        specific_volume_threshold = config.get('specific_volume_threshold', 1000.0)

        # Logic to check if each wallet address has similar inflow and outflow
        grouped = wallet_df.groupby('Wallet Address')['ADA Spent'].sum()
        suspicious_wallets = []
        for address, total_volume in grouped.items():
            if total_volume > specific_volume_threshold:
                suspicious_wallets.append(address)
        
        return suspicious_wallets  # Return list of suspicious wallet addresses

    def scenario_two(self, wallet_df, config):
        # Retrieve parameters from config
        specific_wallet_address = config.get('specific_wallet_address', "some_address")

        # Logic to check if each inflow wallet is connected to a specific wallet address
        inflow_wallets = wallet_df[wallet_df['Is Inflow'] == True]
        connected_wallets = inflow_wallets[inflow_wallets['Transaction Hash FK'].isin(
            wallet_df[wallet_df['Wallet Address'] == specific_wallet_address]['Transaction Hash FK']
        )]

        return connected_wallets  # Return DataFrame of connected wallet transactions
