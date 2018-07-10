import os
import csv

# define paths to the in and out data files
read_path = os.path.join('Resources', 'budget_data.csv')
write_path = ('financial_analysis.txt')

# declare variables
row_count = 0
total_profit = 0
previous_profit = 0
change = 0
changes = []
ave_change = 0
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

        if previous_profit:
            change = profit - previous_profit
            changes.append(change)

        previous_profit = profit

        if change > great_inc:
            inc_date = date
            great_inc = change

        if change < great_dec:
            dec_date = date
            great_dec = change

    ave_change = round(sum(changes) / len(changes), 2)

    writer.writerow(['Financial Analysis',
                     '-' * 23,
                     'Total Months: {}'.format(row_count),
                     'Total: ${}'.format(total_profit),
                     'Average Change: ${}'.format(ave_change),
                     'Greatest Increase in Profits: {} (${})'.format(
                         inc_date, great_inc),
                     'Greatest Decrease in Profits: {} (${})'.format(
                         dec_date, great_dec)])


with open(write_path, 'r') as print_data:
    printer = csv.reader(print_data, delimiter='\n')
    print('\n')
    for line in printer:
        print(line[0])
