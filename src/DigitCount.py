#input number
i=455466
#final result
count = 10
#outer loop (runs till count is a single digit number)
while(count>9):
    count = 0
    #inner loop (each round of digit count is done here)
    while(i>0):
        count = count+(i%10)
        i=int(i/(10))
    i=count
#sum of all digits
print(count)
#verrification of the answer
print(i%9)
