def test_diff(file1, file2):
    data1 = open(file1).read()
    data2 = open(file2).read()
    cnt = 0
    for i in xrange(len(data1)):
        cnt += (1 if data1[i] != data2[i] else 0)
    return 100.0 * cnt / len(data1)

def main():
    lst = [3, 6, 9, 12, 15]
    for i in xrange(1, 4):
        for x in lst:
            orig = 'original{}.enc'.format(x)
            change = '{}_{}.enc'.format(x, i)
            print x, test_diff(orig, change)

if __name__ == '__main__':
    main()