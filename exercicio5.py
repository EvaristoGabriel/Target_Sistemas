string = "pneumoultramicroscopicossilicovulcanoconiótico"
string_inversa = ""

for i in range(len(string)-1, -1,-1):
    string_inversa += string[i]

print(f"String utilizada: {string}")
print(f"String invertida: {string_inversa}")
