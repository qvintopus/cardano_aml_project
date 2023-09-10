import json
import os
import glob



class ConfigManager:
    ## Currently returns a list of scenarios, but can be expanded to extra data
    def fetch_configs(self):
        directory_path = './config'
        text_files = glob.glob(os.path.join(directory_path, '*.json'))
        
        config_list = []
        for file_path in text_files:
            config_data = self.read_config(file_path)
            if config_data == None:
                continue
            for key in config_data:
                if key == "scenarios": # Array of scenario configs
                    config_list.extend(config_data[key]) # Concatinate lists together
        return config_list
    
    def read_config(self, path):
        config_data = None
        try:
            with open(path, 'r') as file:
                config_data = json.load(file)
                return config_data
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
        return config_data
    
    # list with scenario dictionaries
    def parse_config_list(self, config_list):
        for scenario in config_list:
            print(scenario["name"])
