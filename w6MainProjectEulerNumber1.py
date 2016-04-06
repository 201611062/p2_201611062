def solve(size):
    oldsize=0
    for i in range(size+1):
        if (i%3==0 or i%5==0):
            oldsize=oldsize+i
        result=oldsize
    print result

solve(1000)