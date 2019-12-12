total = 0
accounts = {
5324334: (5324334, 10000, 0.02),
2434343: (2434343, 80000, 0.01),
5234343: (5234343, 30000, 0.02)
}
total += accounts.get(5324334)[1]
total += accounts.get(2434343)[1]
total += accounts.get(5234343)[1]
print(total)
