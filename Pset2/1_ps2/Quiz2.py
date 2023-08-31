s1 = "003"
s2 = "2"
works = True

for i in range(len(s1)):
    if s1[i] not in "0123456789":
        if s1[i] == "." and s1[i-1] != ".":
            works = True
        else:
            works = False

            
for i in range(len(s2)):
    if s2[i] not in "0123456789":
        if s2[i] == "." and s2[i-1] != ".":
            works = True
        else:
            works = False
            
if works == True:
    print(float(s1)*float(s2))
