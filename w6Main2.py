def sumList(aList):
    x=list()
    for i in range(0,aList):
        if i%4==0 and i%5!=0:
            x.append(i)
    sum=0
    for i in range(0,len(x)):
        sum+=x[i]
    mysum=sum
    return mysum

def lab6():
    "programing too hard"
    aList=1000
    labsum=sumList(aList)
    print labsum

def main():
    lab6()  

main()