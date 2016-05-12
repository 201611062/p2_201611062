def georgeBush(): 
    bush=list() 
    bush=["Vice President Cheney, Mr. Chief Justice, President Carter, President Bush, President Clinton, reverend clergy, distinguished guests, fellow citizens:",

    "On this day, prescribed by law and marked by ceremony, we celebrate the durable wisdom of our Constitution, and recall the deep commitments that unite our country.",
    "I am grateful for the honor of this hour, mindful of the consequential times in which we live, and determined to fulfill the oath that I have sworn and you have witnessed.",
    "At this second gathering, our duties are defined not by the words I use, but by the history we have seen together. For a half century,",
    "America defended our own freedom by standing watch on distant borders.",
    "After the shipwreck of communism came years of relative quiet, years of repose, years of sabbatical —and then there came a day of fire.", 
    "We have seen our vulnerability —and we have seen its deepest source."
    "For as long as whole regions of the world simmer in resentment and tyranny —prone to ideologies that feed hatred and excuse murder — violence will gather,"
    "and multiply in destructive power, and cross the most defended borders, and raise a mortal threat."
    "There is only one force of history that can break the reign of hatred and resentment, and expose the pretensions of tyrants,"
    "and reward the hopes of the decent and tolerant, and that is the force of human freedom."

    "We are led, by events and common sense, to one conclusion: The survival of liberty in our land increasingly depends on the success of liberty in other lands."
    "The best hope for peace in our world is the expansion of freedom in all the world. "]

    doc=bush 
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
    c=list()
    for i in d.keys(): 
        b.append(i) 
    for i in range(len(a)): 
        if a[i]>=5: 
            c.append(b[i])
    print "Bush was likely to say words "+str(c)+" in his speech"  

def georgeWashington():
    washington=list()
    washington=["AMONG the vicissitudes incident to life no event could have filled me with greater anxieties than that of which the notification was transmitted by your order,", 
    "and received on the 14th day of the present month. On the one hand, I was summoned by my country, whose voice I can never hear but with veneration and love,",
    "from a retreat which I had chosen with the fondest predilection, and, in my flattering hopes, with an immutable decision, as the asylum of my declining years - a retreat which was rendered", 
    "every day more necessary as well as more dear to me by the addition of habit to inclination, and of frequent interruptions in my health to the gradual waste committed on it by time.", 
    "On the other hand, the magnitude and difficulty of the trust to which the voice of my country called me, being sufficient to awaken in the wisest and most experienced of her citizens",
    "a distrustful scrutiny into his qualifications, could not but overwhelm with despondence one who (inheriting inferior endowments from nature and unpracticed in the duties of civil administration)", 
    "ought to be peculiarly conscious of his own deficiencies. In this conflict of emotions all I dare aver is that it has been my faithful study to collect my duty from a" 
    "just appreciation of every circumstance by which it might be affected. All I dare hope is that if, in executing this task,", 
    "I have been too much swayed by a grateful remembrance of former instances, or by an affectionate sensibility to this transcendent proof", 
    "of the confidence of my fellow-citizens, and have thence too little consulted my incapacity as well as disinclination for the weighty and", 
    "untried cares before me, my error will be palliated by the motives which mislead me, and its consequences be judged by my country with some share of the partiality in which they originated."]

    doc=washington 
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
    c=list()
    for i in d.keys(): 
        b.append(i) 
    for i in range(len(a)): 
        if a[i]>=5: 
            c.append(b[i])
    print "Washington was likely to say words "+str(c)+" in his speech"

def presidentSpeech():
    georgeBush()
    georgeWashington()

def school():
    sc=list()
    sc=[["Division","Very well","Well","Bad","Very bad"],["Class quality",13.1,37.1,8.7,1.5
        ],["Class way",10.6,34.6,13.4,1.9],["Friendship",27.1,40.0,2.9,1.5],["Teacher",16.2,37.8,6.8,0.8],
       ["School facility",11.4,29.8,14.8,4.9],["School environment",12.2,26.5,14.9,4.4],
        ["Major",13.5,29.7,11.1,2.4],["School life",13.7,37.6,4.1,1.2]]
    sc2=sc[1:]
    sum=0
    for i in sc2:
        sum1=i[1]+i[2]
        sum+=sum1
    sum2=0
    for i in sc2:
        sum3=i[3]+i[4]
        sum2+=sum3
    wellAverage=sum/len(sc2)
    badAverage=sum2/len(sc2)
    
    print "Well average is "+str(wellAverage)
    print "Bad average is "+str(badAverage)

def lab11():
    presidentSpeech()
    school()

def main():
    lab11()

main()
