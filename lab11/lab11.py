from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    if low<high:
      if high-low == 1:
        if lst[low]>lst[high]:
          lst[low], lst[high] = lst[high], lst[low]
        return
      p = pivot_fn(lst,low,high)
      #print(lst[low:high],p,low,high)
      #partion code
      start=low+1
      end=high
      pivot=lst[p]
      lst[p], lst[low] = lst[low], lst[p]
      #print (lst, pivot, low, high)
      while start < end:
        while start < len(lst) and lst[start] <= pivot:
            start += 1
        while lst[end] > pivot:
            end -= 1
        if(start < end):
            lst[start], lst[end] = lst[end], lst[start]
            #print("switched",lst[start],lst[end])

      lst[end], lst[low] = lst[low], lst[end]
      #print (lst, pivot)
      qsort(lst,low,end-1,pivot_fn)
      qsort(lst,end+1,high,pivot_fn)
    
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    return low
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    return random.randint(low,high)
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    import statistics
    res = statistics.median([lst[low], lst[(low + high) // 2], lst[high]])
    return res
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    #print(lst)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    #print(lst)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
