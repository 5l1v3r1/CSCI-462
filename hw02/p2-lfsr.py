# file: p2-lfsr.py
# author: Duc Phan - ddp3945@rit.edu
# description: keystream generation using LFSR

def genKeyStream(lfsr, nClocks):
    stream = []
    for _ in range(nClocks):
        stream.append(lfsr[-1])
        lfsr = str(int(lfsr[-3 - 1]) ^ int(lfsr[-0 - 1])) + lfsr[:-1]
    return ''.join(stream)


def main():
    s = genKeyStream('11011', 1 * ( (2 ** 5) - 1 ))
    print s


if __name__ == '__main__':
    main()


