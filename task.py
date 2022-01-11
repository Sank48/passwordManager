#!/usr/bin/env python3
import sys
import os

n=len(sys.argv)
if n==1 or (sys.argv[1]=="help" and n==2):
    print('''Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics''')
elif sys.argv[1]=="ls":
    try:
        c=1
        with open("task.txt","r") as file:
            l=file.readlines()
            for line in l:
                #print(line)
                li=line.split(" ",1)
                print(str(c)+". "+li[1].rstrip()+" ["+li[0]+"]")
                c+=1
    except:
        print("There are no pending tasks!")
elif sys.argv[1]=="add":
    #print(n)
    try:
        l=[]
        if os.path.isfile("task.txt"):
            with open("task.txt","r") as file:
                for line in file:
                    l.append(line.rstrip())
        s=sys.argv[2]+" "+sys.argv[3]
        l.append(s)
        l.sort(key = lambda x: int(x.split()[0]))
        with open("task.txt","w") as f:
            for i in l:
                f.write(i+"\n")
        print("Added task: "+'"'+sys.argv[3]+'"'+" with priority "+sys.argv[2])
    except:
        if n<=3:
            print("Error: Missing tasks string. Nothing added!")
elif sys.argv[1]=="del":
    try:
        c=1
        f=0
        if os.path.isfile("task.txt") and n!=2:
            with open("task.txt", "r") as file:
                d=file.readlines()
            with open("task.txt","w") as file:
                for line in d:
                    #li=line.split(" ",1)
                    if c==int(sys.argv[2]):
                        f=1
                    if c!=int(sys.argv[2]):
                        file.write(line)
                    c+=1
            if f==1:
                print("Deleted task #"+sys.argv[2])
            elif f==0:
                print("Error: task with index #"+sys.argv[2]+" does not exist. Nothing deleted.")
        else:
            print("Error: Missing NUMBER for deleting tasks.")
    except:
        if n==2:
            print("Error: Missing NUMBER for deleting tasks.")
elif sys.argv[1]=="done":
    try:
        ct=''
        f=0
        c=1
        if os.path.isfile("task.txt"):
            with open("task.txt",'r') as file:
                d=file.readlines()
            with open("task.txt","w") as file:
                for line in d:
                    if c!=int(sys.argv[2]):
                        file.write(line)
                    else:
                        #print(line)
                        ct+=line
                        f=1
                    c+=1
            with open ("complete.txt","a") as file: 
                file.write(ct) 
            if f==1 and int(sys.argv[2])>0:
                print("Marked item as done.")
            elif f==0 or int(sys.argv[2])<1:
                print("Error: no incomplete item with index #"+sys.argv[2]+" exists.")
        else:
            print("No task added!")
    except:
        print("Error: Missing NUMBER for marking tasks as done.")
elif sys.argv[1]=="report":
    try:
        if os.path.isfile("task.txt"):
            with open("task.txt","r") as file:
                d1=file.readlines()
            print("Pending : {}".format(len(d1)))
            c=1
            for i in d1:
                #print(i)
                i=i.split(" ",1)
                print(str(c)+". "+i[1].rstrip()+" ["+i[0]+"]")
                c+=1
        else:
            print("Pending : 0")
        if os.path.isfile("complete.txt"):
            with open("complete.txt","r") as f:
                d2=f.readlines()
            c=0
            for i in d2:
                if i not in d1:
                    c+=1
            print("\nCompleted : {}".format(c))
            c=1
            for i in d2:
                if i not in d1:
                    c+=1
            c=1
            for i in d2:
                if i not in d1:
                    i=i.split(" ",1)
                    print(str(c)+". "+i[1].rstrip())
                    c+=1
        else:
            print("\nComplete : 0")
    except Exception as e:
        print(e)
