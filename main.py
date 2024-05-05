import os ,time as t,sys##from server import server
animation = "|/-\\"
start_time = t.time()
os.system("cls" if os.name == "nt" else "clear")
def mainUpdater():#this updater line of script main afterremove library server
    with open('main.py', 'r') as file:
        lines = file.readlines()
    lines.pop(21)  
    lines.pop(21)  # Remove line 3 (index 2)
    with open('main.py', 'w') as file:# heer open file main and apply remove lines
        file.writelines(lines)
while True:
    for i in range(4):
        t.sleep(0.2)  
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if t.time() - start_time > 10:  
        break
if os.path.exists("update.txt"):
    choix = input("You have an update that you want to apply ?\n (Y/N) :")
    if choix == "Y" or choix =="y":#
        from check import check_file_exists#
        check_file_exists()
        print("Removing files ")
        t.sleep(3)
        os.remove("check.py")
        os.remove("server.py")
        os.remove("update.txt")
        os.system("cls" if os.name == "nt" else "clear")
        print("fixing Problems.")
        for i in range(21):
            sys.stdout.write('\r')
            sys.stdout.write("        [%-20s] %d%%" % ('='*i, 5*i))
            sys.stdout.flush()
            t.sleep(0.25)
        t.sleep(2)
        mainUpdater()
        os.system("cls" if os.name == "nt" else "clear")
        print("Bot Started")#
        os.system("node index.js")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        if os.path.exists("server.py"):
            from server import server
            print("Running Server .")#
            server()
            os.system("node index.js")
        else:
            print("Running Bot .")
            os.system("node index.js")
else:
    os.system("node index.js")