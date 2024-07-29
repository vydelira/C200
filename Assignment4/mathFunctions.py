def aForLoop(n):
    n = 3
    if n == 1:
        return n
    else:
        for i in range(0, n - 1):
            n = (2 * n) + 5
        return n

def aWhileLoop(n):
    wn = 3
    if n == 1:
        return 3
    else:
        while (0 < n - 1):
            wn = (2 * wn) + 5
            n = (n - 1) 
        return wn

def aRecursive(n):
    if n == 1:
        return 3
    else:
        return ((2 * aRecursive(n - 1)) + 5)




def hForLoop(n):
     ar = 0
     at = 3
     if n == 0:
         return 0
     elif n == 1:
         return at
     else:
         for i in range(0, n - 1):
             ay = at
             at = at + (2 * ar)
             ar = ay
         return at


def hWhileLoop(n):
    ar = 0
    at = 3
    if n == 0:
        return 0
    elif n == 3:
        return 3
    else:
        while(0 < n - 1):
            ay = at
            at = at + (2 * ar)
            ar = ay
        return at

def hRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    else: 
        return (hRecursive(n - 1) + (2 * hRecursive(n - 2)))




def eForLoop(n):
    if n == 0:
        return 1
    else:
        for i in range(0, n - 1):
            n = (2 * (n - 1)) + 2
    return n


def eWhileLoop(n):
    en = 1
    if n == 0:
        return 1
    else:
        while(0 < n - 1):
            en = (2 * (en - 1)) + 2
            n = (n - 1)
        return en


def eRecursive(n):
    if n == 0:
        return 1
    else:
        return((2 * eRecursive(n - 1)) + 2)



