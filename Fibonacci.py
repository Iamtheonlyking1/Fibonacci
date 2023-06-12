num = int(input("How many numbers: "))

n1 =  0
n2 = 1
count = 0

if num <= 0:
    print("ERROR")
elif num == 1:
    print(n1)
else:
    while count < num:
        print(n1)
        x = n1 + n2
        n1 = n2
        n2 = x
        count += 1
        
