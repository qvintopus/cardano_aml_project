from src.data_fetcher import DataFetcher  # Assuming data_fetcher.py is in a src directory
from src.aml_scenarios import AmlScenarios  # Replace with your actual import
from src.table_creator import TableCreator  # Replace with your actual import

def main():
    # data_fetcher = DataFetcher(num_sample_records=3)  # Create 3 sample records for each table
    table_creator = TableCreator()

    # Create and populate wallet table for scenario one
    df_wallet = table_creator.create_and_populate_table('wallet', scenario_name="01_sample", load_from_csv=True)
    
    # Create and populate transaction table for scenario one
    df_transaction = table_creator.create_and_populate_table('transaction', scenario_name="01_sample", load_from_csv=True)

    # Create and populate token table for scenario one
    df_token = table_creator.create_and_populate_table('token', scenario_name="01_sample", load_from_csv=True)

    # df_transaction = data_fetcher.create_transaction_table()
    print("Transaction Table:")
    print(df_transaction)
    
    # df_wallet = data_fetcher.create_wallet_table()
    print("\nWallet Table:")
    print(df_wallet)
    
    # df_token = data_fetcher.create_token_table()
    print("\nToken Table:")
    print(df_token)

    if False: # only for sample creation
        # Save sample data to CSV
        data_fetcher.save_to_csv(df_transactions, "01_transaction_sample_data")
        data_fetcher.save_to_csv(df_wallet, "01_wallet_sample_data")
        data_fetcher.save_to_csv(df_token, "01_token_sample_data")

    # Initialize AML Scenarios
    aml_scenarios = AmlScenarios()

    # Run scenarios
    config_one = {'specific_volume_threshold': 200.0}
    suspicious_wallets_one = aml_scenarios.scenario_one(df_wallet, config_one)
    print("\nSuspicious Wallets in Scenario One:")
    print(suspicious_wallets_one)

    config_two = {'specific_wallet_address': "stake1uy0832h8eyxvxmtzfaanhdkcddfxjmwgfeys7dp7h2ysqhckdgvzv"}
    connected_wallets_two = aml_scenarios.scenario_two(df_wallet, config_two)
    print("\nConnected Wallets in Scenario Two:")
    print(connected_wallets_two)

if __name__ == '__main__':
    main()
