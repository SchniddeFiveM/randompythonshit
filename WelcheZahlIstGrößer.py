
def maximum(x, y):
    if x < y:
        return y
    else:
        return x


x = input("Gebe deine erste Zahl ein: ")
y = input("Gebe deine zweite Zahl ein: ")

result = maximum(x, y)
print(result)