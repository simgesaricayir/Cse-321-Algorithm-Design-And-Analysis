def searchString(text,sub,result,index,validIndex):
    my_dict = {'to' : 'A', 'be' : 'B','or' : 'C','not' : 'D'}
    if "to" in sub:
        result+=(my_dict['to'])
        sub = ""
        validIndex+=2
    if 'be' in sub:
        result+=(my_dict['be'])
        sub = ""
        validIndex+=2
    if 'or' in sub:
        result+=(my_dict['or'])
        sub = ""
        validIndex+=2
    if 'not'in sub:
        result+=(my_dict['not'])
        sub = ""
        validIndex+=3
    if index == len(text):
        if validIndex == len(text):
            return True
        else:
            return False
    else:
        sub += text[index]
        return search(text,sub,result,index+1,validIndex)

text = "tobeornottobe"
print(text,search(text,result,"",-1,0),result)
text = "tobeornotajskdktobe"
print(text,search(text,result,"",-1,0),result)
text = "tobeornotototobe"
print(text,search(text,result,"",-1,0),result)
text = "tobeornottobenottobe"
print(text,search(text,result,"",-1,0),result)


