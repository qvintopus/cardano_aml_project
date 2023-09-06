import pandas as pd

class AmlScenarios:
    
    def test_wallet(self, wallet_df, config_list):
        # cache function references
        function_dict = {
            "numeric_threshold" : self.numeric_threshold,
            "linked_addresses" : self.linked_addresses
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
            "status" : "OK" if suspicious_wallets.size() < 1 else "Alert",
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
        print("REPORTING: linked_addresses")
        # Logic to check if each inflow wallet is connected to a specific wallet address
        inflow_wallets = wallet_df[wallet_df['Is Inflow'] == True]
        # TODO: Not sure what this list is
        adress_list_2 = wallet_df[wallet_df['Wallet Address'] == adress_list]['Transaction Hash FK']
        connected_wallets = inflow_wallets[inflow_wallets['Transaction Hash FK'].isin(adress_list_2)]
        
        report = {
            "status" : "OK" if connected_wallets.size() < 1 else "Alert",
            "name" : config.get("name"),
            "type" : config.get("type"),
            "connected_wallets" : connected_wallets,
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
