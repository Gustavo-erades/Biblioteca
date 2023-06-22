import re
def validatelefone(telefone):
    target=telefone
    pattern=re.compile("^\([0-9]{2}\)[\s\S]?[0-9]{5}\-[0-9]{4}$")
    match= re.fullmatch(pattern,target)
    if(match!=None):
        return True
    else:
        return False
