from random import randint
list1 = []
def generating_list():
    i = 0
    while i < 16:
        a = randint(1, 8)
        
        if list1.count(a) < 2:
            list1.append(a)
            i += 1
    return list1

def return_value(index):
    return list1[index]

generating_list()

if __name__ == "__main__":
    print(list1)