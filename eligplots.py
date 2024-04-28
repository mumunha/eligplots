import os
import csv
from datetime import datetime

yourpath = 'C:\\Users\MSF-Server\.chia\mainnet\log'

general = []
total_num = 0

#linetext = ""
#datetime, plots_eligible, proofs, time, total_plots

print (yourpath)
for root, dirs, files in os.walk(yourpath, topdown=False):
    file_count = 0
    procura = "plots were eligible for farming" 
    for name in files:

        #temp_datetime = datetime.now()
            
        
        #print(os.path.join(root, name))
        print(name)
        # Using readlines()
        file1 = open(os.path.join(root, name), 'r')
        Lines = file1.readlines()
 
        # Strips the newline character
        for line in Lines:
            linetext = line.strip()
            if procura in linetext:
                #Data timestamp
                temp_datetime = datetime.strptime(linetext[:19], '%Y-%m-%dT%H:%M:%S')
                data = int(datetime.timestamp(temp_datetime))
                #print(data)
                
                #Data string
                data2 = temp_datetime
                #print(data2)
                
                #eligible plots
                seek_string_left = "INFO"
                seek_string_right = "plots were eligible"
                temp_left = (linetext.find(seek_string_left)+len(seek_string_left)+1)
                temp_right = (linetext.find(seek_string_right))
                plots_eligible = linetext[temp_left:temp_right]
                #print(plots_eligible)

                #proofs found
                seek_string_left = "Found"
                seek_string_right = "proofs"
                temp_left = (linetext.find(seek_string_left)+len(seek_string_left)+1)
                temp_right = (linetext.find(seek_string_right))
                proofs_found = linetext[temp_left:temp_right]
                #print(proofs_found)

                #time
                seek_string_left = "Time:"
                seek_string_right = "s. Total"
                temp_left = (linetext.find(seek_string_left)+len(seek_string_left)+1)
                temp_right = (linetext.find(seek_string_right))
                time_wait = linetext[temp_left:temp_right]
                #print(temp_left)
                #print(temp_right)
                
                #print(time_wait)

                #Total plots
                seek_string_left = "s. Total"
                seek_string_right = "plots"
                temp_left = (linetext.find(seek_string_left)+len(seek_string_left)+1)
                temp_right = (len(linetext)-5)
                total_plots = linetext[temp_left:temp_right]
                #print(total_plots)

                general = general + [[name, data, data2, plots_eligible, proofs_found, time_wait, total_plots]]
                total_num = total_num + 1


sorted_general = sorted(general , key=lambda x: x[1] , reverse=True)


fields = [ 'FileName', 'DateTimestamp', 'Date', 'EligiblePlots', 'ProofsFound', 'TimeWait', 'TotalPlots' ]

print (total_num)

with open('eligible_plots.csv', 'w', newline='') as f:
      
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(sorted_general)