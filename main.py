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
    df_wallet = csv_manager.load_csv_to_dataframe("03_real","wallet_address")
    # df_transaction = csv_manager.load_csv_to_dataframe("03_real","transaction_details")
    df_transaction_utxo = csv_manager.load_csv_to_dataframe("03_real","transaction_utxos")
    df_token = csv_manager.load_csv_to_dataframe("03_real","token")

    print("\nToken Table:")
    print(df_token.head(AMOUNT_DISPLAY_TABLE_DATA))

    print("\nWallet Table:")
    print(df_wallet.head(AMOUNT_DISPLAY_TABLE_DATA))

    print("Transaction UXTO Table:")
    print(df_transaction_utxo.head(AMOUNT_DISPLAY_TABLE_DATA))
    

    # Initialize AML Scenarios
    aml_scenarios = AmlScenarios()

    # Run scenarios
    config_manager = ConfigManager()
    config_list = config_manager.fetch_configs()
    aml_scenarios.test_wallet(df_transaction_utxo, config_list)

if __name__ == '__main__':
    main()

