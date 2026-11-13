# OOP Data Processing

## Lab Overview
Changing code from procedural-style code into an OOP-style code. There is 1 more different table which is countries with different variables.

## Project Structure
```
oop_lab/
├── README.md            # This file
├── Cities.csv           # The dataset
├── Countries.csv        # Countries has population, EU or not and coastline or not
└── data_processing.py   # The analysis code
```

## Design Overview

### DataLoader
Connect to a database of Cities.csv to let codes in here take from it, and load_csv changes those plain text into a list of dict.

### DB
database - stores table 1 and table 2 that was inserted from the insert function, and search is for searching a table/specific table name in the database and calling it out.

### Table
table_name - is for the specific name of the table, and table is for storing the rows as a list of dict.

filter - is for checking a condition and filtering it down, so that the new list created in the filter function has only the rows you want.

aggregate - uses either the table from filter or self.table to make actions in there, such as sum, len, or getting only a specific part such as only city name or only country name. There is also calculating, but in the list it all came from strings, so we need to change temperature from string into float to be able to calculate, by using try except.

join - is for creating a new list which consists of both cities and countries, which gathers city/country with the same name in the same dict but extends more variables.

Both filter and aggregate are very similar to procedural style.

## How to Test and Run
```
python data_processing.py
```
Running the file runs the test code at the bottom.