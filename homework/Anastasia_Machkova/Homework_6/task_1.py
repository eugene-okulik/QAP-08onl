def enum(s):
    a = list(s)
    c = []
    for let in a:
        if not let in c:
            c.append(let)
    result = ""
    for let in c:
        if s.count(let) == 1:
            result += let
        else:
            result += let + str(s.count(let))
    return result


print(enum("abeehhhhhccced"))
