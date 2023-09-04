from src.aml_scenarios import AmlScenarios  # Replace with your actual import
from src.table_creator import TableCreator  # Replace with your actual import
from src.config_manager import ConfigManager  # Replace with your actual import

def main():
    table_creator = TableCreator()

    # Create and populate wallet table for scenario one
    df_wallet = table_creator.create_and_populate_table('wallet', scenario_name="01_sample", load_from_csv=True)
    df_transaction = table_creator.create_and_populate_table('transaction', scenario_name="01_sample", load_from_csv=True)
    df_token = table_creator.create_and_populate_table('token', scenario_name="01_sample", load_from_csv=True)

    print("Transaction Table:")
    print(df_transaction)
    
    print("\nWallet Table:")
    print(df_wallet)
    
    print("\nToken Table:")
    print(df_token)

    # Initialize AML Scenarios
    aml_scenarios = AmlScenarios()

    # Run scenarios
    config_one = {'specific_volume_threshold': 200.0} ## create config
    suspicious_wallets_one = aml_scenarios.scenario_one(df_wallet, config_one)
    print("\nSuspicious Wallets in Scenario One:")
    print(suspicious_wallets_one)

    config_two = {'specific_wallet_address': "stake1uy0832h8eyxvxmtzfaanhdkcddfxjmwgfeys7dp7h2ysqhckdgvzv"}
    connected_wallets_two = aml_scenarios.scenario_two(df_wallet, config_two)
    print("\nConnected Wallets in Scenario Two:")
    print(connected_wallets_two)

    config_manager = ConfigManager()
    config_list = config_manager.fetch_configs()
    aml_scenarios.test_wallet(df_wallet, config_list)

if __name__ == '__main__':
    main()

