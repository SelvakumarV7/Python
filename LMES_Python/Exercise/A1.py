n = int(input("Enter a number to form diamond: "))           # range  * count   space count
for i in range(n):                                      # n     i       j       k
    for k in range(n-i-1):                              # 5     0       1       4               j = i+1-->1,  k = n-j-->4       n-(i+1)=n-i-1
        print(' ',end = '')                             # 5     1       2       3
    for j in range(i+1):                                # 5     2       3       2
        print('* ',end='')                              # 5     3       4       1
    print()                                             # 5     4       5       0

                                                             # range  * count   space count
for i in range(n):                                      # n     i       j       k
    for k in range(i):                                  # 5     0       5       0               j = n-i-->5,  k = i             n-(i+1)=n-i-1
        print(' ',end = '')                             # 5     1       4       1
    for j in range(n-i):                                # 5     2       3       2
        print('* ',end='')                              # 5     3       2       3
    print()                                             # 5     4       1       4  