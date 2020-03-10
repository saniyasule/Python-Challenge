import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    candidate = []
    votes = []
    name= []

    for row in csvreader:
        candidate.append(row[2])
    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]

    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name,votes)
    candidate_list = list(candidate_zip)
    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]

total_votes = len(candidate)-1
correy = candidate.count('Correy')
correy_percent=int(correy)/int(total_votes)

khan = candidate.count('Khan')
khan_percent = int(khan)/int(total_votes)

Li = candidate.count('Li')
Li_percent = int(Li)/int(total_votes)

Tooley = candidate.count("O'Tooley")
Tooley_percent = int(Tooley)/int(total_votes)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("Resources", "pypolltxt.txt")

with open(output_path, 'w', newline='') as txt_file:
    txt_file.write(f"Election Results \n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes:  {total_votes}\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Khan : {khan_percent:.3%} ({khan})\n")
    txt_file.write(f"Correy : {correy_percent:.3%} ({correy})\n")
    txt_file.write(f"Li : {Li_percent:.3%} ({Li})\n")
    txt_file.write(f"O'Tooley : {Tooley_percent:.3%} ({Tooley})\n")
    txt_file.write(f"------------------------\n")
    txt_file.write(f"Winner : {winner_name}\n")
    txt_file.write(f"--------------------------\n")


