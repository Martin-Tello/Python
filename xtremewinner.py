x=str(input())
#a=["T6","K15","M11","S12","C5","D15","c8","v5","T8","T9","w7","W17","T18","A6"]
#b=[846,7515, 7711,8312,675,6815,998,1105,848,849,1197,8717,8410,656]
v=[51,23,61,50,2,41,5,8,63,30,42,6,54,49]
print(v.index((ord(x[0])+ord(x[-2]))%65)+1)
#for i in v:
#    print(i//10)
#print(ord(x[0]))
#print(b.index(int(str(ord(x[0]))+str(len(x))))+1)
#print(a.index(x[0]+str(len(x)))+1)
#y = "Knapsackers@UNT"
#print(ord("A"))


#x = ["Team 1","Knapsackers@UNT","MoraSeekers","SurpriseTeam","CuSAT","DongskarPedongi","cofrades","viRUs","TeamName",
#"TeamEPFL1","whatevs","WildCornAncestors","TheCornInTheFields","Aurora"]
#o = ' '.join(format(ord(c), 'b') for c in x[0])
#print(hex(x[0]))
#for i in x:
    #print(ord(i[0])+ord(i[1])+ord(i[-2]))
    #print(((ord(i[0])+ord(i[-2]))%65))#45,49,65
    #print(ord(i[-2]))
    #print(i)
    #print(list(map(ord,(i[0]+i[1]+i[-2]))))
#print(y)
#dic = {"Team 1":1,"Knapsackers@UNT":2,"MoraSeekers":3,"SurpriseTeam":4,"CuSAT":5,"DongskarPedongi":6,"cofrades":7,"viRUs":8,"TeamName":9,
#"TeamEPFL1":10,"whatevs":11,"WildCornAncestors":12,"TheCornInTheFields":13,"Aurora":14}
#print(dic[x])
#x=str(input());dic2={"T6":1,"K15":2,"M11":3,"S12":4,"C5":5,"D15":6,"c8":7,"v5":8,"T8":9,"T9":10,"w7":11,"W17":12,"T18":13,"A6":14};print(dic2[x[0]+str(len(x))])
