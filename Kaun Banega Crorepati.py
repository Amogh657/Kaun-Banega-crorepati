import json
import random

lifelines = [
        '1. 50-50',
        '2. audience poll']

class kbc:
    def __init__(self):
        with open ("questions.json", "r") as file:
            self.data = json.load(file)
    def score(self,n):
        match(n):
            case 1:
                print("you won 1 lac")
                print('next Q for 10 lacs')
                return 100000
            case 2:
                print("you won 10 lacs")
                print('next Q for 25 lacs')
                return 1000000
            case 3:
                print("you won 25 lacs")
                print('next Q for 50 lacs')
                return 2500000
            case 4:
                print("you won 5000000")
                print('next Q for 1 crore')
                return 5000000
            case 5:
                print("1 crore")
                return 10000000
            case _:
                print('there is some issue')

    def lifeline(self,c):
        if(len(lifelines)==0):
            print('no lifelines left')
            return
        else:
            for lifeline in lifelines:
                print(lifeline)
            x=input('choose your lifeline: ')
            match(int(x)):
                case 1:
                    print('50-50 lifeline activated')
                    print('removing 2 wrong options')
                    c['options'].remove(random.choice([i for i in c['options'] if i.split(" ")[0] != c['answer']]))
                    c['options'].remove(random.choice([i for i in c['options'] if i.split(" ")[0] != c['answer']]))
                    print('remaining options are: ')
                    for i in c['options']:
                        print(i)
                    lifelines.remove('1. 50-50')    
                case 2:
                    print('audience poll activated')
                    print('audience poll results: ')
                    for i in c['options']:
                        if i.split(" ")[0] == c['answer']:
                            print(f"{i}: 70%")
                        else:
                            print(f"{i}: 10%")
                    lifelines.remove('2. audience poll')            
n=1
person = kbc()
with open ("questions.json", "r") as file:
    data = json.load(file)
    c=random.choice(data)       
while(len(data)!=0):
    c=random.choice(data)
    print(f"{n}.{c['question']}")
    for i in c['options']:
        print(i)
    choice = input('enter your answer or write lifeline to use one: ').upper()
    if choice.upper() == 'LIFELINE':
        person.lifeline(c)
        amount=choice = input('enter your answer ').upper()       
    
    if(c['answer']==choice):
        amount=person.score(n)
        data.remove(c)
        n+=1
    else:
        print('u lost, the correct answer is',c['answer'],"you won",amount)
        break   