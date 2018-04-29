import sympy
import sys

def enc(m, t):
    p = [0] + [ord(c) for c in m]
    l = [0 for _ in xrange(len(p))]
    t = [ord(c) for c in t]
    assert len(p) == len(l)

    x = central_map_enc(p, t, l)
    return x[1:]

def dec(c, t):
    c = [0] + [ord(y) for y in c]
    p = [0 for _ in xrange(len(c))]
    l = [0 for _ in xrange(len(c))]
    t = [ord(y) for y in t]
    assert len(p) == len(l) == len(c)

    x = central_map_dec(c, p, t, l)
    return x[1:]

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