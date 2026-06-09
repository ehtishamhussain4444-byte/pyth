#variables
x=y=z=1
x,y,z=1,2,3
eht_6_khan=34
x=y=2,3
x_1=4,5
print(x_1)
#nested list
x=[1,2,3,[3,4,5],6,7]
#identations is def the spaces given after :
def myduc():
    a=2 # 1tab press is equal to 4 spaces
    b=4
    return b+1
print(myduc())

a=2
b=4
if a>b:
    print(a) #we cannnot right more thenone statement in line like a>b:b=a
else:
    print(b)

def myfuc(): #if there is non we use pass
    pass

x=23.4
p=int(x)
print(p)
print(type(x))
#sets,tuple
x="pakistan"
k=x[4]
print(k)
k=tuple(x)
j=list(x)
p=set(x)
print(k,j,p)

#collection type
#first is list type
x=[1,2,3]
p=x.insert(2,"pak")
print(x)
k=x.remove(1)
print(x)
x=len(x)
print(x)

x=[1,2,3,4,5,6]
p=x.append(10)
print(x)
p=len(x)
print(p)
k=x.count(2)
print(k)
p=x.reverse()
print(p)

x=4
def myfuc():
    print(2*2+x)
myfuc()

x=10
y=20
def myfuc():
    print(x+y)
myfuc()

x=10
p=float(x)
print(p)

import random
print(random.randrange(1,20))

x="pakistan"
print(x.replace("p","f").replace("n","m"))

x=10
y=20
if x>y:
    print(x)
elif y>x:
    print("the greater valuse is",y)
else:
    print("k")

y="pakistan"
for x in y:
    print(x)

p="his nickname is {}"
x="ali"
print(p.format(x))

x="ali"
def myfuc():
    print("his nickname is ",x)
myfuc()

x="pakistan"
y="country"
z="love"
def myfuc():
    print(x,"is my",y,"and i",z,"it")
myfuc()

i=4
while i<30:
    print(i)
    i+=4

x=10
while x<50:
    print(x)
    x+=10
else:
    print("i is no longer smaller")

def myfuc(city):
    print("pak capital is",city)
myfuc("karachi")
myfuc("mardan")

def myfuc(boys):
    print("his name is",boys)
myfuc("ehtisham")
myfuc("khan")

def add(val1,val2):
    print("the sum is ",val1+val2)
add(23,24)

def myfuc(fname,mname):
    print("his f and m name is",fname+mname)
myfuc("sardar","mumtaz")

x=1,2,3,4,5,6
for y in x :
    if x==5:
        break
    print(y)

for x in range(30):
    print(x)


def myfuc(n):
    print(n*3)
myfuc(3)

#factorial
def factorial(n):
    if n==0:
        return 1
    else:
        print(n*5)
factorial(3)

def evennumber(n):
    for x in range(n):
        if x%2:
            continue
        print(x)
n=30
evennumber(n)

p=lambda a,b:a+b
print(p(2,3))

c=["a","b","c"]
p=c.append("k")
for x in c:
    print(x)    

c=["a","b","c"]
k=c.remove("c")
for x in c:
    print(x)

class car:
    def __init__(self,comname,carname,price):
        self.comname=comname
        self.carname=carname
        self.price=price
    def __str__(self):
        return f"{self.comname}({self.carname})({self.price})"
obj1=car("honda", "civic", "4000000")
print(obj1)

class car:
    def __init__(self,comname,carname,price):
        self.comname=comname
        self.carname=carname
        self.price=price

    def __str__(self):
        return f"[self.comname]{self.carname}{self.price}"

    def myfuc(self):
        print("my car name is ",self.comname)
        
obj1=car("honda","civic","k")
obj1.myfuc()

x=1,2,3,4,5,6,7,8,9
count_even=0
count_odd=0
for y in x:
    if y%2:
        count_even+=1
    else:
        count_odd+=1
print(count_even)
print(count_odd)

cap={
    "name":"ehtisham",
    "class":"2nd semester",
    "roll no" : "45"
}
print(cap.values())
print(cap)


def area(a,b):
    print("the area of sqare is =",a*b)
area(3,4)

#find the area of circle 
pi=3.14
r=4
def area():
    print("area of circle =",pi*r*r)
area()

ideology=80
pak=90
cs=90
pf=89
dld=78
civic=88
sum=ideology+pak+cs+dld+civic
percentage=float(sum*100)/600
print("your total marks are =",sum)
print("your total percentage is =",percentage)
if percentage>85:
    print("your grade is A+")
elif percentage>=80 and percentage<=84:
    print("your grade is A")
elif percentage>=70 and percentage<=79:
    print("your grade is B")
elif percentage>=65 and percentage<=69:
    print("your grade is c")
elif percentage>=55 and percentage<=65:
    print("your grade is d")
elif percentage>=45 and percentage<=54:
    print("your grade is e")
else:
    print("you have failed the exam")








