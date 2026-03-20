q = int(input())
commands = []
for _ in range(q):
    line = input().split()
    if line[0] != "clear":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0], None))

# Please write your code here.

s = 0

for command in commands:
    action = command[0]
    target = command[1]
    t = (1<<target)
    
    if action == "clear":
        s = 0
    elif action == "delete":
        s = s & ~t
    elif action == "print":
        if s&t: print('1')
        else: print('0')
    elif action == "toggle":
        s = s ^ t
    elif action == "add":
        s = s | t