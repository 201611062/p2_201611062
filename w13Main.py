%%writefile writefileBasic.txt
Python is a widely used general-purpose, high-level programming language.[19][20]
Its design philosophy emphasizes code readability, and
its syntax allows programmers to express concepts in fewer lines of code than
would be possible in languages such as C++ or Java.[21][22]
Python is a widely used general-purpose, high-level programming language.[19][20]
Its design philosophy emphasizes code readability, and
its syntax allows programmers to express concepts in fewer lines of code than
would be possible in languages such as C++ or Java.[21][22]
The language provides constructs intended to enable clear programs on both a small and large scale.[23]

import os

def findword():
    file=raw_input("Write file name : ")
    try:
        myfile=open(file,'r')
    except IOError as e:
        print e

    #한 줄읽기    
    myfile=open(file)
    line=myfile.readline()
    myfile.close()
    print line
    
    #전체읽기
    myfile=open(file)
    for line in myfile:
        print line
    myfile.close()
    
    #줄 찾기
    word=raw_input("Write word : ")
    myfile=open(file,'r')
    for line in myfile:
        if line.find(word)>=0:
            print line
    myfile.close()
    
    #대문자 바꾸기
    myfile=open('output.txt','w')
    line1=raw_input("Write line1 : ")
    line2=raw_input("Write line2 : ")
   
    line1=line1.upper()
    line2=line2.upper()
    
    myfile.write(line1+('\n'))
    myfile.write(('\t')+line2)

def lab13():
    findword()

def main():
    lab13()

main()