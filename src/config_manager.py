import json
import os
import glob



class ConfigManager:
    def initialize(self):
        directory_path = './config'
        text_files = glob.glob(os.path.join(directory_path, '*.json'))
        print(text_files)
        for file_path in text_files:
            config_data = self.read_config(file_path)
            print(file_path)
            if config_data == None:
                continue
            for key in config_data:
                if key != "scenarios":
                    continue
                self.parse_config(config_data[key])
    
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
    # array with scenario dictionaries
    def parse_config(self, config):
        for scenario in config:
            print(scenario["name"])