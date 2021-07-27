a=input()
b=input()

a_c = [0 for i in range(26)]
b_c = [0 for i in range(26)]

for i in a:
    a_c[ord(i)-ord('a')]+=1
for i in b:
    b_c[ord(i)-ord('a')]+=1
ans = 0
for i in range(26):
    ans += abs(a_c[i]-b_c[i])
print(ans)
