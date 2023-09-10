from src.csv_manager import CardanoCSVManager  # Replace with your actual import
from src.api_wrapper import BlockfrostAPIWrapper  # Replace with your actual import
from blockfrost import ApiUrls

API_PROJECT_ID = "missing"
AML_SCENARIO_NAME = "03_real" # why do I have to have it? TODO: rethink usecase

def fetch_address_data(api_wrapper, address_list, csv_manager):
    for address in address_list:
         # Fetching address details
        address_details = api_wrapper.get_address(address)
        csv_manager.add_wallet(address_details)

        # Fetching transactions for each address
        address_transactions = api_wrapper.get_address_transactions(address)
        # address_transactions = address_transactions[:10] # DEBUG

        # Transforming the transactions data
        transformed_data, trnxs, tokens = api_wrapper.transform_address_transactions(address, address_transactions, csv_manager)
        
        # Adding transformed data to CSV manager
        for row in transformed_data:
            csv_manager.add_transaction_D(row)

        for row in trnxs:
            csv_manager.add_transaction_details_D(row)

        for row in tokens:
            csv_manager.add_token_D(row)

        # api_wrapper.get_transactions_utxo(trnxs, csv_manager)
        

def main():
    global API_PROJECT_ID, AML_SCENARIO_NAME
    if API_PROJECT_ID == "missing":
        print("ERROR: missing project ID. Please add it from you BlackFrost API access.")
        exit()

    print("initiating data import...")
    csv_manager = CardanoCSVManager()
    api_wrapper = BlockfrostAPIWrapper(project_id=API_PROJECT_ID,base_url=ApiUrls.mainnet.value)

    # List of addresses to fetch data for
    address_list = [
        'addr1qx7tzh4qen0p50ntefz8yujwgqt7zulef6t6vrf7dq4xa82j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pqrkj6fh',
        # Add more addresses here
    ]

    # Fetch and store all required data
    fetch_address_data(api_wrapper, address_list, csv_manager)

    # Save all data to CSV files
    csv_manager.save_all(AML_SCENARIO_NAME)

if __name__ == '__main__':
    main()


