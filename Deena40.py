a=30
found=False
b=[]
for i in range(2,a):
if all(i%j!=0 for j in range(2,i)):
b.append(i)
for k in range(len(b)):
for l in range(k+1,len(b)):
if b[k] + b[l]==a:
print([b[k],b[l]])
found=True
if not found:
print(“no pairs found”)
