def partyInvite(people,pairs):
    InviteList = []
    resultList = []

    for who in people: #for every person in the people list
        searched =0
        know =0
        for p in pairs:#find the person in the pairs list and calculate persons that it knows
            searched = searched + 1
            if p[0]==who or p[1]==who:
                know = know +1
            if searched==len(pairs) and know <5 :
                break
            if know >= 5  and searched==len(pairs) and  len(people)- know >=5:#if it is suitable to invite add into the list.
                InviteList.append(who)
                break

    for invited in InviteList: #last check 
        know =0
        searched =0
        for p in pairs:
                searched = searched + 1
                if ((p[0]==invited  and (p[1] in InviteList)) or (p[1]==invited and (p[0] in InviteList))):
                    know = know +1
                if  searched==len(pairs) and know >= 5 and len(InviteList)-know>=5:
                    resultList.append(invited)
                    break
                                       
    return resultList
    
    
    
people = ["Adriana","Abby","Annalise","Nia","Bella","Carla","John","Caroline","Jack","Sam","Chris","Danielle","Jaime","Karen",
          "Lena","Lucy","Madeline","Margaret","Paris","Ryan","Fred"]
pairs = [("Annalise","Sam"),("Annalise","Jack"),("Bella","Annalise"),("Danielle","Annalise"),("Karen","Annalise"),
         ("Sam","Jack"),("Sam","Bella"),("Sam","Danielle"),("Sam","Karen"),
         ("Jack","Bella"),("Jack","Danielle"),("Jack","Karen"),
         ("Bella","Danielle"),("Bella","Karen"),("Danielle","Karen"),
         
         ("Nia","Chris"),("Nia","Jaime"),("Nia","Lena"),("Nia","Lucy"),("Nia","Margaret"),
         ("Chris","Jaime"),("Chris","Lena"),("Chris","Lucy"),("Chris","Margaret"),
         ("Jaime","Lena"),("Jaime","Lucy"),("Jaime","Margaret"),
         ("Lena","Lucy"),("Lena","Margaret"),("Lucy","Margaret"),
         ("Paris","Karen"),("Paris","Margaret"),("Paris","Nia"),("Paris","Sam"),("Paris","Fred")    
        ]

print(partyInvite(people,pairs))