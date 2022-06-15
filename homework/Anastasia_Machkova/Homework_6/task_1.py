def enum(S):
    A = list(S)
    C = []
    for let in A:
        if not let in C:
            C.append(let)
    result = ""
    for let in C:
        if S.count(let) == 1:
            result += let
        else:
            result += let + str(S.count(let))
    return result


print(enum("abeehhhhhccced"))
