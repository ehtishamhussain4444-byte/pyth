if 2 >3:
    print("two is greater then three")
    if 4>2:
        print("s")
elif 5>4:
    print("five is greater then four")
else:
    print("both are incorrect")


list=["apple","mangoe","pineapple"]
x,y,z=list
print(x,y,z)


x="sweets"
def myfuc():
    print("he likes"+" "+x)
myfuc()

x="sweets"
def myfuc():
    x="lemon"
    print("he like "+" "+x)
myfuc()

name="ahsan"
def myfuc():
    name="ehtisham"
    print("he like"+" "+name)
myfuc()

name="subhan"`
def myfuc():
    globalname="ehtisham"
    print('he is outstanding and his name is'+" "+name)
myfuc()

x=56
p=float(56)
print(p)
c=45.00
b=int(45.00)
print(b)

x="ehtisham"
y=56
print(x,y)
print(type(y))

#if u want to print random numbers
import random
print(random.randrange(1,10))

#loops
p="pakistan"
print(len(p))
print(format(p))
print(p[2])


x="pakistan is my beatiful country"
if "my" in x:
    print("yes", 'my'in x)

x="he is good"
if "he"not in x:
    print("yes")
if "excellent" in x:
    print("no")
else:
    print("i am right")

x="pakistan is my country"
if "yes" in x:
    print("yes")
else:
    print("no")


x="out of limit"
#print(x.replace("out","he").replace("of","is"))
print(x.split())

x="good"
para="he is a {} student"
print(para.format(x))
print(para.capitalize())

subgrade=50
if subgrade>60:
    print("he is passed")
if subgrade<50:
    print("he is failed")
else:
    print("he has passed the whole exam")

subhangrade=60
if subhangrade>40 and subhangrade<50:
    print("he has passed with c grade")
elif subhangrade>50 and subhangrade<70:
    print("he has passed with b grade")
else:
    print("he is failed")

grade=40
if grade>30:
    print("his percentage is 20 ")
    if grade<50:
        print("he is mediocare")

i=2
while i<30:
    print(i)
    if i==28:
        break
    i+=2

i=3
while i<40:
    i+=3
    if i==30:
        continue
    print(i)

def myfuc(name):
    print(name+" "+"khan")
myfuc("ehtisham")


def myfuc(val1):
    print("this is captain saad reporting sir",val1)
myfuc(32)

def myfuc(fname,lname):
    print(fname+" "+lname)
myfuc("ehti","hussain")




def myfuc(*fruit):
    print("he likes",fruit[1])
myfuc("app","ban","pine")

def factorial(n):
    if n==0:
        return 1
    else:
        return n*6
n=3
print(factorial(n))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*4
#n=4
print(factorial(4))

def threetable(n):
    for x in range(n):
        if x%3:
            continue
        print(x)
threetable(30)

def fourtable(n):
    for x in range(n):
        if x%4:
            continue
        print(x)
fourtable(44)

def fivetable(n):
    for x in range(n):
        if x%5:
            continue
        print(x)

#if u wnat to give more then one arguments
def myfuc(*students):
    print("class 10th cr name is",students[2])
myfuc("subhan","akmal","talha")

#lambda is use if u wnat to give statement in one line
x=lambda val1,val2:val1+val2 
print(x(40,10))

x=lambda val1,val2:val1%val2
print(x(5,20))

x=lambda val1,val2,val3:val1*val2%val3
print(x(4,4,2))

vege=["apple","banana","pineapple"]
vege.append("watermelon")
for x in vege:
    print(x)


fruits=["apple","banana","pineapple"]
fruits.pop(0)
for x in fruits:
    print(x)

planets=["mercury","mars","earth","venus"]
planets.append("jupiter")
for x in planets:
    print(x)


planets=["mercury","mars","earth","venus"]
planets.pop(3)
for x in planets:
    print(x)


x={
    "name":"ehtisham",
    "language":"urdu",
    "nationality":"pakistan"
}
print(x.values())


x=["apple","mangoes","cherry"]
x[1:2]=["pine","kane"]
print(x)

x=["apple","mangoes","banana"]
x[1:2]=["pineapple","watermelon"]
print(x)

a=23
b=43
if a>b:
    print("a is greater tehn b")
else:
    print("b is greater then a")


a=20
b=45
if a>b:
    print("a is greater then b")
elif b==a:
    print("b is equal to a")
else:
    print("b is greater then a")

subhanmarks=85
if subhanmarks>60 and subhanmarks<80:
    print("he is passed with grade 70 percentage and grade b")
elif subhanmarks>80 and subhanmarks<90:
    print("he is passed with 80 percentage and grade a")
elif subhanmarks <40 and subhanmarks <=35:
    print('he is failed')
else :
    print("he doesnt reached the criteria")


subhangrade =50
if subhangrade>40 or subhangrade<40:
    print("he is failed")
elif subhangrade<40 or subhangrade>=50:
    print("he is passed")
else:
    print (" he is fucked up")

subhangrade=50
if subhangrade>35:
    print("he is passed")
    if subhangrade==50:
        print("with grade c")

subgrade=60
if subgrade >40:
    print("he is passed")
    if subgrade <70:
        print("he is failed in maths")


def myfuc():
    print("he is a good boy")
myfuc()

def myfuc(name):
    print("he is outstanding student of his class",name)
myfuc("ehtisham")

def myfuc(val1,val2):
    print("he is good",val1+val2)
myfuc(20,34)


def myfuc(fname,lname):
    print(fname+" "+lname)
myfuc("ehtisham","hussain")


list="a","b","c"
for x in list:
    if x=="b":
        break
    print(x)


#class and objects
class soap:
    def __init__(self,name,company,price):
        self.name=name
        self.company=company
        self.price=price
obj1=soap("lux","branded",120)
print(obj1.name)
print(obj1.company)
print(obj1.price)


class issb:
    def __init__(self,recommended,notrecommended):
        self.recommended=recommended
        self.notrecommended=notrecommended
    def __str__(self):
        return f"{self.recommended}({self.notrecommended})"
    def myfuc(self):
        print("ali is recommende in ",self.recommended)
obj1=issb(10,90)
obj1.myfuc()


def factorial(n):
    if n==0:
        return 1
    else:
        return n*4

print(factorial(4))


print("hello world")




