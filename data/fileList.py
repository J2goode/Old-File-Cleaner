
# comment out anything marked DWF (Delete.When.Finished)once this runs perfectly


def fileList(message, filename):
    """This Program asks user for a list of items to be put into a .txt file. \nWhen done inputing, it will put this list into lines on the .txt file"""

    import os
    
    optPath = os.getcwd()

    data = open(os.getcwd() + '\OPTIONS.txt')
    os.chdir(os.pardir)
    os.chdir(os.pardir)

    print(os.getcwd())

    # read text file for items already in it
    raw = data.readlines()

    for i in range(len(raw)):
        n = raw[i]
        raw[i] = n.strip("\n")

    # ask if they want to keep current list, add to it, or start fresh
    if raw == []:
        while True:
            ans = input("There are currently no protected files and/or folders.\nWould you like to protect any files? (y/n): ")
            if ans.lower() == 'y':
                break
            if ans.lower() == 'n':
                os.chdir(os.getcwd() + '\Kondo')
                data.close()
                return raw
            else:
                print("Please answer with 'y' or 'n'")
                continue
    if raw != []:
        while True:
            print('\n')
            # print out each line of raw list
            for i in range(len(raw)):
                print(raw[i])
            print('\n')
            ans = input("There are already protected files and/or folders.\nWould you like to overwrite this list? (y/n): ")
            if ans.lower() == 'y':
                break
            if ans.lower() == 'n':
                os.chdir(os.getcwd() + '\Kondo')
                print(os.getcwd())
                return raw 
            else:
                print("Please answer with 'y' or 'n'")
                continue
    # ask them to input list
    items = []
    data = open(optPath + '\OPTIONS.txt',"w")

    while True:
        entered = str(input("\n" + message + ": "))
        n = entered + '\n'

        if os.path.isfile(entered) == True:
            print("File!") #DWF
            items.append(entered)
            continue
        if os.path.isdir(entered) == True:
            print("Folder!") #DWF
            items.append(entered)
            continue
        if entered == str("") :
            break
        else:
            print("\nFile or folder not in current Directory.\nPlease enter correct file or folder name (include .pdf, .wav, etc. for files)")
            continue
            
    for i in range(len(items)):
        data.writelines(items[i] + '\n')

    os.chdir(os.getcwd() + '\Kondo')

    # figure out how to get it so this returns a list
    # not just all of the the words
    return items
    

#options = fileList("Enter Files or Folders (This is case sensitive)\nWhen you're finished, leave the line blank and press enter","OPTIONS.txt") #DWF
#options.append("Kondo")
#print(options) #DWF
