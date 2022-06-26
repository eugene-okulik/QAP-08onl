def enum(s_s):
    a_a = list(s_s)
    c_c = []
    for let in a_a:
        if let not in c_c:
            c_c.append(let)
    result = ""
    for let in c_c:
        if s_s.count(let) == 1:
            result += let
        else:
            result += let + str(s_s.count(let))
    return result


print(enum("abeehhhhhccced"))
