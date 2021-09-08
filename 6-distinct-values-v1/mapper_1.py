import sys


def main():
    for line in sys.stdin:
        value, groups = line.strip().split('\t')
        for group in groups.split(','):
            print(f'{value},{group}\t1')
            


if __name__ == '__main__':
    main()
