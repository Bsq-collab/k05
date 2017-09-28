'''
Team B2-4ac- Bayan Berri, Alessandro Cartegni
SoftDev1 pd7
HW03: StI/O: Divine your Destiny!
2017-09-14
'''
import random


def makedict(filename):
    """
    makes a dictionary from csv file param 
arg: 
    string filename csv file 
ret:
    dictionary d keys: jobs values: percents
    """
    d = dict()
    for line in open(filename):
        newline= line[line.rfind("n")]
        d[line[0:line.rfind(',')]] = line[line.rfind(',')+1:len(line)-1]#deals with the categories that include commas by searching from the end.
        #rfind returns index of last comma.
    if "Job Class" in d:
        del d["Job Class"]
    return d


def make_float(d):
    """
    makes string numbers into floats (first line of csv value is a string)
    
arg: 
    dictionary d whose values are to be typecasted into floats
ret:
    dictionary with values changed into floats
"""
    for k in d:
        try:
            d[k]=float(d[k])
        except:
            d[k]=d[k]
    return d


def make_arr(d):
    """
    makes an array of 998 based on dictionary values to then select a random choice
for each key in the dictionary it adds it to an array as many times as ten times 
    the value. If the key is x and the value is 6.1 then x would be added to the array 61 times. 
arg:
    dictionary d of keys type string and values type float
ret:
    array of compiled jobs based on percentages
"""
    jobs=[]
    for k in d:
        if type(d[k])!= str and k!="Total":
            ctr= int(d[k]*10) #adds every job 10 times the percentage. 
            while ctr!=0:
                jobs.append(k)
                ctr-=1
    return jobs

#final selectio
def get_random(arr):
    """
    Uses an array to randomly choose a job using python builtin function random.choice(arr)
arg:
    array arr compilation of jobs of type string from make_arr
ret:
    string from array parameter which will be the name of the job
"""
    return random.choice(arr)#random.choice picks a random item from the array


def getRandom(f):
    """
    wrapper function to make executing it easier
arg:
    string f will be the file name used in makedict
ret:
    string randomly generated from choosing a job from the array randomly
    """
    return get_random(make_arr(make_float(makedict(f))))
