import sys


def main():
    results = []
    for line in sys.stdin:
        result = line.strip().split('\t')[0]
        if result in results:
            continue
        results.append(result)
        print(result)


if __name__ == '__main__':
    main()
