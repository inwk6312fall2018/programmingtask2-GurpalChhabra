import string
l1=[]
l2=[]
l3=[]
myfile=open("Crime.csv")            
for lines in myfile:
    line=lines.strip(string.punctuation and string.whitespace) #removing punctuation and whitespaces
    lol=line.strip()
    list_details=lol.split(",")
    l1.append(list_details[-1])         #list of crime 
    l2.append(list_details[-2])         #list of crime ID
for j in l2:
    count=0
    for k in range (len(l2)):
        if j==l2[k]:
            count+=1
    l3.append(count)                    # list of count of crime 
print ("CRIME               CRIME-ID                 CRIME-COUNT")   #printing ALL LIST 
for i in range(len(l1)):
    print(l1[i],"                        ",l2[i],"              ", l3[i])


