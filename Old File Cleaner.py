import os
import shutil
import datetime
from data.fileList import fileList
from data.olderThan import olderThan


# List of every file and directory in Kondo folder (to protect from cleanup)
SAFETY = ['data', 'Does Not Spark Joy']

## MAIN PROGRAM ##
while True:
    start = input("PRESS ENTER TO BEGIN ")
    if start.lower() == 'j2goode':
        break
    
    # get to directory where OPTIONS is
    n = os.getcwd() + "\data"
    os.chdir(n)

    # read the options
    options = fileList("Enter Files or Folders (This is case sensitive)\nWhen you're finished, leave line blank and press enter","OPTIONS.txt")
    

    oldDate = input("What date is the cutoff for an 'old file' to you?\n(Make sure to enter in mm/dd/yyyy format): ")
    print("Options Saved!")
    break

# check if these options are correct one last time
while True:
    if 'options' in globals():
        raw = options
    else:
        data = open(os.getcwd() + '\data\OPTIONS.txt')
        raw = data.readlines()
        for i in range(len(raw)):
            n = raw[i]
            raw[i] = n.strip("\n")
    
    print("\nProtected Files:")
    for i in range(len(raw)):
        print(raw[i])
    if 'oldDate' in globals():
        print("\nCutoff date: " + oldDate + "\n")
    else:
        oldDate = input("\nCutoff date(mm/dd/yyyy): ")

    correct = input("Are these options correct (y or n)? ")

    # if they aren't, then ask them to reenter the info
    if correct == 'y':
        # first, sneak Kondo into protected files
        for i in SAFETY:
            raw.append(i)
        break
    if correct == 'n':
        print("Please reenter information.")
        time.sleep(1.5)

        os.chdir(os.getcwd() + '\data')
        options = fileList("Enter Files or Folders (This is case sensitive)\nWhen you're finished, leave line blank and press enter","OPTIONS.txt")
        print("Options Saved!")

        time.sleep(1)

        oldDate = input("What date is the cutoff for an 'old file' to you?\n(Make sure to enter in mm/dd/yyyy format): ")

        print("Options Saved!")

        time.sleep(1)
        continue
    else:
        print("Please answer with a 'y' or a 'n'.\n")

    

# keeping the Does Not Spark Joy folder tabbed
DNSJ = os.getcwd() + '\Does Not Spark Joy'

# getting names of all protected files/ folders and stripping the "\n" from them
if 'options' in globals():
    raw = options
else:
    data = open(os.getcwd() + '\data\OPTIONS.txt')
    raw = data.readlines()
    for i in range(len(raw)):
        n = raw[i]
        raw[i] = n.strip("\n")
    for i in SAFETY:
        raw.append(i)

# getting the date that items need to be older than
if 'oldDate' in globals():
    date = oldDate

# go back to starting folder, remember the directory as OG
os.chdir(os.pardir)
OG = os.getcwd()


##---------------START OF CLEANING LOOP---------------##
z = 0
completed = []
paths = [OG]
pBase = []

while True:
    z += 1
    
    for i in paths:
        os.chdir(i)
        print(os.getcwd())
        fName = []
        folders = []

        # go through everything in current directory, split into fName and folders
        for entry in os.scandir(os.getcwd()):
            if entry.is_file():
                file = str(entry.name)
                fName.append(file)
            if entry.is_dir():
                fold = str(entry.name)
                folders.append(fold)


        # check for protected directories, remove from list
        for j in folders:
            if j in raw or pBase or completed:
                folders.remove(j)

        print(folders) #DWF
        
        # add folders to path functions
        for k in folders:
            if os.getcwd() + "\\" + k in paths:
                break
            else:
                paths.append(os.getcwd() + "\\" + k)
                pBase.append(k)

        # remove already completed person
        for i in pBase:
            if i in completed:
                pBase.remove(i)

        print('Paths to Clean:')#DWF
        print(pBase) #DWF

        
        # check for unprotected files, move old ones to DNSJ
        for l in range(len(fName)):
            if fName[l] not in raw:
                path = os.getcwd() + "\\" + fName[l]
                nTime = os.path.getmtime(path)
                modTime = time.strftime('%m/%d/%Y', time.localtime(nTime))
                print(modTime) #DWF

                print(olderThan(modTime, date)) # DWF
                if olderThan(modTime, date) == True:
                    shutil.move(path, DNSJ)
        
        # record already done directory
        print('COMPLETED')
        if os.path.basename(os.getcwd()) not in set(completed):
            completed.append(os.path.basename(os.getcwd()))
        print(completed)
        
    if pBase == []:
        print("FINISHED CLEANING") #DWF
        break
    if z >= 10:
        print("Ran too many times.") #DWF
        break
    
    

