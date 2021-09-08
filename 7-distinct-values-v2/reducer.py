import sys


def main():
    categories = []
    d = {}
    for line in sys.stdin:
        category = line.strip()
        if category in categories:
            continue
        categories.append(category)
    for category in categories:
        category = category.split('\t')[-1]
        if not d.get(category, None):
            d[category] = 0
        d[category] += 1
    for category, value in d.items():
        print(category, value, sep='\t')


if __name__ == '__main__':
    main()
