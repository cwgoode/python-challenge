import os 
import csv

budget1 = os.path.join("raw_data", "budget_data_1.csv")
budget2 = os.path.join("raw_data", "budget_data_2.csv")

with open(budget1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    count_rows = 0
    revenue = 0
    greatest_change = 0
    prev_row_revenue = 0
    biggest_up = 0
    biggest_down = 0
    biggest_up_date = ''
    biggest_down_date = ''
    
    # Iterate through each row
    for row in csvreader:
        
        # Convert row to float and compare to grams of fiber
        if (row[1]) != 'Revenue':
            count_rows = count_rows + 1
            revenue = revenue + int(row[1])
            recent_change = (int(row[1]) - prev_row_revenue)
            if recent_change < biggest_down or recent_change > biggest_up:
                greatest_change = recent_change
                if recent_change>0:
                    biggest_up = recent_change
                    biggest_up_date = str(row[0])
                if recent_change<0:
                    biggest_down = recent_change
                    biggest_down_date = str(row[0])
            prev_row_revenue = int(row[1])
            prev_row_date = str(row[0])
    print("Total number of months: " + str(count_rows))
    print("Total Revenue: $" + str(float(revenue)))
    print("Average change in revenue: $" + str(float(revenue/count_rows)))
    print("Highest Revenue increase was $" + str(float(biggest_up)) + " on " + biggest_up_date)
    print("Greatest Change in Revenue was $" + str(float(biggest_down)) + " on " + biggest_down_date)
