# -*- coding: utf-8 -*-
"""
@author: fcperni
"""

# credited:
# https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py
# https://stackabuse.com/command-line-arguments-in-python/

import os
import glob
import pandas as pd
import getopt
import sys


def main():
    full_cmd_arguments = sys.argv

    argument_list = full_cmd_arguments[1:]

    short_options = "ho:f:"
    long_options = ["help", "output=", "folder="]

    try:
        arguments, values = getopt.getopt(argument_list, short_options,
                                          long_options)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    output_file_name = "joined.csv"
    folder = "csv"

    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            print_help()
        elif current_argument in ("-o", "--output"):
            output_file_name = current_value
        elif current_argument in ("-f", "--folder"):
            folder = current_value

    try:
        os.chdir(folder)
    except OSError as e:
        print(f'Error: {e}')
        print_help()
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    try:
        # combine all files in the list
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
        # export to csv
        combined_csv.to_csv(output_file_name, index=False,
                            encoding='utf-8-sig')
    except ValueError as e:
        print(f'Error: {e}')
        print_help()


def print_help():
    print("""This program will join all the csv files of a
folder in a single one called 'joined.csv'.

Available options:
    --help      Display this help screen.
    --folder    Sets the folder that contains the files.
    --output    Sets the name of the output file.""")


if __name__ == "__main__":
    main()
