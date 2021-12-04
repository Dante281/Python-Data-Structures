fname = input("Enter file name: ")  #Asking for the file name
if len(fname) < 1:                  #If the name is smaller than 1
    fname = "mbox-short.txt"        #We add automatically this filename

fh = open(fname)
count = 0



for line in fh:
    if not line.startswith("From"): #Excluimos las lineas que no queremos
        continue
    if line.startswith("From:"): #Excluimos las lineas que no queremos
        continue
    else :
        words = line.split()    #we split the line
        email = words[1]        # and we pick the email 
        print(email)            #printing all the emails
    count = count + 1           #adding 1 into count


print("There were", count, "lines in the file with From as the first word")
