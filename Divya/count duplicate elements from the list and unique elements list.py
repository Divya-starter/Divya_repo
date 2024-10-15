list1=list(map(int,input("enter elements:").split()))

list1_uni=[]
list1_dup=[]
count=0
dict1={}
for i in list1:
    if(i not in list1):
        dict1[i]=1
    else:
        dict1[i]=count+
        count=dict1[i]+1
for k,v in dict1.items():
    print(f"{k} appeared of times {v}")

for keys,values in dict1.items():
    if(values>1):
        list1_dup.append(keys)
    list1_uni.append(keys)
print("dup:",*list1_dup)
print("uni:",*list1_uni)
