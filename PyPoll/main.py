import os 
import csv
import operator

data1 = os.path.join("raw_data", "election_data_1.csv")
data2 = os.path.join("raw_data", "election_data_2.csv")

with open(data1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    count_rows = 0 
    candidates_list = []
    candidates_percentage = []
    vote_count = {}
    count = 0
    for row in csvreader:
            if (row[1]) != 'County':
                count_rows = count_rows + 1
                if str(row[2]) not in vote_count:    
                    candidates_list.append(str(row[2]))
                    vote_count[row[2]] = 1 
                elif str(row[2]) in vote_count:
                    vote_count[row[2]] = vote_count[row[2]] + 1
    for item in vote_count.items():
        candidates_percentage.append(int((item[1])*100/count_rows))
    print("Total Num of votes: " + str(count_rows))
    print("List of candidates is as follows:")
    for item in candidates_list:
        print(" "+str(item) +" with " + str(vote_count[item])+ " votes (that's " + str(candidates_percentage[count]) + "%)" )
        count = count +1 
    print("------------------")
    greatest = max(vote_count.items(), key= operator.itemgetter(1))[0]
    print("The winner of the election is " + str(greatest))

