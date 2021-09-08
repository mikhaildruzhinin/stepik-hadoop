import sys


def main():
    for line in sys.stdin:
        elements = line.strip().split(' ')
        for i in elements:
            for j in elements:
                if i == j:
                    continue
                print(f'{i},{j}\t1')


if __name__ == '__main__':
    main()
