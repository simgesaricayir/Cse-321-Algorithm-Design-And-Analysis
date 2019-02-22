def searchString(text):
    sub=""
    index=0
    validIndex=0
    my_dict = ("it","was","the","best","of","time","add","new")
    for i in text:
        sub += i
        index = index + 1
        if sub in my_dict:
            validIndex = len(sub)+validIndex
            sub = ""
    if validIndex == index:
        return True
    else:
        return False

print(searchString("itwasthebestaaof"))
print(searchString("itwasthebestof"))
print(searchString("bestof"))
print(searchString("itwastheidea"))
 
print(searchString("itwasthebestoftimes"))