## Convert

The Convert is a console utility for converting CSV documents to parquet documents and vice versa. 
It also can output a parquet document file scheme to the console. 

## Requirements
python 3+

## Usage

# To convert from csv to parquet enter 
--csv2parquet <src-filename> <dst-filename>

> convert.py --csv2parquet C:\Users\1\Documents\test.csv C:\Users\1\Documents\test.parquet

# To convert from parquet  to scv enter 
--parquet2csv <src-filename> <dst-filename>

> convert.py --parquet2parquet C:\Users\1\Documents\test.parquet C:\Users\1\Documents\test.csv 

# To display the schema from the parquet file to the console, enter
--get-schema <filename>

> convert.py --get-schema C:\Users\1\Documents\test.parquet

# For help enter 
--help
> convert.py --help