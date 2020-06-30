def formatcode(code):
    tmp=''
    while(len(code)>3):
        tmp+=code[:4]+'-'
        code=code[4:]
    tmp+=code
    if tmp[-1]=='-':tmp=tmp[:-1]
    return tmp