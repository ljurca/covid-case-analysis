# Lisa Jurca, CS110
import csv
import CovidSFPlot as plt

# Part 2a
# Open each relevant file in read mode
file_2020 = open('us-counties-2020.csv', 'r')
file_2021 = open('us-counties-2021.csv', 'r')
file_2022 = open('us-counties-2022.csv', 'r')

# Convert each file into a list
cov_2020 = list(csv.reader(file_2020, delimiter = ','))
cov_2021 = list(csv.reader(file_2021, delimiter = ','))
cov_2022 = list(csv.reader(file_2022, delimiter = ','))

# Create constants
FILE_PATH_INPUT = cov_2020 + cov_2021 + cov_2022
FILE_PATH_OUTPUT = 'covid-SF.csv'
WINDOW = 7

# Define main function
def main():
	dailyList = fReadInputFile(FILE_PATH_INPUT)
	fWriteOutputFile(dailyList)
	fileList = fReadOutputFile(FILE_PATH_OUTPUT)
	movingAverage = fCalcMovAvg(fileList)
	fWriteCovidSFFIle(FILE_PATH_OUTPUT, movingAverage)
	
	plt.fPlotSFCovid(FILE_PATH_OUTPUT)

# Define fReadInputFile
def fReadInputFile(pFileName):

	# Initialize variables
	total = 0
	previous = None
	daily_data = []
	daily_list = []
	daily_cases = 0

	# Loop over cov_2020 file
	for x in range(0, len(cov_2020)):
		# If statement to track only SF case numbers
		if 'San Francisco' in cov_2020[x]:

			# Assign the first case found into 'previous'
			if previous == None:
				previous = int((cov_2020[x][4]))

			# Create an elif for the rest of the cases
			elif previous != None:
				# Convert the total cases for x day to an int
				total = int((cov_2020[x][4]))
				# Find daily increase of cases by subtracting previous value from x day's total value
				daily_cases = total - previous 
				# Set previous equal to total to signify the previous day
				previous = total 

				# Test irregularities 
				if daily_cases > 2000:
					daily_cases = str(2000)

				# Put daily data together: the date and the daily cases
				daily_data = [cov_2020[x][0], str(daily_cases)]
				# Append the daily data into a list
				daily_list.append(daily_data)

	# Loop over cov_2021 file
	for x in range(0, len(cov_2021)):
		# If statement to track only SF case numbers
			if 'San Francisco' in cov_2021[x]:

				# Assign the first case found into 'previous'
				if previous == None:
					previous = int((cov_2021[x][4]))

				# Create an elif for the rest of the cases
				elif previous != None:
					# Convert the total cases for x day to an int
					total = int((cov_2021[x][4]))
					# Find daily increase of cases by subtracting previous value from x day's total value
					daily_cases = total - previous
					# Set previous equal to total to signify the previous day
					previous = total
				
				# Test irregularties 
					if daily_cases > 2000:
						daily_cases = str(2000)

				# Put daily data together: the date and the daily cases
					daily_data = [cov_2021[x][0], str(daily_cases)]
				# Append the daily data into a list
					daily_list.append(daily_data)

	# Loop over cov_2022 file
	for x in range(0, len(cov_2022)):
		# If statement to track only SF case numbers 
			if 'San Francisco' in cov_2022[x]:

				# Assign the first case found into 'previous'
				if previous == None:
					previous = int((cov_2022[x][4]))

				# Create an elif for the rest of the cases
				elif previous != None:
					# Convert the total cases for x day to an int
					total = int((cov_2022[x][4]))
					# Find daily increase of cases by subtracting previous value from x day's total value
					daily_cases = total - previous
					# Set previous equal to total to signify the previous day
					previous = total
					
					# Test irregularities 
					if daily_cases > 2000:
						daily_cases = str(2000)

					# Put daily data together: the date and the daily cases
					daily_data = [cov_2022[x][0], str(daily_cases)]
					# Append the daily data into a list
					daily_list.append(daily_data)

	# Return daily_list
	return daily_list

# Define fWriteOutputFile
def fWriteOutputFile(pList):
	# Open FILE_PATH_OUTPUT in append mode
	dataFile = open(FILE_PATH_OUTPUT, 'a')
	# Loop through the list and write it into the new file
	for x in range(0, len(pList)):
		string = pList[x][0] + ',' + pList[x][1] + '\n'
		dataFile.write(string)
	# Close file
	dataFile.close()

# Define fReadOutputFile
def fReadOutputFile(pFile):
	# Initialize file_list
	file_list = []
	# Open FILE_PATH_OUTPUT in read mode
	dataFile = open(FILE_PATH_OUTPUT, 'r')
	# Loop through each line in the file
	for lineValue in dataFile:
		temp = lineValue.split(',')
		temp = temp[1].split('\n')
		# Append the values into a list
		file_list.append(temp[0])

	# Return file_list
	return file_list

# Define fCalcMovAvg
def fCalcMovAvg(pList):
	# Initialize movAvg
	movAvg = []
	# Loop through first 6 values
	for x in range(0,6):
		movAvg.append(0)
	for i in range (7, len(pList)):
		# Sum up previous 6 values along with the current value, and then divide it by WINDOW
		sum_pList = (int(pList[i - 6]) + int(pList[i - 5]) + int(pList[i - 4]) + int(pList[i - 3]) + int(pList[i - 2]) + int(pList[i - 1])) + int(pList[i])
		ans = sum_pList/WINDOW
		# Add values to list
		movAvg.append(ans)

	# Return movAvg
	return movAvg

# Define fWriteCovidSFFile
def fWriteCovidSFFIle(pFile, pListMovAvg):
	# Open file in read mode
	dataFile = open(pFile, 'r')
	count = 0 
	# intialize list
	newList = []
	# Make for loop to pick up data
	for rows in dataFile:
		new_row = rows.split()
		new_row = new_row[0] + ',' + str(pListMovAvg[count]) + '\n'
		newList.append(new_row)
		if (count < len(pListMovAvg)-1):
			count = count + 1

	# Write information in document
	dataFile = open(pFile, 'w')
	for i in range(0, len(newList)):
		dataFile.write(newList[i])

# Call main function
main()
