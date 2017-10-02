


alist = [1,2,3,4,5,6,7,8,9,10]
K = 10

count=0
new_list=[]

for n in range(len(alist)/2):
    if K - alist[n] in alist:
        new_list.append((n,alist[alist.index(K-n)]))
        count +=1

print new_list
print count