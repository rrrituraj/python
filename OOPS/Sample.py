def f(*x):
    if len(x) == 1:
        return x[0] + 42
    else:
        return x[0] + x[1] + 42
print(f(1 , 4 , 3))