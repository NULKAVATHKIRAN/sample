def decor(func):
    def inner():
        value = func()
        return value+2
    return inner

@decor
def value():
    return 10


def generator():
    for i in range(1,11):
        yield i

def sample():
    yield "A"
    yield "B"
    yield "C"

temp=sample() 
print(next(temp))
print(next(temp))
print(next(temp))

