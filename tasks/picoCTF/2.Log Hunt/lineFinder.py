with open("server.log") as f:
    logs = [i for i in f.readlines()]
for i in logs :
    if "FLAGPART" in i:
        print(i)
