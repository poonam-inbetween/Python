# Exercise 5.1


def userinput():
    inp = ""
    total = 0
    count = 0
    avg = 0
    while (inp != 'done'):
        try:
            inp = raw_input("`enter the number\n")
            if(inp != "done"):
                inp = int(inp)
                total = total + inp
                count = count + 1
        except:
            print("`invalid Entry\n")
    avg = float(total) / count

    print(total, count, avg)

userinput()

# Exercise 5.2


def userinput1():
    inp = ""
    all = []

    while(inp != 'done'):
        try:
            inp = raw_input('Enter any number\n')
            if (inp != 'done'):
                inp = int(inp)
                all.append(inp)
        except:
            print('Invalid Entry \n')
    print(all)
    print min(all)
    print max(all)

userinput1()
