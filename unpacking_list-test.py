# Unpacking List

def f(y1, y2, x1, x2):
    return (y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1)

ob = [0, 0, 4, 3]

num = f(*ob)

print(num)
