import numpy
import sys

A = None

def make_matrix(p, t, mode=1):
    global A
    if mode == 1: # Identity matrix
        A = [[0 for _ in xrange(len(p))] for _ in xrange(len(p))]
        for i in xrange(len(p)):
            A[i][i] = 1
    elif mode == 2: # Deriving the matrix from the password, not being used, in development
        A = [[0 for _ in xrange(len(p))] for _ in xrange(len(p))]
        for i in xrange(len(t)):
            idx = i % len(p)
            A[idx][0] = ord(t[i]) % 2

def matrix_multiplication(A, B, MOD=127):
    C = [0 for _ in xrange(len(A))]
    for i in xrange(1): # A vector
        for j in xrange(len(B[0])):
            for k in xrange(len(A)):
                C[j] += A[k] * B[k][j]
                C[j] %= MOD
    return C

def enc(m, t, MOD=127):
    global A
    make_matrix(m, t)
    p = [ord(c) % MOD for c in m]
    p = matrix_multiplication(p, A)
    p = [0] + p
    l = [0 for _ in xrange(len(p))]
    t = [ord(c) % MOD for c in t]
    assert len(p) == len(l)

    x = central_map_enc(p, t, l)[1:]
    x = matrix_multiplication(x, A)
    return x

def dec(c, t, MOD=127):
    global A
    make_matrix(c, t)
    c = [ord(y) % MOD for y in c]
    c = matrix_multiplication(c, A)
    c = [0] + c
    p = [0 for _ in xrange(len(c))]
    l = [0 for _ in xrange(len(c))]
    t = [ord(y) % MOD for y in t]
    assert len(p) == len(l) == len(c)

    x = central_map_dec(c, p, t, l)[1:]
    x = matrix_multiplication(x, A)
    return x

def central_map_enc(p, t, l, MOD=127):
    for i in xrange(len(t)):
        if i % 2 == 0:
            l[1] = (p[1] + t[i]) % MOD
            l[2] = (p[2] + p[1] * l[1]) % MOD
            l[3] = (p[3] + p[1] * l[2]) % MOD
            for j in xrange(4, len(p)):
                if j % 4 == 3 or j % 4 == 2:
                    l[j] = (p[j] + p[1] * l[j - 2]) % MOD
                else:
                    l[j] = (p[j] + p[j - 2] * l[1]) % MOD
        else:
            p[1] = (l[1] + t[i]) % MOD
            p[2] = (l[2] - p[1] * l[1]) % MOD
            p[3] = (l[3] - p[1] * l[2]) % MOD
            for j in xrange(4, len(p)):
                if j % 4 == 3 or j % 4 == 2:
                    p[j] = (l[j] - p[1] * l[j - 2]) % MOD
                else:
                    p[j] = (l[j] - p[j - 2] * l[1]) % MOD
    if len(t) % 2 == 0:
        return p
    return l

def central_map_dec(c, p, t, l, MOD=127):
    if len(t) % 2 == 0:
        r = 0
        p = c
    else:
        r = 1
        l = c
    for i in xrange(len(t) - 1, -1, -1):
        if r == 0:
            l[1] = (p[1] - t[i]) % MOD
            l[2] = (p[2] + p[1] * l[1]) % MOD
            l[3] = (p[3] + p[1] * l[2]) % MOD
            for j in xrange(4, len(c)):
                if j % 4 == 3 or j % 4 == 2:
                    l[j] = (p[j] + p[1] * l[j - 2]) % MOD
                else:
                    l[j] = (p[j] + p[j - 2] * l[1]) % MOD
            r = 1
        else:
            p[1] = (l[1] - t[i]) % MOD
            p[2] = (l[2] - p[1] * l[1]) % MOD
            p[3] = (l[3] - p[1] * l[2]) % MOD
            for j in xrange(4, len(c)):
                if j % 4 == 3 or j % 4 == 2:
                    p[j] = (l[j] - p[1] * l[j - 2]) % MOD
                else:
                    p[j] = (l[j] - p[j - 2] * l[1]) % MOD
            r = 0
    return p

def main():
    if len(sys.argv) != 4:
        print 'Usage: python csci462.py <encrypt/decrypt> <input_file> <output_file>'
        print 'Example: python csci462.py encrypt input.txt file.enc'
        print 'Example: python csci462.py decrypt file.enc plaintext.txt'
        exit(1)
    if sys.argv[1] == 'encrypt':
        t = raw_input("Password: ").strip()
        m = open(sys.argv[2]).read()
        x = enc(m, t)
        f = open(sys.argv[3], 'wb')
        f.write(''.join([chr(c) for c in x]))
        f.close()
        print 'Data encrypted and saved to {}'.format(sys.argv[3])
    elif sys.argv[1] == 'decrypt':
        t = raw_input("Password: ").strip()
        c = open(sys.argv[2]).read()
        x = dec(c, t)
        f = open(sys.argv[3], 'wb')
        f.write(''.join([chr(y) for y in x]))
        f.close()
        print 'Data decrypted and saved to {}'.format(sys.argv[3])
    else:
        print 'Usage: python csci462.py <encrypt/decrypt> <input_file> <output_file>'
        print 'Example: python csci462.py encrypt input.txt file.enc'
        print 'Example: python csci462.py decrypt file.enc plaintext.txt'
        exit(1)

if __name__ == '__main__':
    main()