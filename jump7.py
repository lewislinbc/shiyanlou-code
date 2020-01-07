while n < 100:
    n = n+1
    if n % 7 == 0:
        continue
    elif n % 10 == 7:
        continue
    elif n // 10 == 7:
        continue
    elif n == 100:
       break 
    else:
       print(n)
    
