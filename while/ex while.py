# 1
#  x = 0
#  while x < 20:
#      x += 1
#      if x % 2 != 0:
#          print(x)

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






