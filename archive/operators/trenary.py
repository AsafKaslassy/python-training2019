a = 3
b = 4

helloval = "hello" if b > a else "salam"
haifa = 'haifa' if b > a and b > 0 else 'ramat-gan'
rehovot = 109 if a > b else 'rehovot'
telaviv = 'tel-aviv' if 'a' in ['a', 'b', 'c', 'd'] else 'rehovot'
rehovot2 = 'tel-aviv' if 'a' in 'abcd' else 'rehovot'
color = 'blue' if 'b' not in "mosh" else 'red'
winter = 'winter' if a > 2 and a % 2 == 1 else "summer"
yahoo = 123 if 'y' not in 'yahoo' else 'x'

print(helloval)
