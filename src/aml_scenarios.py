import pandas as pd

class AmlScenarios:
    
    def test_wallet(self, wallet_df, config_list):
        # cache function references
        scenario_dict = {
            "numeric_threshold" : self.numeric_threshold,
            "linked_addresses" : self.linked_addresses
        }
        for config in config_list:
            _type = config["type"]
            scenario_dict[_type](wallet_df, config)
           
            # TODO: cache functions into dictionary and access with _type as a key
            # if _type == "numeric_threshold":
            #     self.numeric_threshold(wallet_df, config)
            # if _type == "linked_addresses":
            #     self.linked_addresses(wallet_df, config)
                
    def numeric_threshold(self, wallet_df, config):
        # Retrieve parameters from config
        specific_volume_threshold = config["threshold"]
        unit = config["unit"] ## example: ADA

        # Logic to check if each wallet address has similar inflow and outflow
        grouped = wallet_df.groupby('Wallet Address')['ADA Spent'].sum()
        suspicious_wallets = []
        for address, total_volume in grouped.items():
            if total_volume > specific_volume_threshold:
                suspicious_wallets.append(address)
        
        return suspicious_wallets  # Return list of suspicious wallet addresses
    
    def linked_addresses(self, wallet_df, config):
        # Retrieve parameters from config
        adress_list = config["addresses"]

        ## TODO: change function to support a list of addresses
        
        # Logic to check if each inflow wallet is connected to a specific wallet address
        inflow_wallets = wallet_df[wallet_df['Is Inflow'] == True]
        connected_wallets = inflow_wallets[inflow_wallets['Transaction Hash FK'].isin(
            wallet_df[wallet_df['Wallet Address'] == adress_list]['Transaction Hash FK']
        )]

        return connected_wallets  # Return DataFrame of connected wallet transactions
    
    
    
    
    
    
    
    
    
    
    
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
