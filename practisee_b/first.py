n = "Java1234"
temp = ""

for i in range(len(n)):
    ch = n[i]
    if ch in "aeiouAEIOU":
        temp += '@'
    elif ch.isdigit() and int(ch) % 2 == 0:
        temp += '*'
    elif ch.islower():
        temp += ch.upper()
    else:
        temp += ch

print(temp)

