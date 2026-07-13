n = int(input())
commands = dict()
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands[k] = v
    elif cmd == "remove":
        commands.pop(k)
    else: # find
        if k in commands:
            print(commands[k])
        else:
            print('None')