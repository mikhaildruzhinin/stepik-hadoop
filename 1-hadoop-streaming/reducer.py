import sys


def main():
    prev_key = None
    res = 0
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        if prev_key and prev_key == key:
            res += int(value)
        else:
            if prev_key:
                print(prev_key, res, sep='\t')
            res = int(value)
        prev_key = key
    if prev_key:
        print(prev_key, res, sep='\t')


if __name__ == '__main__':
    main()
