__author__ = 'Sonu'
import random
import time

# def quickSort (alist) :
#     recurQsort (alist,0,len(alist)-1)

def recurQsort (alist,left,right) :
    if  left+15 <= right :

        partition = partitionIt (alist,left,right)
        recurQsort(alist,left,partition-1)
        recurQsort(alist,partition+1,right)

    else :
        insertionSort (alist,left,right)

def median3 (alist,left,right) :
    middle = (left + right)//2
    if (alist[left] > alist[middle]) :
        swap (alist,left,middle)
    if (alist[left] > alist[right]) :
        swap (alist,left,right)
    if (alist[middle] > alist[right]) :
        swap (alist,middle,right)
    swap (alist,middle,right-1)
    return right-1

def swap (alist,a,b) :
    alist[a],alist[b]=alist[b],alist[a]

def partitionIt (alist,left,right):
    x= alist[median3 (alist,left,right)]
    i= left-1
    for j in range (left,right-1,1) :
        if alist[j] <= x :
            i= i+1
            swap(alist,i,j)
    swap(alist,i+1,right-1)
    return i+1

def insertionSort(alist,p,r) :
    for j in range(p+1, r+1,1):
        key = alist[j]
        i = j
        while i > 0 and alist[i - 1] > key:
            alist[i] = alist[i - 1]
            i = i - 1
        alist[i] = key
    return alist

def main_quick():
    input =[1000,3000,5000,10000,15000,20000,32000]
    for s in input:
      alist = random.sample(range(1,100000),s)
      stime= time.time()
      recurQsort (alist,0,len(alist)-1)
      etime=time.time()
      print("Unsorted Array :")
      print ("Array Size:",s,"\tStart Time",stime,"\tEnd Time",etime,"\tExecution Time",(etime-stime)*1000)
      alist = random.sample(range(1,100000),s)
      alist.sort()
      stime1=time.time()
      recurQsort (alist,0,len(alist)-1)
      etime1=time.time()
      print ("Sorted Array :")
      print ("Array Size:",s,"\tStart Time",stime1,"\tEnd Time",etime1,"\tExecution Time",(etime1-stime1)*1000)
      alist.sort(reverse=True)
      stime2=time.time()
      recurQsort (alist,0,len(alist)-1)
      etime2=time.time()
      print ("Reverse Sorted Array : \t Array Size:",s,"\tStart Time",stime2,"\tEnd Time",etime2,"\tExecution Time",round(((etime2-stime2)*1000),2))

def main():
   main_quick()     #print(alist)


if __name__ == "__main__":
            main()