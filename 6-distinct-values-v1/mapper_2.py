import sys


def main():
    for line in sys.stdin:
        value, group = line.strip().split(',')
        print(group, 1, sep='\t')
            


if __name__ == '__main__':
    main()
