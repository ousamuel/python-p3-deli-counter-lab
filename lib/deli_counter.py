
def line(list):
    if(len(list) == 0):
        print("The line is currently empty.")
    else:
        i = 0
        print("The line is currently: ", end ="")
        while(i<len(list)-1):
            print(f"{i+1}. {list[i]}", end =" ")
            i += 1
        print(f"{i+1}. {list[i]}")
    # return None

def take_a_number(list , name):
    print(f"Welcome, {name}. You are number {len(list) + 1} in line.")
    list.append(name)

def now_serving(list):
    if (len(list)>0):

        print(f"Currently serving {list[0]}.")
        list.pop(0)
    else:
        print("There is nobody waiting to be served!")