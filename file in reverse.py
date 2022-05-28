#Read the contents of file in reverse order:

def program():
    for i in reversed(list(open("merge.txt","r"))):
        print(i.rstrip())
program()
