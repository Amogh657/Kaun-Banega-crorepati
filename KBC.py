import random

print('lets play kaun banega crorepati')
list=['''who is pm??
A)modi b)trump
c)meloni d)charles''']

list.append(''' Which gas is the most abundant in Earth's atmosphere?
A) Oxygen 
B) Carbon dioxide
C) Nitrogen
D) Hydrogen  ''')
list.append(''' Which country is completely surrounded by South Africa?
A) Lesotho
B) Eswatini
C) Botswana
D) Namibia ''')
list.append('''Which organ in the human body is responsible for producing insulin?
A) Liver
B) Kidney
C) Pancreas
D) Gallbladder''')

list.append('''Which island country was formerly known as Ceylon until 1972?
A) Madagascar
B) Sri Lanka
C) Cyprus
D) Jamaica''')

amount=0

answer=['A','C','A','C','B']
def Amount(i):
    match i:
        case 1:
            print("you won 1 lac")
            amount=100000
            print('next Q for 10 lacs')
            return 100000
        case 2:
            print("you won 10 lacs")
            amount=1000000
            print('next Q for 25 lacs')
            return 1000000
        case 3:
            print("you won 25 lacs")
            amount=2500000
            print('next Q for 50 lacs')
            return 2500000
        case 4:
            print("you won 5000000")
            amount=5000000
            print('next Q for 1 crore')
            return 5000000
        case 5:
            print("1 crore")
            amount=10000000
            return 10000000
        case _:
            print('there is some issue')   

def modify(ind,d):
    d.pop(ind)
    answer.pop(ind)
    return d           



    
for i in range(1,6):
    print('the Question',i,':is on your screen')
    c=random.choice(list)
    print(c)
    ind=list.index(c)
    if(answer[ind]==input()):
        print('u got it correct')
        amount=Amount(i)
    else:
        print('u lost, the correct answer is',answer[ind])
        print('your balance is ',amount)
        break
    list=modify(ind,list)
    
    
