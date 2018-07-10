# file: p3-RC4Cracker.py
# author: Duc Phan - ddp3945@rit.edu
# description: This crypto is broken. Do not use it. Please!

p1 = 'BARACKOBAMA'
c1 = '01000011 00011011 00010010 00110000 11111000 10100111 10001110 11101001 00010100 00011101 01100100'
n1 = 1

c2 = '01000110 00010100 00001111 00110011 11110000 10101001 10010110 11111110 00000011 00011100 01110110'
n2 = 2


def xor(s1, s2):
    return ''.join([chr(ord(a) ^ ord(b)) for (a, b) in zip(s1, s2)])


def bitsToStr(s):
    return ''.join([chr(int(x, 2)) for x in s.split(' ')])


def calKeystreamReverse(p, c):
    return xor(p, c)


def calScrambleEggs(n, ks):
    return ''.join([chr((ord(x) - n + 256) % 256) for x in ks])


def calKeystreamForward(n, eggs):
    return ''.join([chr((ord(x) + n) % 256) for x in eggs])


def calPlaintext(ks, c):
    return xor(ks, c)


def main():
    global p1, c1, n1, n2, c2
    c1 = bitsToStr(c1)
    c2 = bitsToStr(c2)
    ks1 = calKeystreamReverse(p1, c1)
    eggs = calScrambleEggs(n1, ks1)
    ks2 = calKeystreamForward(n2, eggs)
    p2 = calPlaintext(ks2, c2)
    print 'Your cipher is broken: {}'.format(p2)


if __name__ == '__main__':
    main()
