import os 
import csv

#read csv
def read_csv(file_name):
    #reset variables
    global total_mth
    global total_rev
    global avg_rev
    global init_rev
    global change
    global max_increase
    global max_decrease
    global date_increase
    global date_decrease
    total_mth = 0
    total_rev = 0
    avg_rev = 0
    init_rev = 0
    change = 0
    max_increase = 0
    max_decrease = 0
    date_increase = ''
    date_decrease = ''

    #create file path
    csvpath = os.path.join("Resources", file_name)

    #open csv file and read
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvreader)
        for row in csvreader:
            total_mth = total_mth + 1
            total_rev = total_rev + int(row[1])
            calc_increase(init_rev, int(row[1]), row[0])
        avg_rev = total_rev/total_mth

#calculates and determines max and min change in revenue            
def calc_increase(init_rev, revenue, date):
    global change
    global max_increase
    global max_decrease
    global date_increase
    global date_decrease
    change = revenue - init_rev
    if (change > max_increase):
        max_increase = change
        init_rev = revenue
        date_increase = date
    elif(change < max_decrease):
        max_decrease = change
        init_rev = revenue
        date_decrease = date

#terminal output
def terminalOutput():
    global total_mth
    global total_rev
    global avg_rev
    global max_increase
    global max_decrease
    global date_increase 
    global date_decrease 
    print("Financial Analysis\n --------------------")
    print("Total Months: " + str(total_mth))
    print("Total Revenue: " + str(total_rev))
    print("Average Revenue Change: " + str(avg_rev))
    print("Greatest Increase in Revenue: " + date_increase + " | " + str(max_increase))
    print("Greatest Decrease in Revenue: " + date_decrease +  " | " +str(max_decrease))

#txt output
def txtOutput(file_name):
    global total_mth
    global total_rev
    global avg_rev
    global max_increase
    global max_decrease
    global date_increase 
    global date_decrease 
    
    file_name = os.path.join("Output", file_name)
    txt = open(file_name,'w')
    txt.write("Financial Analysis\n --------------------\n")
    txt.write("Total Months: " + str(total_mth) + "\n")
    txt.write("Total Revenue: " + str(total_rev) + "\n")
    txt.write("Average Revenue Change: " + str(avg_rev) + "\n")
    txt.write("Greatest Increase in Revenue: (" + date_increase + ") " +  " | " +str(max_increase) + "\n")
    txt.write("Greatest Decrease in Revenue: (" + date_decrease + ") " +  " | " +str(max_decrease) + "\n\n")
    txt.close()

confirm = "y"
while confirm == "y":
    
    #read file
    file_name = input("\nWhat is the name of your file? \n Make sure to include your file name in quotations!\n")
    read_csv(file_name)
    
    #print to terminal
    terminalOutput()

    #create txt file
    name = input("\nWhat would you name your output file? (Include .txt and quotations)\n")
    txtOutput(name)

    confirm = input("\nWould you like to continue? ")