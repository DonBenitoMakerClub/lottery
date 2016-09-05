#!/usr/bin/env python

import csv
import random

file_name="Fall_2016_After_School_Signs_Ups.tsv"
Lottery_entries=[]

# List of After School Activities
# Should correspond to the names of activities in the lottery list
After_School_Activities= ["Makers Club","Coding Club","Sunny Days Garden Club","Chess Club"]

# Reads the Input Spreadsheet and places each entry into a list
with open(file_name,'rb') as f:
    reader=csv.reader(f,delimiter='\t')
    data=list(reader)
    for i in range(1,len(data)):
		Lottery_entries.append((data[i]))


for activity in After_School_Activities:
    lottery_position=0
    activity_list=[]
    results=[]
    # Cycle through each lottery entry
    for entry in Lottery_entries:
        # If the entry corresponds to the particular after school activity, add it to the activity list
        if activity in entry[1]:
            # Check that the child is the correct age - if so add them to the list, else print a warning
            if activity=="Coding Club" and (entry[6] == "1" or entry[6]=="K"):
                activity_list.append((entry[5],entry[6],entry[2]))
            elif activity=="Coding Club" and not (entry[6] == "1" or entry[6]=="K"):
                print "Child: %s - Grade:%s is not eligible for %s" %(entry[5],entry[6],activity)
            if activity =="Makers Club" and (entry[6] == "1" or entry[6]=="K"):
                print "Child: %s - Grade:%s is not eligible for %s" %(entry[5],entry[6],activity)
            elif activity=="Makers Club" and not (entry[6] == "1" or entry[6]=="K"):
                activity_list.append((entry[5],entry[6],entry[2]))
            if activity in ["Chess Club"] and (entry[6] == "1" or entry[6]=="K"):
                print "Child: %s - Grade:%s is not eligible for %s" %(entry[5],entry[6],activity)
            elif activity=="Chess Club" and not (entry[6] == "1" or entry[6]=="K"):
                activity_list.append((entry[5],entry[6],entry[2]))
            if activity in ["Sunny Days Garden Club"] and entry[6]=="K":
                print "Child: %s - Grade:%s is not eligible for %s" %(entry[5],entry[6],activity)
            elif activity=="Sunny Days Garden Club" and not entry[6]=="K":
                activity_list.append((entry[5],entry[6],entry[2]))
    while len(activity_list) > 0:
        lottery_position +=1
        # Pick a random integer number from 0 to the number of people in the lottery
        selected_person=random.randint(0,len(activity_list)-1)
	    # Remove the selected_person from the pool
        spot=activity_list.pop(selected_person)
        results.append((lottery_position,spot[0],spot[1],spot[2]))
    print "Lottery Completed for %s - %s entries" %(activity,len(results))
    results_file_name="Lottery_Results_%s.csv" %activity.replace(" ","")
    with open(results_file_name,"w") as f:
        a=csv.writer(f,lineterminator='\n')
        a.writerows(results)
        f.close()
