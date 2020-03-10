import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
 
    csvreader = (csv.reader(csvfile, delimiter=","))
    csv_header = next(csvreader)

    sheet_row = []
    sheet_column = []
    maxandmin = []
    for row in csvreader:
        date = row[0]
        profit_loss = row[1]

        sheet_row.append(date)
        sheet_column.append(profit_loss)
        row_count = len(sheet_column)
    #print (row_count)
    with open(csvpath) as csvfile:

        csvreader = (csv.reader(csvfile, delimiter=","))
        csv_header = next(csvreader)
    
        total = sum(int(r[1]) for r in csv.reader(csvfile))
        #print ("total: $" + str(total))
         
   
    percent = sheet_column[0]
    #print (percent)
    percent1 = sheet_column[-1]
    #print (percent1)
    change = (int(percent1) - int(percent))/(int(row_count) -1)
    #print (change)
    
    i = 1

    for i in range (1,len(sheet_column)):
        maxandmin.append(int(sheet_column[i]) - int(sheet_column[i-1]))  
        max_change = max(maxandmin)
        min_change = min(maxandmin)
    #print (max_change)
    #print (min_change) 
    max_date = str(sheet_row[maxandmin.index(max(maxandmin))+1])
    min_date = str(sheet_row[maxandmin.index(min(maxandmin))+1])
    #print (max_date)
    #print (min_date)



os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("Resources", "pybanktxt.txt")

with open(output_path, 'w', newline='') as txt_file:
    txt_file.write("Financial Analysis  \n")
    txt_file.write("---------------------------------\n")
    txt_file.write(f"Total Months : {(row_count)} \n")
    txt_file.write(f"total: $ {(total)} \n")
    txt_file.write(f"Average Change: ${round(change, 2)} \n")
    txt_file.write(f"Greatest Increase in Profits: {(max_date)},(${(max_change)})\n")
    txt_file.write(f"Greatest Decrease in Profits: {(min_date)},(${(min_change)})\n")







   
  

    
    
    
    