from pydoc import doc

x=[
   [1,2,3],
   [4,5,6],
   [7,8,-45]
   ]
print(len(x))

num=1
diagonal1=0
diagonal2=0
while num <= len(x):
    diagonal1=diagonal1+x[num-1][num-1]
    diagonal2=diagonal2+x[num-1][len(x)-num]
    num=num+1
result=diagonal2-diagonal1
print(abs(result))