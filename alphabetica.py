from collections import deque
import string
import sys

abc = string.ascii_uppercase
mem = deque([])
heap = {}
ifbuff = [False, []]
f = open(sys.argv[1]).read().split("\n")
p = 0

def dorv(v,n,m):
    if v[n]=="d": return mem[int(v[m], base=36)]
    if v[n]=="v": return heap[v[m]]

def numon_if(v):
    ifd = {
        "-":"!=",
        ":":">",
        ";":"<",
        "=":"=="}

    o = dorv(v,1,3)
    if type(o)==str: o = f"'{o}'"
    t = dorv(v,2,5)
    if type(t)==str: t = f"'{t}'"
    condition = f"{o}{ifd[v[4]]}{t}"

    return [eval(condition), v[6:]] 

def numon_math(v):
    math_d = {
        "s":"-",
        "a":"+",
        "m":"*",
        "d":"/",
        "o":"%"}

    o = dorv(v,1,3)
    if not str(o).lstrip("-").isdigit(): o = f"'{o}'"
    t = dorv(v,2,5)
    if not str(t).lstrip("-").isdigit(): t = f"'{t}'"
    return f"{o}{math_d[v[4]]}{t}"

def numon(v, n=1):
    d = "".join(v[(n+1):])
    if v[n]=="s": return sum([abc.find(v[(n+1):][i])+1 for i in range(len(v[(n+1):]))]) 
    if v[n]=="v": return heap[v[n+1]]
    if v[n]=="w": return chr(heap[v[n+1]])
    if v[n]=="m": return mem[int(v[n+1], base=36)]
    if v[n]=="h": return mem[int(heap[v[n+1]])%len(mem)]
    if v[n]=="n": return d
    if v[n]=="k": return "".join(v[(n+2):int(v[n+1])+3])
    if v[n]=="x": return int(d)
    if v[n]=="6": return int(d, base=36)
    if v[n]=="y": return float(d)
    if v[n]=="i": return int(input())
    if v[n]=="f": return float(input())
    if v[n]=="r": return str(input())
    if v[n]=="a": return chr(int(d))
    if v[n]=="o": return ord(d[0])

while p!=len(f[0]):
    vl = [f[i][p] for i in range(len(f))]
    if ifbuff[0]: 
        vl = ifbuff[1]
        p-=1
        ifbuff = [False, []]
    match vl[0]:
        case "g": print("".join([chr(i) if vl[1]=="t" else str(i) for i in mem]), end="")
        case "a": mem.append(numon(vl))
        case "b": mem.appendleft(numon(vl))
        case "c": heap[vl[1]] = mem.pop()
        case "d": heap[vl[1]] = mem.popleft()
        case "u": 
            t = numon(vl)
            if type(t)==str: [mem.append(i) for i in t]
            else: mem.append(t)
        case "o": print(numon(vl), end="")
        case "h": ifbuff = numon_if(vl)
        case "e": break
        case "m": 
            if vl[6]=="d": 
                mem[int(vl[7], base=36)] = eval(numon_math(vl))
            if vl[6]=="v": heap[vl[7]] = eval(numon_math(vl))
        case "j": p = numon(vl)-1
        
    p+=1
