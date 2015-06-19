__author__ = 'Sonu'
import random
import time
def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
            # print("Merging ",alist)

def main_merge():
    input =[1000,3000,5000,10000,15000,20000,32000]
    for s in range (0,len(input),1):
      alist = random.sample(range(1,input[s]),input[s]-1)
      stime= time.time()
      mergeSort(alist)
      etime=time.time()
      print ("Unsorted Array : \t Array Size:",input[s],"\tStart Time",stime,"\tEnd Time",etime,"\tExecution Time",round(((etime-stime)*1000),2))
      alist.sort()
      stime1=time.time()
      mergeSort(alist)
      etime1=time.time()
      print ("Sorted Array : \t Array Size:",input[s],"\tStart Time",stime1,"\tEnd Time",etime1,"\tExecution Time",round(((etime1-stime1)*1000),2))
      alist.sort(reverse=True)
      stime2=time.time()
      mergeSort(alist)
      etime2=time.time()
      print ("Reverse Sorted Array : \t Array Size:",input[s],"\tStart Time",stime2,"\tEnd Time",etime2,"\tExecution Time",round(((etime2-stime2)*1000),2))

def main():
   main_merge()

if __name__ == "__main__":
    main()