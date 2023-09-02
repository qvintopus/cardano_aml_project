from src.data_fetcher import DataFetcher  # Assuming data_fetcher.py is in a src directory

def main():
    data_fetcher = DataFetcher(num_sample_records=3)  # Create 3 sample records for each table
    
    # Fetch the sample transaction data
    df_transactions = data_fetcher.create_transaction_table()
    print("Transaction Table:")
    print(df_transactions)
    
    # Fetch the sample wallet data
    df_wallet = data_fetcher.create_wallet_table()
    print("\nWallet Table:")
    print(df_wallet)
    
    # Fetch the sample token data
    df_token = data_fetcher.create_token_table()
    print("\nToken Table:")
    print(df_token)

if __name__ == '__main__':
    main()
