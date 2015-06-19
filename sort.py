__author__ = 'Sonu'
import sort_merge
import quick_inplace
import heapsort
import modified_qsort


def main() :
    print ('Merge sort')
    sort_merge.main_merge()
    print ('\n\nHeap Sort')
    heapsort.main_heap()
    print('\n\nQuick with median of three')
    modified_qsort.main_quick()
    print('\n\nQuick In place')
    quick_inplace.main_quick()
    print('Thank you')

if __name__ == "__main__":
    main()