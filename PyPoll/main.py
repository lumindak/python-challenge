#imports
import os #this enables the code to work on any os
import csv #required to read csv files

#get the file location
data_csv = os.path.join("Resources", "election_data.csv")
#create a poiter at the top of csv file
with open(data_csv, 'r') as csvfile:

	#read as a list separated by ","
	csvreader = csv.reader(csvfile)
	
	votes_counter =0
	khan = 0
	correy = 0
	li = 0
	otooley = 0
	
	#looping the rows
	for row in csvreader:
		#print(row[0], month_counter)
		if (row[0]!= "Voter ID") : #header is skipped
			votes_counter +=1
			if (row[2] == "Khan"):
				khan+=1
			if (row[2] == "Correy"):
				correy +=1
			if(row[2] == "Li"):
				li +=1
			if(row[2] == "O'Tooley"):
				otooley +=1
	#Finding the winner
	winner ="nobody"

	if (correy>khan):
		if (otooley>li):
			if (correy>otooley):
				winner = "Correy"
			else:
				winner ="O'Tooley"
		else:
			if (li>correy):
				winner = "Li"
			else:
				winner = "Correy"
	else:
		if (otooley>li):
                        if (khan>otooley):
                                winner = "Khan"
                        else:
                                winner ="O'Tooley"
		else:
                        if (li>khan):
                                winner = "Li"
                        else:
                                winner = "Khan"

	#end of finding the winner

	#writing to the terminal	
	print("")
	print("Election Results")
	print("-------------------------")
	print("Total Votes :" , votes_counter)
	print("-------------------------")
	#{0:.3f}.format(x) formats x for 3 decimal points
	print("Khan: ",str("{0:.3f}".format(khan*100/votes_counter))+"%","("+str(khan)+")")
	print("Correy: ",str("{0:.3f}".format(correy*100/votes_counter))+"%","("+str(correy)+")")
	print("Li: ",str("{0:.3f}".format(li*100/votes_counter))+"%","("+str(li)+")")
	print("O'Tooley: ",str("{0:.3f}".format(otooley*100/votes_counter))+"%","("+str(otooley)+")")
	print("Winner: ",winner)
	print("")


	#location of the output file
	output_path = os.path.join("output", "results.csv")
	#open csv file in write mode
	with open(output_path, 'w') as csvfile:

		#values are separated by ":"
		csvwriter = csv.writer(csvfile,delimiter=':')

		#writing row by row
		csvwriter.writerow(['Election Results'])
		csvwriter.writerow(['-------------------------'])
		csvwriter.writerow(['Total Votes', votes_counter])
		csvwriter.writerow(['-------------------------'])

		temp = "Khan : "+str("{0:.3f}".format(khan*100/votes_counter))+"% " +  "(" + str(khan) + ")"
		#print(temp)
		#csvwriter.writerow({temp})
		csvwriter.writerow(["Khan "] + [str("{0:.3f}".format(khan*100/votes_counter)) +  "%" + " (" + str(khan) + ")"])
		csvwriter.writerow(["Correy "] + [str("{0:.3f}".format(correy*100/votes_counter)) +  "%" + " (" + str(correy) + ")"])
		csvwriter.writerow(["Li "] + [str("{0:.3f}".format(li*100/votes_counter)) +  "%" + " (" + str(li) + ")"])
		csvwriter.writerow(["O'Tooley "] + [str("{0:.3f}".format(otooley*100/votes_counter)) +  "%" + " (" + str(otooley) + ")"])
		csvwriter.writerow(["Winner "] + [winner])




