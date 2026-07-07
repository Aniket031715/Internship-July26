Num = ['','','','','']
sort = ['','','','','']

for i in range(len(Num)):
    print("Please enter number ",i," : ",)
    x = float(input())
    Num[i] = x

print(Num)

Max = 0

for i in range(0,5):
    if Num[i] >= Max:
        Max = Num[i]

for i in range(0,5):
    if Max == Num[i]:
        Num[i] = 0
        
print("Maximum Number is: ", Max)

sort[4] = Max
Max = 0

for i in range(0,5):
    if Num[i] >= Max:
        Max = Num[i]

for i in range(0,5):
    if Max == Num[i]:
        Num[i] = 0

sort[3] = Max
Max = 0

for i in range(0,5):
    if Num[i] >= Max:
        Max = Num[i]

for i in range(0,5):
    if Max == Num[i]:
        Num[i] = 0

sort[2] = Max
Max = 0

for i in range(0,5):
    if Num[i] >= Max:
        Max = Num[i]

for i in range(0,5):
    if Max == Num[i]:
        Num[i] = 0

sort[1] = Max
Max = 0

for i in range(0,5):
    if Num[i] >= Max:
        Max = Num[i]

for i in range(0,5):
    if Max == Num[i]:
        Num[i] = 0

sort[0] = Max
Max = 0

print(sort)
