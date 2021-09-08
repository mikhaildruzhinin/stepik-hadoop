import sys


def main():
    for line in sys.stdin:
        for word in line.strip().split(' '):
            if not word:
                continue
            print(word, 1, sep='\t')


if __name__ == '__main__':
    main()
