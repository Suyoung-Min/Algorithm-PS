n=input()
num=[0]*(10)
for i in n:
    num[int(i)]+=1
if (num[6]+num[9])%2 == 1:
    num[6]=(num[6]+num[9])//2 +1
else:
    num[6]=(num[6]+num[9])//2
num[9]=0
print(max(num))
