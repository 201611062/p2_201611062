
import os

def findword():
    mydir=os.getcwd()
    filename='writefileBasic.txt'
    myfilename=os.path.join(mydir,filename)
    file=raw_input("Write file name : ")
    if filename==file:
        #한 줄읽기    
        myfile=open(filename)
        line=myfile.readline()
        myfile.close()
        print line
    
        #전체읽기
        myfile=open(filename)
        for line in myfile:
            print line
        myfile.close()
    
        #줄 찾기
        word=raw_input("Write word : ")
        myfile=open(filename,'r')
        for line in myfile:
            if line.find(word)>=0:
                print line
        myfile.close()
        
    else:
        print IOError

    
def changeUpper():
    #대문자 바꾸기
    myfile2=open('output.txt','w')
    line1=raw_input("Write line1 : ")
    line2=raw_input("Write line2 : ")
    
    myfile2.write(line1+('\n'))
    myfile2.write(('\t')+line2)
    
    myfile2=open('output.txt','r') 
    contentstwo=myfile2.readlines() 
    for a in range(0,len(contentstwo)): 
        print contentstwo[a].upper() 
    myfile2.close() 

def lab13():
    findword()
    changeUpper()

def main():
    lab13()

main()
raw_input("")
