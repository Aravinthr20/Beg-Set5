a=[]
s=int(input())
for i in range(0,s):
    i=input("Your Value:")
    a.append(i)
    a.sort()
print(min(a),max(a))