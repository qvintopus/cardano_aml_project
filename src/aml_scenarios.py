import pandas as pd

class AmlScenarios:
    
    def test_wallet(self, wallet_df, config_list):
        # cache function references
        function_dict = {
            "numeric_threshold" : self.numeric_threshold,
            "linked_addresses" : self.linked_addresses,
            "numeric_aggregated" : self.numeric_aggregated,
            "frequency" : self.frequency,
            "list_text_match" : self.list_text_match,
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

        ## TODO: change function to support a list of addresses
        # Logic to check if each inflow wallet is connected to a specific wallet address
        inflow_wallets = wallet_df[wallet_df['Is Inflow'] == True]
        connected_wallets = []
        for _adress in adress_list:
            # TODO: Not sure what this list is
            matched_list = wallet_df[wallet_df['Wallet Address'] == _adress]['Transaction Hash FK']
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
        #TODO: implement
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
    
    def list_text_match(self, wallet_df, config):
        #TODO: implement
        print("ERROR: ", config.get("type"), " not implemented")
        report = {
            "status" : "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
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
