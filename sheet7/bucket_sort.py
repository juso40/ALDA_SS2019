import random
import math
import timeit
import matplotlib.pyplot as plt


def createData(size):
  a = []
  while len(a) < size:
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    r = math.sqrt(x**2 + y**2)
    if r < 1.0:
      a.append(r)
  return a

def insertionSort(a):   # sort 'a' in-place
  N = len(a)          # number of elements

  for i in range(N):
      current = a[i]  # remember the current element
      # find the position of the gap where 'current' is supposed to go
      j = i       # initial guess: 'current' is already at the correct position
      while j > 0:
          if current < a[j-1]:  # a[j-1] should be on the right of 'current'
              a[j] = a[j-1]     # move a[j-1] to the right
          else:
              break             # gap is at correct position
          j -= 1                # shift gap one index to the left
      a[j] = current            # place 'current' into appropriate ga

def bucketMap(r, M):
  return int(r**2 * M)

def naiveBucketMap(r, M):
    return r*m

def bucketSort(a, d):
    N = len(a)
    M = int(N / float(d))  # Anzahl der Buckets festlegen

    # M leere Buckets erzeugen
    buckets = [[] for k in range(M)]

    # Daten auf die Buckets verteilen
    for k in range(len(a)):
        index = bucketMap(a[k], M)     # Bucket-Index berechnen
        buckets[index].append(a[k])    # a[k] im passenden Bucket einfügen

    # Daten sortiert wieder in a einfügen
    start = 0                          # Anfangsindex des ersten Buckets
    for k in range(M):
        insertionSort(buckets[k])      # Daten innerhalb des aktuellen Buckets sortieren
        end = start + len(buckets[k])  # Endindex des aktuellen Buckets
        a[start:end] = buckets[k]      # Daten an der richtigen Position in a einfügen
        start += len(buckets[k])       # Anfangsindex für nächsten Bucket aktualisieren

    return buckets

def chi2Test(bucket_lens,N):
    M=len(bucket_lens)
    c=N/M
    chi2=0
    for k in range(M):
        chi2+=((len(bucket_lens[k])-c)**2)/c
    t=math.sqrt(2*chi2**2)-math.sqrt(2*M-3)
    print(t)
    if(math.sqrt(t**2)>3):
        return False
    else:
        return True

print(chi2Test(bucketSort(createData(22),5),22))



t = []
t_naive = []
size = []
for n in range(1000,10001,1000):
    timer_1 = timeit.Timer(stmt= 'bucketSort',
                            setup = 'from __main__ import insertionSort,'+
                            'bucketSort, bucketMap, createData \n' +
                            'a = createData('+ str(n) + ')\n')
    timer_2 = timeit.Timer(stmt= 'bucketSort',
                            setup = 'from __main__ import insertionSort,'+
                            'bucketSort, naiveBucketMap, createData \n' +
                            'a = createData('+ str(n) + ')\n')
    time_1 = timer_1.repeat(repeat = 10, number = 1)
    time_2 = timer_2.repeat(repeat = 10, number = 1)
    t.append(min(time_1))
    t_naive.append(min(time_2))
    size.append(n)

    plt.xlabel('Anzahl der Elemente')
    plt.ylabel('Laufzeit [s]')
    plt.title('Laufzeit bucketSort')
    plt.axis([0,10100,0,0.008])
    plt.plot(size,t,'ro', label='bucketMap')
    plt.plot(size,t_naive,'b*', label='naiveBucketMap')
    plt.legend(loc='upper left')
    plt.show()
