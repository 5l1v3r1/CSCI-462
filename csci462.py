import sympy

def enc(m, t):
    pass

def dec(c, t):
    pass

def central_map(p, t, l, MOD=127):
    for i in xrange(len(t)):
        if i % 2 == 0:
            l[1] = (p[1] + t[i]) % MOD
            l[2] = (p[2] + p[1] * l[1]) % MOD
            l[3] = (p[3] + p[1] * l[2]) % MOD
            for j in xrange(4, len(p) + 1):
                if j % 4 == 3 or j % 4 == 2:
                    l[j] = (p[j] + p[1] * l[j - 2]) % MOD
                else:
                    l[j] = (p[j] + p[j - 2] * l[1]) % MOD
        else:
            p[1] = (l[1] + t[i]) % MOD
            p[2] = (l[2] - p[1] * l[1]) % MOD
            p[3] = (l[3] - p[1] * l[2]) % MOD
            for j in xrange(4, len(p) + 1):
                if j % 4 == 3 or j % 4 == 2:
                    p[j] = (l[j] - p[1] * l[j - 2]) % MOD
                else:
                    p[j] = (l[j] - p[j - 2] * l[1]) % MOD

def central_map_dec(c, p, t, l, MOD=127):
    if len(t) % 2 == 0:
        r = 0
        p = c
    else:
        r = 1
        l = c
    for i in xrange(len(t), -1, -1):
        if r == 0:
            l[1] = (p[1] - t[i]) % MOD
            l[2] = (p[2] + p[1] * l[1]) % MOD
            l[3] = (p[3] + p[1] * l[2]) % MOD
            for j = xrange(4, len(c) + 1):
                if j % 4 == 3 or j % 4 == 2:
                    l[j] = (p[j] + p[1] * l[j - 2]) % MOD
                else:
                    l[j] = (p[j] + p[j - 2] * l[1]) % MOD
            r = 1
        else:
            p[1] = (l[1] - t[i]) % MOD
            p[2] = (l[2] - p[1] * l[1]) % MOD
            p[3] = (l[3] - p[1] * l[2]) % MOD
            for j in xrange(4, len(c) + 1):
                if j % 4 == 3 or j % 4 == 2:
                    p[j] = (l[j] - p[1] * l[j - 2]) % MOD
                else:
                    p[j] = (l[j] - p[j - 2] * l[1]) % MOD
            r = 0

def main():
    while True:
        pass

if __name__ == '__main__':
    main()