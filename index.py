import random

arr1 = []
for x in range(1, 66): 
    num1 = random.randrange(1, 100)
    arr1.append(num1)
f = open("pali.csv", "a")
for x in range(len(arr1)):
    num2 = [int(i) for i in str(arr1[x])]
    if(num2[0] == num2[len(num2)-1]):
        f.write("A Palidrome\n")
    else:
        f.write("Not a Palidrome\n")
f.close()
f = open("pali.csv", "r")
print(f.read())
