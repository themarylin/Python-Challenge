import os
import csv

#declare variables
vote_count = 0.00
candidates = []
votes = []
winner = ''

#output to terminal
def terminal_output():
    print("Election Results\n---------------------------\nTotal Votes: " + str(vote_count)+ "\n---------------------------\n")
    for x in range(len(candidates)):
        print(candidates[x] + ": " + "%.2f"%(votes[x]/vote_count*100.00) + "% (" + str(votes[x]) + ")\n")
    print("------------------------------\n")
    print("Winner: " + winner)

#output to text file
def text_output(name):
    txtpath = os.path.join('Output',name)
    txt = open(txtpath,'w')
    txt.write("Election Results\n---------------------------\nTotal Votes: " + str(vote_count)+ "\n---------------------------\n")
    for x in range(0,len(candidates)):
        txt.write(candidates[x] + ": " + str(votes[x]/vote_count*100.00) + "% (" + str(votes[x]) + ")\n")
    txt.write("------------------------------\n")
    txt.write("Winner: " + winner)

#read first file
file_name = input("What is the file name?")
#read file
csvpath = os.path.join('Resources',file_name)
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        vote_count = vote_count + 1
        if (len(candidates)== 0):
            candidates.append(row[2])
            votes.append(1)
        else:
            exist = False
            for x in candidates:
                if(row[2] == x):
                    num = candidates.index(x)
                    votes[num] = votes[num] + 1
                    exist = True
            if not exist:
                candidates.append(row[2])
                votes.append(1)
    max = 0            
    for x in range(0,len(candidates)):
        if int(votes[x]) > max:
            winner = candidates[0]
    terminal_output()
    name = input("\nWhat would you like to call your txt output? (include .txt and quotations)\n")
    text_output(name)
