def virtual_converter(s:str,alphabets:dict)->str:
    final=""
    for i in s:
        final=final+alphabets[i]
    
    return final.upper()