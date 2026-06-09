#from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
#data={#
    #"name":["khan","imra","ali","talak"],
    #"age":[23,54,32,24],
    #"gender":["male","female","male","shemale"],
    #"passed":["yes","no","yes","yes"]
#}
#pk=pd.DataFrame(data)
#print(pk)
#le=LabelEncoder()
#pk["gender"]=le.fit_transform(pk["gender"])
#pk["passed"]=le.fit_transform(pk["gender"])
#print(pk)
pk=pd.read_csv("D:\project\data")
#pkk=pk.copy()
#pko=pd.get_dummies(pk,columns=["city"])
ohe=OneHotEncoder(sparse_output=False)
#ohe=OneHotEncoder(sparse=False)
po=ohe.fit_transform(pk[["city"]])
print(po)
print(ohe.get_feature_names_out(["city"]))


from sklearn.preprocessing import StandardScaler,MinMaxstandard
import pandas as pd
pk=pd.read_csv("D:\project\clean data")
sto=StandardScaler()
pk=sto.fit_transform(pk[["pay","hours"]])
print(pk)
minmax=MinMaxstandard()
stp=minmax.fit_transform()


from sklearn.preprocessing import LabelEncoder
import pandas as pd
pk=pd.read_csv("clean data")
pk.insert(2,"passed",["yes","no","yes","no"])

le=LabelEncoder()
pk["passed"]=le.fit_transform(pk["passed"])
pk=pd.DataFrame(pk)
print(pk)

from sklearn.preprocessing import StandardScaler,MinMaxScaler


from sklearn.preprocessing import StandardScaler,MinMaxScaler
import pandas as pd
dic={
    "pay":[4000,9000,12000],
    "hours":[2,3,4]
}
#pk=pd.read_csv("clean file")
pk=pd.DataFrame(dic)
st=StandardScaler()
pk[["pay","hours"]]=st.fit_transform(pk[["pay","hours"]])
print(pk)

mm=MinMaxScaler()
pk[["pay","hours"]]=mm.fit_transform(pk[["pay","hours"]])
print(pk)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
X=[[1],[2],[3],[4]]
y=[40,55,60,76]

model.fit(X,y)
hours=float(input("enter the hours that ali study:"))
predicted_marks=model.predict([[hours]])
print(f"for studying {hours} hours ali will get {predicted_marks} marks")

from sklearn.linear_model import LogisticRegression
X=[[1],[2],[3],[4]]
y=[0,0,1,1]
model=LogisticRegression()
model.fit(X,y)
hour=float(input("enter the hours:"))
result=model.predict([[hour]])
if result==1:
    print(f"{hour} you r pass {result}")
else:
    print("u r failed")
    
import matplotlib.pyplot as plt
x=[2,3,4,5]
y=[45,60,80,90]
plt.title("marks of students")
plt.xlabel("hours study")
plt.ylabel("marks obtained")
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
months=["jan","feb","march","april"]
sales=[2000,5000,3000,6000]
plt.plot(months,sales,color="brown",linestyle="--",linewidth=3,marker="o")
plt.title("sale of the year")
plt.xlabel("months")
plt.ylabel("sales in month")
plt.xlim("jan","may")
plt.ylim(2000,7000)

plt.grid()
plt.legend()
plt.show()

import matplotlib.pyplot as plt
product=["A","B","C","D"]
sales=[2000,400,900,3000]
plt.bar(product,sales,color="orange",linewidth="4",label="2025 sales")
plt.title("sales per product")
plt.xlabel("product")
plt.ylabel("sales")
plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt
places=["karachi","quetta","risalpur","islamabad"]
contribution=[2000,4000,3000,1000]
plt.pie(contribution,labels=places,autopct="%1.1f%%",colors=["red","blue","pink","orange"])
plt.title("total contribution in 2026")
plt.show()

import matplotlib.pyplot as plt
scores=[56,34,54,67,76,87,56,44,88,78,97,99,77,65,55,56,65,45]
plt.hist(scores,bins=6,color="blue",edgecolor="pink")
plt.xlabel("scores")
plt.ylabel("total student")
plt.title("marks distribution")
plt.show()

import matplotlib.pyplot as plt
hours=[2,3,5,6,8]
money=[2000,3000,4000,6000,9000]
plt.scatter(hours,money,color="red",marker="o",label="pay")
plt.xlabel("total hour of work")
plt.ylabel("money")
plt.title("pay of work")
plt.legend()
plt.grid()
plt.show()


import matplotlib.pyplot as plt
plt.scatter([1,2,4,5],[200,400,500,600],color="blue",marker="o",label="worker A")
plt.scatter([1,2,4,5],[400,5000,6000,7000],color="black",marker="o",label="worker B")
plt.xlabel("hour of work")
plt.ylabel("pay gien")
plt.title("total work pay")
plt.grid()
plt.legend()
plt.show()

import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(5,5))
x=[2,3,4,5]
y=[45,50,55,60]
#for line graph
ax[0].plot(x,y)
ax[0].set_title("line graph")
ax[1].bar(x,y)
ax[1].set_title("bar graph")
plt.show()


import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,3,figsize=(5,5))
x=[2,3,4,5]
y=[45,50,55,60]
#for line graph
ax[0].plot(x,y)
ax[0].set_title("line graph")
ax[1].bar(x,y)
ax[1].set_title("bar graph")
plt.show()

import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(6,6))
x=[2,3,4,5,6]
y=[45,56,78,88,93]
ax[0].plot(x,y,color="red")
ax[0].set_title("line graph")
ax[1].bar(x,y,color="blue")
ax[1].set_title("bar graph")
fig.suptitle("comparison of bar and line graph")
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
x=[1,2,4,5]
y=[45,50,70,80]
plt.plot(x,y,color="green",label="result of ehtisham")
plt.xlabel("hour studies")
plt.ylabel("marks obtained")
plt.title("marks graph")
plt.grid()
plt.legend()
plt.savefig("graph.pdf",dpi=200,bbox_inches="tight")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
read=pd.read_csv("netflix_titles.csv")
nl=pd.dropna(subset=["type","release_year","duration","country"])
ty=nl["type"].value_counts()
plt.bar(ty.index,ty.values,colors=["red","blue"])
plt.title("bar graph")
plt.xlabel("rat")
plt.ylabel("number of movies")