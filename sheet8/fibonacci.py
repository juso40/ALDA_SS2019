import os

def decorator(function):
    def wrapper(N):
        columns, rows = os.get_terminal_size(0)
        print("=" * columns)
        print(function.__name__ + "(" + str(N) + ") = " + str(function(N)))
        print("=" * columns)
        return function(N)
    return wrapper



@decorator
def fib1(n):                      # Funktion berechnet die n-te Fibonacci-Zahl
    if n <= 1:
         return n                 # Rekursionsabschluss
    return fib1(n-1) + fib1(n-2)  # Baumrekursion


@decorator
def fib3Impl(n):
    if n == 0:
        return 1, 0         # gebe die Fibonacci-Zahl von 1 und die davor zurück
    else:                          # rekursiver Aufruf
       # f1 ist Fibonacci-Zahl von n, f2 die von (n-1)
       f1, f2 = fib3Impl(n-1)
       # gebe neue Fibonacci-Zahl fn+1 = f1+f2 und die vorherige (fn = f1) zurück.
       return f1 + f2, f1


@decorator
def fib3(n):
    # Hilfsfunktion, f1 ist die Fibonacci-Zahl von (n+1) und f2 ist die Fibonacci-Zahl von n
    f1, f2 = fib3Impl(n)
    return f2


@decorator
def fib5(n):
    f1, f2 = 1, 0                # f1 ist die Fibonaccizahl für n=1, f2 die für n=0
    while n > 0:
        # berechne die nächste Fibonaccizahl in f1 und speichere die letzte in f2
        f1, f2 = f1 + f2, f1
        n -= 1
    return f2


#fib1(37) # Time limit of 10secs reached

#fib3(996) # fib3(997) throws "RecursionError"

#fib5(1000000) # Time limit of 10secs reached

'''
fib1() ist die Funktion die am längsten dauert, dies kann man darauf zurückführen,
dass sie sich selber jedesmal selber 2-mal selber aufruft. Das bedeutet ausserdem, 
dass sie relativ schnell die maximale Rekursionstiefe erriechen wird.

fib3() benutzt einfache Rekursion. Die Rekursionstiefe ist 
demnach also im gegensatz zu fib1() nur halb so tief.

fib5() setzt komplett auf Iteration anstatt auf Rekursion.
Es wird demnach nie die maximale Rekursionstiefe erreicht.
Ausserdem wird nicht jedesmal neuer Speicher für neue variablen allokiert.


'''



def mul2x2(M1, M2):
    if len(M1) == 4 and len(M2) == 4:
        Result = [
                    M1[0]*M2[0]+M1[1]*M2[2], M1[0]*M2[1]+M1[1]*M2[3], 
                    M1[2]*M2[0]+M1[3]*M2[2], M1[2]*M2[1]+M1[3]*M2[3]
                    ]
        return Result


@decorator
def fib6(N):
    if N == 0:
        return 1
    else:
        M1 = M2 = [1, 1, 1, 0]
        while N > 1:
            M2 = mul2x2(M1, M2)
            N -= 1
    return M2[1]

#fib6(280000) #280000 reaches the time limit of 10 seconds
@decorator
def fib7(N):
    if N == 1:
        return 1
    elif N == 0:
        return 0
    else:
        X = [1, 1, 1, 0]
        if N % 2 == 0:
            X = temp = mul2x2(X, X)   
            for _ in range(1, int(N/2)):    
                temp = mul2x2(temp, X)
            return temp[1]
       
        else:
            X = temp = mul2x2(X, X)
            for _ in range(1, int((N-1)/2)):
                temp = mul2x2(temp, X)
            return mul2x2([1,1,1,0], temp)[1]
        
   
#fib7(360000)  # 360000 reaches the time limit of 10 seconds

for i in range(1000):
    assert(fib5(i) == fib7(i))


