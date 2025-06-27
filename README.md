# dim-ces-qe-data-testing

The CSV Exporter is a Python-based command-line tool designed to extract data from a PostgreSQL database dynamically and export it as CSV files. The tool supports flexible query construction based on input parameters, making it easy to fetch either header or detail level data with customized filters.

## Installation of the Libraries
To install the required libraries, run the following command:
```pip install psycopg2-binary python-dotenv```

## DB Properties
The database properties should feed to the `db_properties.ini` and `db_config.json` files. Please add them before running the code.

## Running the Code
Run the main script with appropriate CLI arguments:
```python main.py --env dev --schema invoice --table header --limit 100 --opco_nbr 123 --date_from 2023-01-01 --date_to 2023-01-31```
Or
Running with input files:
`data/common_inputs.txt` and `data/<table>_inputs.txt` (e.g., `data/header_inputs.txt`)
You can edit these files to set default filter values.Then,
```python main.py```

## Output
The code will save all the results under the`results` folder according to the  timestamp.
