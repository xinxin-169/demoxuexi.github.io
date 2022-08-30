num = 1
result = 0
while num<=300:
    if num%2!=0:
        if num%7!=0:
            result += num

    num+=1


print(result)

