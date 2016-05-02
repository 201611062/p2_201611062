import matplotlib
import matplotlib.pyplot as plt

def charCount():
    d=dict()
    word=raw_input("Write word :")
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

def countDigitsLetter(word):
    d=dict()
    d={"number":0, "word":0}
    for c in word:
        if c.isdigit()==True:
            d["number"]+=1
        elif c.isdigit()==False:
            d["word"]+=1
    

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

def findDifference():
    myhouse=set()
    friendhouse=set()
    myhouse={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
    friendhouse={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}
    print myhouse
    print friendhouse
    difference=myhouse.difference(friendhouse)
    print difference

def lab9():
    charCount()
    word=raw_input("Write word")
    countDigitsLetter(word)
    findDifference()

def main():
    lab9()

if __name__=="__main__":
    main()
