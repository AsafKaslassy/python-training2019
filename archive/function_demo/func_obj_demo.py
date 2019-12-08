def doSomething():
    print("gaga")


doSomething.author = "Dima Banny"
doSomething.version = "1.0.1"

temp = doSomething

temp()
print(doSomething.version)
