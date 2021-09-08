import sys


def main():
    prev_key = None
    sum_ = 0
    count = 0
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        value = int(value)
        if prev_key and prev_key != key:
            print(prev_key, sum_ // count, sep='\t')
            sum_ = value
            count = 1
        else:
            sum_ += value
            count += 1            
        prev_key = key
    if prev_key:
        print(prev_key, sum_ // count, sep='\t')


if __name__ == '__main__':
    main()
