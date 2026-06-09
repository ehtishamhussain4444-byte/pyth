#to find the type we use type fun
a=10
ty=type(a)
print(ty)

#if u want to chnge the type of a ariable
a=34
ty=float(a)
print(ty)

#if u want to access a str we use indexing [start : end ]
pk="He is a good boy "
pk=pk[2:4]
print(pk)
#if u want to access the str in reerse
pk="he is Ali"
pp=pk[::-1]
pp=pk[-3::]
pp=(pk[:-1]+pk[-2]+pk[-3])
print(pp)

#if u want to write more then single line text we use three quotations
nam="""hello ehtisham
its me kamran from UET mardan
how may i help u"""
print(pk)

#if u want to find tht a text is present in str we use in method
pk="hola" in nam
print(pk)

#to find the length we use len() func
nam="he"
ln=len(nam)
print(ln)

#2 or more str can be cnocatenate or add through + 
first_name="ehtisham"
last_name="Hussain"
met=first_name.capitalize()#capital the first letter
met=last_name.upper()#capital all the characters
met=last_name.lower()
print(met)

full_name=first_name+" "+last_name
print(full_name)




