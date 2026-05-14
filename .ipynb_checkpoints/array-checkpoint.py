
'''exp=[2200,2350,2600,2130,2190]
print("Feb, how many dollars you spent extra compare to January?",exp[1]-exp[0])
print("your total expense in first quarter",exp[0]+exp[1]+exp[2])
for i in range(len(exp)):
    if exp[i]== 2000:
        print("yes,you spent exactly 2000 in month",i+1)
print(exp.append(1980))
c=exp[3]-200
print("your expense in April decreased by",c,"dollars compare to March")
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)
'''
a=[]
b=int(input("enter the max odd number"))
for i in range(1,b+1,2):
    a.append(i)
print(a)