import time

def txt():
    data=[1,2,3,4,5,6,7,8,9,10]
    meno=open('ouputNumber.txt','w')
    for i in data:
        if i%2==0:
            i=str(i)
            meno.write(i+'\n')
        else:
            i=str(i)
            meno.write(i+'\t')
    meno.close()

def changeUpper():
    t1=open('output.txt','w')
    t1.write('frist line\n')
    t1.write('second line\n')
    t1.write('third')
    t1.close()
    fin=open('output.txt','r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        for word in words:
            if word=='line':
                word=word.upper()
                fout.write(word+'\n')
            else:
                fout.write(word+' ')
    fin.close()
    fout.close()

def lab13():
    txt()
    changeUpper()

def main():
    lab13()

main()