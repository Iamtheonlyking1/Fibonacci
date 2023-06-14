list = []
x = int(input("Size of the list: "))
for i in range(0,x):
    y = int(input("Enter element: "))
    list.append(y)

print("Output: ")
for i in list:
    if i >= 0:
        print(i, end=" ")
