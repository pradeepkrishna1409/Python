import random
random.seed()

def shuffle(myList):
   n = len(myList)
   for i in xrange(0, n):
      j = random.randint(i, n-1) # randint is inclusive
      myList[i], myList[j] = myList[j], myList[i]

   print myList




st_list=[6,9,14,3,66,11]
print st_list

shuffle(st_list)







