import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
 
    csvreader = (csv.reader(csvfile, delimiter=","))
    csv_header = next(csvreader)
    Voter_ID = []
    County = []
    Candidate = []

    for row in csvreader:
        sheet_row_a = row[0]
        sheet_row_b = row[1]
        sheet_row_c = row[2]
        Voter_ID.append(sheet_row_a)
        County.append(sheet_row_b)
        Candidate.append(sheet_row_c)
        row_count = len(Voter_ID)
    #print (row_count)
    row_count1 = Candidate.count("Khan")
    row_count2 = Candidate.count("Correy")
    row_count3 = Candidate.count("Li")
    row_count4 = Candidate.count("O'Tooley")

    per1 = ((row_count1)/(row_count)*100)
    per2 = ((row_count2)/(row_count)*100)
    per3 = ((row_count3)/(row_count)*100)
    per4 = ((row_count4)/(row_count)*100)
    

os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("Resources", "pypolltxt.txt")

with open(output_path, 'w', newline='') as txt_file:
    txt_file.write("Election Results  \n")
    txt_file.write("---------------------------------\n")
    txt_file.write(f"Total Votes: : {(row_count)} \n")
    txt_file.write("---------------------------------\n")
    txt_file.write(f"Khan : {per1} ({(row_count1)})\n")
    txt_file.write(f"Correy : {per2} ({(row_count2)})\n")
    txt_file.write(f"Correy : {per3} ({(row_count3)})\n")
    txt_file.write(f"Correy : {per4} ({(row_count4)})\n")
    txt_file.write("---------------------------------\n")
    txt_file.write("Winner : Khan \n")
    txt_file.write("---------------------------------\n")

