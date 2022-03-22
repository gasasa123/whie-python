# 1
 x = 0
 while x < 20:
     x += 1
     if x % 2 != 0:
         print(x)

# 2
guessnum=int(input("please choose numbetween 1 -1000:"))
start=1
end=1000
middle =(start+end)//2
print("start=",start,"middle=",middle,"end=",end,"number=",guessnum)
while guessnum!=middle:
    middle = (start+end)//2
    if guessnum>middle:
        start=middle
        print("start=",start,"end=",end,"number=",guessnum)
    else:
        end=middle
        print("start=",start,"end=",end,"number=",guessnum)
print("found",guessnum)

# 3
n = 0
sum = 0
p = 1
while n < 32:
    sum += n
    if (sum >= 20) and (p == 1):
        print(n)
        p = True
        n += 1
        print(sum)

# 4
a = int(input("please enter your grade:"))
while a != 100:
    print("Retest exam")
    a = int(input("please enter your grade:"))
if a == 100:
    print("your the king")
num = 0
a = int(input("please enter number:"))
while a != 10:
    a = int(input("please enter number:"))
if a == 10:
    print(pow(a, 2))






