import math
import matplotlib
import matplotlib.pyplot as plt

def findNew():
    Location=tuple()
    Location=[(37.575869, 126.976637),(37.576549, 126.985520),(37.571618, 126.976551),(37.574577, 126.957754)]
    x=list()
    y=list()
    z=list()
    for i in Location:
        x.append(i[0])
        y.append(i[1])
    for c in range(0,len(x)-1):
        z.append(math.sqrt((x[0]-x[c+1])**2+(y[0]-y[c+1])**2))
    anguk=z[0]
    Gwanghwamun=z[1]
    Dongnimmun=z[2]
    min (anguk,Gwanghwamun,Dongnimmun)
    print "Gwangwamun"

def seoulPopularGragh():
    popular=tuple()
    popular={(74425, 76326
    ),(61164, 61636
    ),(109688, 115744
    ),(144796, 146776
    ),(174996, 181676
    ),(177841, 177434
    ),(204630, 205980
    ),(223373, 232245
    ),(161055, 166130
    ),(171576, 176735
    ),(279169, 293772
    ),(239450, 251066
    ),(148690, 156510
    ),(182977, 196992
    ),(237792, 242641
    ),(283869, 296762
    ),(209344, 210282
    ),(118965, 114441
    ),(186503, 186856
    ),(195734, 203014
    ),(254381, 249472
    ),(212401, 229111
    ),(271654, 295354
    ),(319197, 335045
    ),(229829, 231671)}
    x=list()
    y=list()
    for i in popular:
        x.append(i[0])
        y.append(i[1])
    sum=0
    for i in range(0,len(x)):
        sum+=x[i]
        boy=sum
    for i in range(0,len(y)):
        sum+=y[i]
        girl=sum
    boyAverage=boy/len(x)
    girlAverage=girl/len(y)
    x=dict()
    x={"boySum":boy,"girlSum":girl,"boyAverage":boyAverage,"girlAverage":girlAverage}
    plt.bar(range(len(x)),x.values(), align='center')
    plt.xticks(range(0,10), list(x.keys()))
    #단위는 백만
    plt.show()

def lab9():
    findNew()
    seoulPopularGragh()

def main():
    lab9()

main()
