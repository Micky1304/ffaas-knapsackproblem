#Code to change the format of the hard instances to match the "Pisinger" format
#It is assumed that the instances are stored in the folder "problemInstances"
#The converted items are stored in the folder "hardInstancesPI" (on the server "knapsacksolver/hardInstancesPI")

#Imports
import pandas as pd
import os
import fileinput

#Functions to read the profit and weight from a line of input
def read_profit(line):
    line = str(line)
    line = line[(line.find(" ")+1):]
    line = line[:line.find(" ")]
    return int(line)

def read_weight(line):
    line = str(line)
    line = line[(line.find(" ")+1):]
    line = line[(line.find(" ")+1):]
    line = line[:line.find(" ")]
    return int(line)

#Function to build the items
def build_items(items):
    #For every item
    for index in items.index:

        #Read the profit and weight
        profit = read_profit(items[0][index])
        weight = read_weight(items[0][index])

        #Write the profit and weight to new columns together with an id and x
        items.at[index, "profit"] = profit
        items.at[index, "weight"] = weight
        items.at[index, "id"] = int(index)+1
        items.at[index, "x"] = 1
    
    #Return the DataFrame containing four columns
    return pd.concat([items["id"], items["profit"], items["weight"], items["x"]], axis=1)

#Iterate over each instance (in the folder "problemInstances")
for filepath in os.listdir("probleminstances/"):
    
    #Read the time from the "time.out" file
    with open("probleminstances/"+filepath+"/time.out") as file:
        time = file.readline()

    #Some instances were not solved and contain a "-1" as error code
    if time.strip() == "-1":
        #Skip the loop iteration and ignore the instance
        continue  

    #Read the input and output files of the instance
    with open("probleminstances/"+filepath+"/test.in") as file:
        in_lines = file.readlines()
    with open("probleminstances/"+filepath+"/outp.out") as file:
        out_lines = file.readlines()
    
    #Capacity is given as the final line from the input
    capacity = in_lines[1001]

    #Max_profit is the first line of the output
    max_value = out_lines[0]

    #Read the items from the input file
    items = pd.DataFrame(in_lines[1:1001])
    items = build_items(items)

    #Convert the items to integers
    items = items.applymap(int)

    #Save the items in the folder "hardInstancesPI"
    items.to_csv("hardInstancesPI/"+str(filepath)+".csv", index=False, sep=",", header=False, index_label=None, na_rep="")
    
    #To add the capacity and max_profit read the file as lines
    f = fileinput.input("hardInstancesPI/"+str(filepath)+".csv", inplace=1)
    for xline in f:
        #Write the general information in front of the items
        if f.isfirstline():
            #Write the information
            print(  filepath
                    + "\n" + "n 1000"
                    + "\n" + "c "+ str(capacity)
                    + "z " + str(max_value) #No \n, as it is within the line
                    + "time 0.00"
                    + '\n' + xline.rstrip("\r\n"))
        else:
            #Leave the lines unchanged
            print(xline.rstrip("\r\n"))
    
    #Output to show the progress
    print(str(filepath)+" completed!")