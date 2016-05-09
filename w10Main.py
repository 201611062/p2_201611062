import turtle
wn=turtle.Screen()

def letItBe():
    let=list()
    let=["when I find myself in times of trouble",
    "mother Mary comes to me",
    "speaking words of wisdom let it be",
    "and in my hour of darkness",
    "she is standing right in front of me",
    "speaking words of wisdom let it be",

    "let it be let it be",
    "let it be let it be",
    "shisper words of wisdom let it be",

    "and when the broken-hearted people",
    "living in the world agree",
    "there will be an answer let it be",
    "for though they may be parted",
    "there is still a chance that they will see",
    "there will be an answer let it be",

    "let it be let it be",
    "let it be let it be",
    "yeah there will be an answer let it be",
    "let it be let it be",
    "let it be let it be",
    "whisper words of wisdom let it be",

    "let it be let it be",
    "ah let it be yeah let it be",
    "whisper words of wisdom let it be",

    "and when the night is cloudy",
    "there is still a light that shines on me",
    "shine on until tomorrow let it be",
    "i wake up to the sound of music",
    "mother Mary comes to me",
    "speaking words of wisdom let it be",

    "let it be let it be",
    "let it be yeah let it be",
    "oh there will be an answer let it be",
    "let it be let it be",
    "let it be yeah let it be",
    "whisper words of wisdom let it be"]
    doc=let
    d=dict()
    for i in range(len(doc)):
        for c in doc[i].split():
            if c not in d:
                d[c]=1
            
            else:
                d[c]+=1
    a=list()
    for i in d.values():
        a.append(i)
    b=list()
    for i in d.keys():
        b.append(i)
    for i in range(len(a)):
        if a[i]>=20:
            print b[i]

def milkPercent():
    allData=list()
    allData=[["coffee","Water","Milk","Icecream"],
      ["Espresso","No","No","No"],
      ["Long Black","Yes","No","No"],
      ["Flat White","No","Yes","No"],
      ["Cappuccino","No","Yes","No"],
      ["Affogato","No","No","Yes"]]
    for i in range(len(allData)-1):
        print allData[i+1]
    data=allData[1:]
    percent=0
    for c in data:
        if c[2]=="Yes":
            percent+=1
    percent=float(percent)
    per=str(percent/5*100)
    print "Using Milk percent is "+per+"%"

def mathEnglish():
    grade=list()
    sum=dict()
    for i in grade:
        print i[0]
    sum={"English":0,"Math":0}
    en=0
    ma=0
    grade=[["English",100],["Math",200],["English",200],["Math",200],["English",100],["Math",300]]
    for i in grade:
        if i[0]=="English":
            en+=1
        elif i[0]=="Math":
            ma+=1
    for i in grade:
        if i[0]=="English":
            sum["English"]+=i[1]
        elif i[0]=="Math":
            sum["Math"]+=i[1]
    print "Math sum is "+str(sum['Math'])
    print "English average is "+str(sum['English'])
    print "Math average is "+str(sum['Math']/ma)
    print "English average is "+str(sum['English']/en)

def lab10():
    letItBe()
    milkPercent()
    mathEnglish()
def main():
    lab10()

main()
wn.exitonclick()