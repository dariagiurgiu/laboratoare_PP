from curses.ascii import isdigit

import stiva

def verifParanteze(expr):
    d=0
    i=0
    j=0
    while j<len(expr):
        if expr[j]=='(':
            d+=1
        if expr[j]==')':
            i+=1
        j+=1
    if d==i:
        return True
    else:
        raise "Eroare"

def prioritate(op) -> int:
    if op=='/' or op == '*':
        return int(3)
    else:
        if op == '+' or op == '-':
            return int(2)
        else:
            return int(0)

def transPostfix(expr):
    s=stiva.Stiva()
    inf=str()
    i=0
    while i < len(expr):
        if expr[i]>='0' and expr[i]<='9':
            inf+='|'
            inf+=expr[i]
            j=i+1
            while j< len(expr) and expr[j]>='0' and expr[j]<='9':
                inf+=expr[j]
                j += 1
            inf+='|'
            i=j-1
        else:
            if expr[i]=='(':
                s.push(expr[i])
            else:
                if expr[i]==')':
                    while ~s.isEmpty() and s.top()!='(':
                        inf+=s.top()
                        s.pop()
                    s.pop()
                else:
                    while ~s.isEmpty() and (prioritate(expr[i]) <= prioritate(s.top())):
                        inf+=s.top()
                        s.pop()
                    s.push(expr[i])
        i+=1
    while s.isEmpty()==False:
        if s.top()=='(':
            raise "Eroare"
        inf+=s.top()
        s.pop()
    print(inf)
    return inf

def evalPostfix(expr):
    s=stiva.Stiva()
    i=0
    while i<len(expr):
        if expr[i]=='|':
            nr=""
            j=i+1
            while j< len(expr) and expr[j] != '|':
                nr+=expr[j]
                j+=1
            i=j
            nr_i=float(nr)
            s.push(nr_i)
        else:
            if ~s.isEmpty():
                b=s.top()
                s.pop()
            else:
                raise "Eroare"

            if ~s.isEmpty():
                a=s.top()
                s.pop()
            else:
                raise "Eroare"
            if expr[i]=='+':
                s.push((a+b))
            if expr[i]=='-':
                s.push((a-b))
            if expr[i]=='*':
                s.push((a*b))
            if expr[i]=='/':
                if b==0:
                    raise "Eroare"
                s.push((a/b))
        i+=1
    return s.top()

def elimSpatiiMultiple(str):
    i=0
    while i < len(str):
        if str[i]==' ':
            j=i+1
            while j<len(str) and str[j]==' ':
                str=str[:j]+str[j+1:]
        i+=1
    return str