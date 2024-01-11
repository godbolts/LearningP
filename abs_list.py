def abs_list(a):
    vastus = []
    for i in a:
        if i < 0:
            vastus.append(abs(i))
        else:
            vastus.append(i)
    return vastus

list = [1, 3, -4, 5, -8, -0.5]

print(abs_list(list))