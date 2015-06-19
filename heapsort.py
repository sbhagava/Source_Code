__author__ = 'Sonu'
import random
import time
def heapsort( aList ):
    # convert aList to heap
    length = len( aList ) - 1
    leastParent = length // 2
    for i in range ( leastParent, -1, -1 ):
        moveDown( aList, i, length )

    # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if aList[0] > aList[i]:
            swap( aList, 0, i )
            moveDown( aList, 0, i - 1 )


def moveDown( aList, first, last ):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[first]:
            swap( aList, largest, first )
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return # force exit


def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def main_heap():
    input =[1000,3000,5000,10000,15000,20000,32000]
    for s in range (0,len(input),1):
        alist = random.sample(range(1,input[s]),input[s]-1)
        stime= time.time()
        heapsort(alist)
        etime=time.time()
        print ("Unsorted Array : \t Array Size:",input[s],"\tStart Time",stime,"\tEnd Time",etime,"\tExecution Time",round(((etime-stime)*1000),2))
        alist.sort()
        stime1=time.time()
        heapsort(alist)
        etime1=time.time()
        print ("Sorted Array : \t Array Size:",input[s],"\tStart Time",stime,"\tEnd Time",etime,"\tExecution Time",round(((etime1-stime1)*1000),2))
        alist.sort(reverse=True)
        stime2=time.time()
        heapsort(alist)
        etime2=time.time()
        print ("Reverse Sorted Array : \t Array Size:",input[s],"\tStart Time",stime2,"\tEnd Time",etime2,"\tExecution Time",round(((etime2-stime2)*1000),2))

def main():
    main_heap()     #print(alist)

if __name__ == "__main__":
    main()

