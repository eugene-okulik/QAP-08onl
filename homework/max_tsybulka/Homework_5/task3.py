# Подсчет букв
# Дано две переменные: строка и буква => "fizbbbuz","b",
# нужно подсчитать сколько раз буква b встречается в заданной строке
# Примеры результатов:
# "Hello there", "e" == 3
# "Hello there", "t" == 1
# "Hello there", "h" == 2
# "Hello there", "L" == 2
# "Hello there", " " == 1

A = "fizbbbbbuz"
B = "b"
C = "f"
D = "z"
E = "u"
F = "i"
J = " "

print('"fizbbbbbuz"', '"b"', '==', A.count(B))
print('"fizbbbbbuz"', '"f"', '==', A.count(C))
print('"fizbbbbbuz"', '"z"', '==', A.count(D))
print('"fizbbbbbuz"', '"u"', '==', A.count(E))
print('"fizbbbbbuz"', '"i"', '==', A.count(F))
print('"fizbbbbbuz"', '" "', '==', A.count(J))
