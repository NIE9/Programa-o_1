def hammig(s, t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count

s = []
t = []
for x in range(0, 17):
    s.append(input("Cadeia s:"))
for y in range(0, 17):
    t.append(input("Cadeia t:"))

print(hammig(s, t))
