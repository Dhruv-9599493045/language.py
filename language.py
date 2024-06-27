# Import string and random module
import string
import random
while True :
    print('''Do you want to-
        1) Code 
        2) Decode ''')
    start = input("enter the number \n")
    if start == "1" :
        limit = int(input("enter the range of message "))
        value = 0
        while value < limit:
            value += 1
     # Randomly choose a letter from all the ascii_letters
            a = random.choice(string.ascii_letters)
     #print(a)
            b = random.choice(string.ascii_letters)
            #print(b)
            c = random.choice(string.ascii_letters)
            #print(c)
            f = random.choice(string.ascii_letters)
            #print(f)
            g = random.choice(string.ascii_letters)
            #print(g)
            h = random.choice(string.ascii_letters)
            #print(h)
            d = str(input("enter a message "))
            i = d[1:] + d[0]
            e = str(a + b + c + i + f + g + h)
            print(e)
        

        

    else:
        limit = int(input("enter the range of message "))
        value = 0
        while value < limit:
            value += 1
        # Randomly choose a letter from all the ascii_letters
            j = random.choice(string.ascii_letters)
        #print(a)
            k = random.choice(string.ascii_letters)
        #print(b)
            l = random.choice(string.ascii_letters)
        #print(c)
            m = random.choice(string.ascii_letters)
        #print(f)
            n = random.choice(string.ascii_letters)
        #print(g)
            o = random.choice(string.ascii_letters)
        #print(h)
            p = str(input("enter a message "))
            q = p[1:] + p[0]
            r = str(j + k + l + q + m + n + o)
            print(r)


