n = int(input())
commands = []

x = set()

for _ in range(n):
    cmd, val = input().split()

    if cmd == "add":
        x.add(val)
    elif cmd == "remove":
        x.remove(val)
    else: # find
        if val in x:
            print("true")
        else:
            print("false")
        

# Please write your code here.