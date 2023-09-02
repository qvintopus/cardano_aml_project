# Cardano AML Project


## Description
This project aims to analyze Cardano transactions for Anti-Money Laundering (AML) purposes. It fetches transaction data, loads it into pandas DataFrames, and performs various AML checks.

## Features

- Fetch and analyze Cardano transactions for a single wallet.
- Apply AML scenarios to identify suspicious activities.
- Load custom datasets for different AML scenarios.

## Getting Started

### Prerequisites

- Python 3.11+
- Pandas library

### Installation

1. Clone this repository:
    ```
    git clone https://github.com/your-username/cardano_aml_project.git
    ```
2. setup python's virtual environment in projects directory:
    ```
    python -m venv myenv
    ```
3. Open python virtual environment:
    ```
    myenv\Scripts\activate
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

### Usage

1. Open python virtual environment - if not already
    ```
    myenv\Scripts\activate
    ```
2. Run the `main.py` script to execute the project:
    ```python
    python main.py
    ```

## Project Structure

- `data/`: Folder containing scenario-specific CSV files for testing.
- `src/`: Source code.
  - `aml_scenarios.py`: Contains different AML scenarios.
  - `table_creator.py`: Responsible for creating and populating tables.
- `main.py`: Main script to run the project.
- `requirements.txt`: Required Python packages.

## Customizing AML Scenarios

You can customize AML scenarios by editing the `aml_scenarios.py` file. Each scenario is defined as a method within the `AmlScenarios` class.

## Authors
Agnis Aldiņš

Mārtiņš Aldiņš

## License
This project is licensed under the MIT License - [ see the LICENSE.md file for details ].



