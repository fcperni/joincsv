# joincsv
This program will join all the csv files of a folder in a single one.

Default folder is "csv" and default output file is "joined.csv".

Available options:
```
     -h --help      Display this help screen.
     -f --folder    Sets the folder that contains the files.
     -o --output    Sets the name of the output file.
```
     
Usage example: 
```
py joincsv.py -f myfiles -o joinedfile.csv
```

Based on these articles:
- https://learningactors.com/how-to-combine-multiple-csv-files-with-8-lines-of-code/
- https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py
- https://stackabuse.com/command-line-arguments-in-python/
