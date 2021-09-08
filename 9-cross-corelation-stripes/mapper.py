import sys


def main():
    for line in sys.stdin:
        elements = line.strip().split(' ')
        for i in elements:
            d = {}
            for j in elements:
                if i == j:
                    continue
                if not d.get(j, None):
                    d[j] = 0
                d[j] += 1
            d = str(d).strip(r'\{\}').replace('\'','').replace(' ','')
            print(i, d, sep='\t')


if __name__ == '__main__':
    main()
