'''
Team B2-4ac- Bayan Berri, Alessandro Cartegni
SoftDev1 pd7
HW03: StI/O: Divine your Destiny!
2017-09-14
'''
import random


def makedict(filename):
    d = dict()
    for line in open(filename):
        newline= line[line.rfind("n")]
        d[line[0:line.rfind(',')]] = line[line.rfind(',')+1:len(line)-1]#deals with the categories that include commas by searching from the end.
        #rfind returns index of last comma.
    if "Job Class" in d:
        del d["Job Class"]
    return d

#make string numbers into floats (first line of csv value is a string 
def make_float(d):
    for k in d:
        try:
            d[k]=float(d[k])
        except:
            d[k]=d[k]
    return d

#makes an array of 998 to then select a random choice
def make_arr(d):
    jobs=[]
    for k in d:
        if type(d[k])!= str and k!="Total":
            ctr= int(d[k]*10) #adds every job 10 times the percentage. 
            while ctr!=0:
                jobs.append(k)
                ctr-=1
    return jobs


'''def make_table(d):
    table = "<table border = 1>\n\t<thead><th>Occupation</th><th>percentage</th></thead>"
    
    for each in d:
        if each== "Job Class":
            table=table
        elif each== "Total":
            table= table
        else:
             table+= "<tr><td>" + each + "</td><td>" + d[each] +"</td></tr>"
             
    return table+ "</table>"
'''
#final selectio
def get_random(arr):
    return random.choice(arr)#random.choice picks a random item from the array

def getRandom(f):
    return get_random(make_arr(make_float(makedict(f))))
     
#output
#print get_random(make_arr(make_float(makedict("occupations.csv")))) #prints random occ
#d= make_float(makedict("occupations.csv"))
#print "DICTIONARY"

#print d
#tbl= make_table(d)
#print tbl
 

