list1=[3,4,5,1,5,3,5]
dict1={}
list1_dup=[]
list1_uni=[]
count=0

for i in list1:
    if i not in dict1:
        dict1[i]=1
    else:
        count=dict1[i]
        dict1[i]=count+1
for k,v in dict1.items():
    print(f"{k} apperaed of times {v}")

for keys,values in dict1.items():
    if(values>1):
        list1_dup.append(keys)
    list1_uni.append(keys)

print("duplicate are:",*list1_dup)
print("unique values are:",*list1_uni)