# Unpacking Dictionary

def f(a,b,c):
    print('Type A:',type(a),', Value: ',a)
    print('Type B:',type(b),', Value: ',b)
    print('Type C:',type(c),', Value: ',c)
    return a + b < c and a + c > b and b + c > a

ob = {'a': 0,'b': 1, 'c': 2}

num = f(*ob)

print(num)
