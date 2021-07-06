str = input()
num = 0
for i in str:
    if ord(i) <= 79:
        num += int((ord(i)-65)/3) + 3
    elif (80 <= ord(i) and ord(i) <= 83):
        num += 8
    elif (84 <= ord(i) and ord(i) <= 86):
        num += 9
    else:
        num += 10

print(num)
