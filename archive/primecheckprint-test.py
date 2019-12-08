num = 50
x = num

while(x != 0):
    if num%x == 0:
        if num*x == x:
            print(x, "====>", "is prime")
            x -= 1
    else:
        print(f"{x} ====> not a prime.")
        x -= 1
