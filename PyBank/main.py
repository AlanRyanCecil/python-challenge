# * Your task is to create a Python script that analyzes
#       the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The total net amount of "Profit/Losses" over the entire period

#   * The average change in "Profit/Losses" between
#       months over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   -----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the
#       analysis to the terminal and export a text file with the results.
############################################################################

import os
import csv

# define paths to the in and out data files
read_path = os.path.join('Resources', 'budget_data.csv')
write_path = ('financial_analysis.txt')

row_count = 0
total_profit = 0
great_inc = 0
inc_date = ''
great_dec = 0
dec_date = ''
write_data = ''

# open with block
with open(read_path, 'r') as data_in, \
        open(write_path, 'w') as data_out:
    reader = csv.reader(data_in, delimiter=',')
    writer = csv.writer(data_out, delimiter='\n')
    header = next(reader)

    for row in reader:
        date, profit = row
        profit = int(profit)
        row_count += 1
        total_profit += profit

        if profit > great_inc:
            inc_date = date
            great_inc = profit

        if profit < great_dec:
            dec_date = date
            great_dec = profit

    writer.writerow(['Financial Analysis',
                     '-' * 23,
                     'Total Months: {}'.format(row_count),
                     'Total: ${}'.format(total_profit),
                     'Greatest Increase in Profits: {} (${})'.format(
                         inc_date, great_inc),
                     'Greatest Decrease in Profits: {} (${})'.format(dec_date, great_dec)])



with open(write_path, 'r') as print_data:
    printer = csv.reader(print_data, delimiter='\n')

    for line in printer:
        print(line[0])










