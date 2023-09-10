from blockfrost import BlockFrostApi

class BlockfrostAPIWrapper:
    def __init__(self, project_id, base_url):
        self.api = BlockFrostApi(project_id=project_id, base_url=base_url)

    def get_address(self, address):
        return self.api.address(address=address)

    def get_assets_policy(self, _id):
        # return self.api.assets_policy(policy_id=_id)
        return self.api.asset(asset=_id)

    def get_address_transactions(self, address, from_block=None):
        return self.api.address_transactions(address=address, from_block=from_block)

    def get_transactions(self, hash):
        return self.api.transaction(hash=hash)
    
    def transform_address_transactions(self, address, address_transactions, csv_manager):
        print("initiating transform_address_transactions...")
        transformed_data = []
        transactions = []
        tokens_raw = []
        tokens = []

        for tx in address_transactions:
            tx_hash = tx.tx_hash
            tx_index = tx.tx_index
            block_height = tx.block_height
            block_time = tx.block_time

            # Fetch transaction details to get unit and quantity
            tx_details = self.get_transactions(tx_hash)
            
            transactions.append(tx_details)
            output_amounts = tx_details.output_amount  # Assuming this is also a Namespace object

            trnx_json = self.api.transaction_utxos(hash=tx_hash)
            csv_manager.add_transaction_UTXOs(trnx_json)

            for amount in output_amounts:
                unit = amount.unit  # Assuming this is also a Namespace object
                tokens_raw.append(amount.unit)
                quantity = amount.quantity  # Assuming this is also a Namespace object
                transformed_data.append([address, tx_hash, tx_index, block_height, block_time, unit, quantity])

        tokens_unique = list(set(tokens_raw))
        # tokens_unique = tokens_unique[:20] # DEBUG limiter
        for token in tokens_unique:
            print("fetching token:", token)
            if token == "lovelace":
                print("skipping lovelace")
                continue
            token_detailed = self.get_assets_policy(token)
            tokens.append(token_detailed)

        # transactions = [getattr(transactions, attr, '') for attr in ["tx_hash", "block", "block_height", "block_time", "slot", "fees", "deposit", "size", "valid_contract"]]

        return transformed_data, transactions, tokens
    
    
