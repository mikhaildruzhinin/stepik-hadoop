import sys


def main():
    d = {}
    for line in sys.stdin:
        for word in line.strip().split(' '):
            if not d.get(word, None):
                d[word] = 0
            d[word] += 1
    for word, sum_ in d.items():
        print(word, sum_, sep='\t')


if __name__ == '__main__':
    main()
