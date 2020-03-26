#imports
import os #this enables the code to work on any os
import csv #required to read csv files

#get the file location
data_csv = os.path.join("Resources", "budget_data.csv")
#create a poiter at the top of csv file
with open(data_csv, 'r') as csvfile:

	#read as a list separated by ","
	csvreader = csv.reader(csvfile, delimiter=',')
	
	month_counter =0
	profit_losses = 0.0
	greatest_increase = 0.0
	greatest_decrease = 0.0
	total_change = 0.0
	temp = 0.0
	temp1=0.0
	
	#looping the rows
	for row in csvreader:
		#print(row[0], month_counter)
		if (row[0]!= "Date") :
			month_counter +=1
			
			profit_losses = profit_losses + float(row[1])
			if (month_counter !=1) :
				#print(month_counter,row[0], temp, float(row[1])-temp)
				total_change = total_change +float(row[1])-temp
				if ((float(row[1])-temp) > greatest_increase):
					greatest_increase = float(row[1]) - temp
				if ((float(row[1])-temp) < greatest_decrease):
                                        greatest_decrease = float(row[1]) - temp

			temp=float(row[1])
	print("Total months :" ,  month_counter)
	print("Total profit/losses:",profit_losses)
	print("Average of changes:", total_change/(month_counter-1))
	print("Greatest increase of profits:",greatest_increase)
	print("Greatest decrease of profits:",greatest_decrease)

	#location of the output file
	output_path = os.path.join("output", "output.csv")
	#open csv file in write mode
	with open(output_path, 'w') as csvfile:

		#values are separated by ":"
		csvwriter = csv.writer(csvfile, delimiter=':')

		#writing row by row
		csvwriter.writerow(['Total Months',month_counter])
		csvwriter.writerow(['Total profit/losses',profit_losses])
		csvwriter.writerow(['Average of Changes',total_change/(month_counter-1)])
		csvwriter.writerow(['Greatest increasse of profits',greatest_increase])
		csvwriter.writerow(['Greatest decrease of profits',greatest_decrease])





