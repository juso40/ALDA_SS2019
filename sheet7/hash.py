def hhash(s):
    h = 0
    for k in s:
        h = 23 * h + ord(k)
    return h



"""
Vorgehensweise für 2 buchstaben bsp:
print(hhash("sa"))
sa => (23 * 115) + 97
s = 115
a = 97
=> (23 * x_1) + x_2 = 2742
=> 23 * x_1 = 2742 - x_2

for x in range(300):
    a = (2742 - x)/23
    if a.is_integer():
        a = int(a)
        print(chr(a),chr(x))
"""
print(hhash("AzWo"))
"""
AzWo
A 65 0
z 122 65
W 87 1617
o 111 37278

h = 857505
=> (((((((23 * 0) + A) * 23) + z) * 23) + W) * 23) + o)
(((((65*23)+122)*23)+87)*23)+111 = 857505

((A*23+z)*23+W)*23+o = 857505
=> ((A*23+z)*23+W) = (857505-o)/23
=> (A*23+z) = (((857505-o)/23)-W)/23
=> A = (((((857505-o)/23)-W)/23)-z)/23

"""

"""
To make this code work with any generated hash from the hhas() funciton
simply replace the value for "MyHash" with your own
generated hash of a strig of the lenght of 4
"""
MyHash=857505

f = open("collisions.txt", "w+")
for A in range(64, 123):
    for z in range(64, 123):
        for W in range(64, 123):
            for o in range(64, 123):
                solution = (((((MyHash-o)/23)-W)/23)-z)/23-A
                if solution.is_integer and solution == 0:
                    print(chr(A), chr(z), chr(W), chr(o))
                    s = chr(A) + chr(z) + chr(W) + chr(o)
                    f.write("String: " + s + " Hash: " + str(hhash(s))+ "\n")
