# Change Log Generator
# Creates a changelog between two same format CSV files. 
# Change Log:

import datetime

oldDoc = input("Enter original file: ")
newDoc = input("Enter new file: ")
now = datetime.datetime.now()
with open(oldDoc, 'r') as t1, open(newDoc, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
with open('ChangeLog' + now.strftime("%m-%d") + '.csv', 'w') as out1, open('RoomListRept.csv', 'r') as l1:
    line1 = l1.readline()
    out1.write(line1)
    for line in filetwo:
        if line not in fileone:
            out1.write(line)
print("Look in file ChangeLog" + now.strftime("%m-%d") + ".csv for changes.")

