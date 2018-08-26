def factorial(a):
    if a == 0:
        return 1
    else:
        for i in range(1,a):
            a*=i
        return a

def combinatoria(n,k):
    if n < k:
        return "%d es mayor que %d, no se puede"%(k,n)
    else:
        return float(factorial(n))/(factorial(k)*factorial(n-k))

def coeficiente(n):
    lista = []
    if n==0:
        lista.append(1)
    else:
        for i in range(n+1):
            lista.append(int(combinatoria(n,i)))
    return lista

for i in range(10):
    print coeficiente(i)
