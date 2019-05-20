import timeit
import copy

##########################
#    standard version    #
##########################
initialisation = '''
size=100
A,B = [k for k in range(size*size)], [k for k in range(size*size)]
C = [0 for k in range(size*size)]
'''
code_to_be_measured = '''
for i in range(size):
    for j in range(size):
        for k in range(size):
            C[i + j*size] += A[i + k*size] * B[k + j*size]
'''

repeats = 10 # repeat the test so many times
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time_standard = min(t.repeat(repeats, 1))
print("standard execution time:", (time_standard*1000), "ms")


##########################
#    optimized version   #
##########################
'''
Durch das ersetzen von j*size in dem array durch die neue Variable
j_size wird die anzahl der benötigten Multiplikationen verringert.
Ausserdem kann man die Häufigkeit der Indexzugriffen auf C minimieren indem
man eine neue Variable hinzufügt.
'''
initialisation = '''
size=100
A,B = [k for k in range(size*size)], [k for k in range(size*size)]
C = [0 for k in range(size*size)]
'''
code_to_be_measured = '''
for i in range(size):
    for j in range(size):
        j_size=j*size
        temp = 0
        for k in range(size):
            temp += A[i + k*size] * B[k + j_size]
        C[i + j_size] = temp
'''

repeats = 10 # repeat the test so many times
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())
time_optimized = min(t.repeat(repeats, 1))
print("optimized execution time:", (time_optimized*1000), "ms")
print("The optimized implementation is:", (float(100)-100*float(time_optimized)/float(time_standard)), "% faster!")
