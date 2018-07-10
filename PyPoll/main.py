import os
import csv

read_path = os.path.join('Resources', 'election_data.csv')
write_path = 'election_results.txt'

total_votes = 0
candidates = {}
votes_as_keys = {}
results = []
winner = ''
title = 'Election Results'
border = '-' * 25

with open(read_path, 'r') as data_in:
    reader = csv.reader(data_in, delimiter=',')
    next(reader)
    for row in reader:
        _, _, candidate = row
        total_votes += 1
        if candidate in candidates:
            candidates[candidate]['votes'] += 1
        else:
            candidates.update({candidate: {'votes': 1}})


with open(write_path, 'w') as data_out:
    writer = csv.writer(data_out, delimiter='\n')
    for candidate in candidates:
        vote_percent = candidates[candidate]['votes'] / total_votes
        vote_percent = '{:.3%}'.format(vote_percent)
        votes_as_keys.update({candidates[candidate]['votes']:
                              {'name': candidate, 'percent': vote_percent}})

    # use a sorted list of the vote counts to order the results
    votes_list = sorted(votes_as_keys)
    for vote in range(len(votes_list)):
        vote_count = votes_list.pop()
        name = votes_as_keys[vote_count]['name']
        percent = votes_as_keys[vote_count]['percent']
        results.append('{}: {} ({})'.format(name, percent, vote_count))
        if not winner:
            winner = 'Winner: {}'.format(name)

    # write data to text file
    writer.writerow([title, border, 'Total Votes: {}'
                                    .format(total_votes), border])
    writer.writerow(results)
    writer.writerow([border, winner, border])


# print text file to console
with open(write_path, 'r') as print_data:
    printer = csv.reader(print_data, delimiter='\n')
    print('\n')
    for line in printer:
        print(line[0])
    print('\n')
