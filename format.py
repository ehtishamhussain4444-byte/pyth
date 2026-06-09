x=20
y=10
z=20.5
OTJ="i buy {} items {} cars, and {} bananas."
print(OTJ.format(x,y,z))

#escape
x=20
y=10
z=20.5
OTJ="i buy {} items {} \"cars\",, and {} bananas."
print(OTJ.format(x,y,z))

x=9
v=float(x)
print(v)

#the price is 9.00$


x=10
print(f"he is outstanding {x:.3f}times")

print(f"the price is {2+3}dollar")

#print the position or r in txt
txt="to be or not to be"
print(txt.find("r"))
print(txt[-1])
print(txt[0])

#to remove spaces and capatilized letters
txt="to be or not to be"
print(txt.replace(" ","").upper())

#relace e by 6 l by 9
x="Hello World"
print(x.replace("e","6").replace("l","9"))

txt="06/30/98"
print(txt.replace("98","1998"))

#print output as Memoon jabbar A
name="abdul jabbar memon"


name = "abdul jabbar memon"
parts = name.split()
formatted_name = f"{parts[2].capitalize()} {parts[1]} A"
print(formatted_name)


