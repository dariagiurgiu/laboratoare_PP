import functii as fn

if __name__ == "__main__":
    f=open("in.txt")
    str=f.read()
    punc=".,!?:;"
    i=0
    while i < len(str):
        if str[i] in punc:
            str = str[:i] + str[i+1:]
        i+=1
    str=fn.elimSpatiiMultiple(str)

    print(str)

    f.close()
