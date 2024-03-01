s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = 'qwertyuioplkjhgfdsazxcvbnm'


for index in range(len(s1)):
    for i in (range(len(s2))):
        if s1[index] == s2[i]:
            print(s1[index], end="")
            break

print()
for char in s1:
    print(char)