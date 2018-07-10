# file: p1-trivium.py
# author: Duc Phan - ddp3945@rit.edu
# description: trivium cipher keystream generator


def genKeyStream(iv, key, nClocks=1152):
    lenA = 93
    lenB = 84
    lenC = 111
    A = '-' + iv + '0' * (lenA - len(iv))
    B = '-' + key + '0' * (lenB - len(key))
    C = '-' + '0' * (lenC - 3) + '111'

    stream = []
    for _ in range(nClocks):
        outputA = int(A[91]) & int(A[92])
        outputA ^= int(A[93])
        outputA ^= int(A[66])

        outputB = int(B[82]) & int(B[83])
        outputB ^= int(B[84])
        outputB ^= int(B[69])

        outputC = int(C[109]) & int(C[110])
        outputC ^= int(C[111])
        outputC ^= int(C[66])

        stream.append(str(outputA ^ outputB ^ outputC))
        A = '-' + str(int(A[69]) ^ outputC) + A[1:-1]
        B = '-' + str(int(B[78]) ^ outputA) + B[1:-1]
        C = '-' + str(int(C[87]) ^ outputB) + C[1:-1]

    return ''.join(stream)


def main():
    print genKeyStream('0' * 80, '0' * 80, 70)


if __name__ == '__main__':
    main()
