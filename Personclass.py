# Personclass.py

class Person:
    def __init__(self,name=' ',address=' ',phone='',email=''):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def hello(self):
        print("Hi there! My name is ",self.name)


Sally = Person('Sally','1 Any Way','123-4567','sally@gmail')

print(Sally.name)

Sally.hello()

#instantiate a Person in the variable Bob, named "Robert" 
Bob = Person("Robert",'1234 Drive',email='bob@gmail')
Bob.hello()

people=[Bob,Sally]

e=open('emaillist.csv','w')
for member in people:
    l='"'+member.name+'"+","+member.email+'"'+"\n"
    e.writelines(l)
e.close()    


