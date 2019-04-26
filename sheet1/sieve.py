from math import sqrt
def sieve(sieve_up_to):
    sieve_up_to=int(sieve_up_to)
    is_prime = [True] * sieve_up_to #jede zahl ist eine potentielle primzahl
    is_prime[0],is_prime[1]=False,False #0 und 1 sind keine Primzahlen

    for n in range(2, int(sqrt(sieve_up_to)+1)):    #bei 2(der erstenprimzahl) fängt man an
        if is_prime[n]: #wenn eine primzahl da ist, dann:
            for l in range (n * n, sieve_up_to, n): #range(x,y, Schrittgröße)
                is_prime[l]=False   #jedes echt vielfache von n ist keine prime
    #for i in range (len(is_prime)):
    #    print(i,"is prime",is_prime[i])
    prime_numbers = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_numbers.append(i)
    return prime_numbers

#up_to = input("Please enter the number to search up to for primes using the sieve:")
#sieve(up_to)
