__author__ = 'Sonu'
import random
import time
import sys

sys.setrecursionlimit(1000000)


# def quickSort (alist) :
#     recurQsort (alist,0,len(alist)-1)

def recurQsort (alist,left,right) :
    if  left < right :
        partition = partitionIt (alist,left,right)
        #print ('partition - ',partition)
        recurQsort(alist,left,partition-1)
        recurQsort(alist,partition+1,right)
    #print('quick',alist)
    return alist



def partitionIt (alist,left,right):
    #print('Alist - Partition',alist)
    x= alist[right]
    #print ('Pivot - ',x)
    i= left-1
    for j in range (left,right,1) :
        if alist[j] <= x :
            i= i+1
            alist[i],alist[j]=alist[j],alist[i]
    alist[i+1],alist[right] = alist[right],alist[i+1]
    #print ('Partition',alist)
    return i+1



def main_quick():
    #input = [30]
    input =[1000,3000,5000,10000,15000,20000,32000]
    for s in input:
        alist = random.sample(range(1,100000),s)
        stime= time.time()
        recurQsort (alist,0,len(alist)-1)
        etime=time.time()
        print ("Unsorted Array : \t Array Size:",s,"\tStart Time",stime,"\tEnd Time",etime,"\tExecution Time",round(((etime-stime)*1000),2))
        #print(alist)
        alist = random.sample(range(1,100000),s)
        alist.sort()
        stime1=time.time()
        recurQsort (alist,0,len(alist)-1)
        etime1=time.time()
        print ("Sorted Array : \t Array Size:",s,"\tStart Time",stime1,"\tEnd Time",etime1,"\tExecution Time",round(((etime1-stime1)*1000),2))
        alist.sort(reverse=True)
        stime2=time.time()
        recurQsort (alist,0,len(alist)-1)
        etime2=time.time()
        print ("Reverse Sorted Array : \t Array Size:",s,"\tStart Time",stime2,"\tEnd Time",etime2,"\tExecution Time",round(((etime2-stime2)*1000),2))

        # print(alist)

def main():
    main_quick()     #print(alist)


if __name__ == "__main__":
    main()