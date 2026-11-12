# OOP Data Processing

Changing code from procedural-style code into OOP-style code.

## Project Structure
```
oop_lab/
├── README.md            # This file
├── Cities.csv           # The dataset
└── data_processing.py   # The analysis code
```

## Design Overview

### DataLoader
Connects to the Cities.csv database so the code can take data from it. `load_csv` changes the plain text into a list of dicts.

### Table
- table_name is the name of the table, and `table` stores the data.

- filter checks a condition and filters the list down, so the new table created in filter only has the rows you want.
- aggregate uses either the filtered table or `self.table` to do actions like sum, len, or getting only one part, such as only city names or only country names. Everything in the list comes from strings, so it changes temperature from string into float with try/except to be able to calculate.

Both filter and aggregate are very similar to the procedural style.

## Run locally
```
python data_processing.py
```