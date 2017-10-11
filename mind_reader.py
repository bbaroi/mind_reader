a=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
b=[2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
c=[8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
d=[4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
e=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
number_list=[a,b,c,d,e]
g=['a','b','c','d','e']
answer=0
print("\nTHINK OF A NUMBER BETWEEN 1 AND 31 AND THE COMPUTER WILL GUESS THE NUMBER")
print("--------------------------------------------------------------------------\n")
for counter in range(0,5):
    print("{}={}\n".format(g[counter].upper(),number_list[counter]))
    x=input("Is the number in list {} [YES or NO]: ".format(g[counter].upper()))
    print("\n")
    if x.lower() == 'yes':
        answer +=int(number_list[counter][0])
    elif x.lower() != 'yes' and x.lower() != 'no':
        print("Enter YES or NO only,try again")
        break
    number_list +=number_list[counter]
    g +=g[counter]
    if counter == 4:
        print("\nThe number you picked was {}\n".format(answer))


    
    
    
    
