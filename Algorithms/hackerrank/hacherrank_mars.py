

if __name__ =="__main__":

    cnt=0

    for x,y in zip('SOSSPSSQSSOR','SOSSOSSOSSOS'):
        if x!=y:
            cnt+=1

    print cnt
