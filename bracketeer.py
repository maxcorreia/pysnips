# Bracketeer: Python script to estimate tournament bracket runtimes
import math

def bracketeer(pnum, elim, bof, mtime, dqp, err):
    if(err == ""):
        err = 1.0
    if(elim == "D" or elim == ""):
        time = (2*(pnum - (pnum * dqp / 100))+.5)*mtime*err
    elif(elim == "s"):
        time = math.floor(math.log(pnum,2))*mtime*err
    else:
        return("Invalid format; Cannot return")
    #return str(time)
    sc = math.floor(time % 60)
    mn = math.floor(time/60)
    hr = math.floor(mn/60)
    return str(hr)+":"+str(mn)+":"+str(sc)
        
    
    

pnum = int(input("Enter the number of players: "))
elim = input("[s]ingle or [D]ouble elimination: ")
bof = float(input("Best of #: "))
mtime = float(input("Match length [S]: "))
dqp = float(input("DQ%: "))
err = float(input("Factor of error (starts at 1.0): "))
print(bracketeer(pnum, elim, bof, mtime, dqp, err)+" the estimated bracket run time")
