from glob import glob
from src.aml_scenarios import AmlScenarios  # Replace with your actual import
from src.table_creator import TableCreator  # Replace with your actual import
from src.config_manager import ConfigManager  # Replace with your actual import
from src.csv_manager import CardanoCSVManager  # Replace with your actual import



AMOUNT_DISPLAY_TABLE_DATA = 10

def main():
    global AMOUNT_DISPLAY_TABLE_DATA
    csv_manager = CardanoCSVManager()

    # Create and populate wallet table for scenario one
    wallet_df = csv_manager.load_csv_to_dataframe("03_real","wallet_address")
    # df_transaction = csv_manager.load_csv_to_dataframe("03_real","transaction_details")
    utxo_df = csv_manager.load_csv_to_dataframe("03_real","transaction_utxos")
    token_df = csv_manager.load_csv_to_dataframe("03_real","token")
    transaction_df = csv_manager.load_csv_to_dataframe("03_real","transaction_details")

    # print("\nWallet Table:")
    # print(wallet_df.head(AMOUNT_DISPLAY_TABLE_DATA))

    # print("\nTransaction UXTO Table:")
    # print(utxo_df.head(AMOUNT_DISPLAY_TABLE_DATA))

    # print("\nToken Table:")
    # print(token_df.head(AMOUNT_DISPLAY_TABLE_DATA))
    # print("\n------------------------------------------")


    # Run scenarios
    config_manager = ConfigManager()
    config_list = config_manager.fetch_configs()
    
    # Initialize AML Scenarios
    aml_scenarios = AmlScenarios()
    aml_scenarios.test_scenarios(wallet_df, utxo_df, token_df, transaction_df, config_list)

if __name__ == '__main__':
    main()

