import csv




def prod_lst_m1(lst):

    prd_lst=[]
    for i in range(0,len(lst)):
        prd=1
        for j in range(0,len(lst)):
            if i != j:
                prd *= lst[j]
        prd_lst.append(prd)

    print prd_lst




def prod_lst_m2(lst):

    prd=1
    for i in range(0,len(lst)):
        prd *= lst[i]

    print [  prd/lst[i] for i in range(0,len(lst))]

if __name__ =="__main__":

   dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

   print dict['Age']
   prod_lst_m1([1,2,3,4])


