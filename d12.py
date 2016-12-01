import sys, re

def main():
    print sum(map(int, re.findall(r'(\-?\d+)', open(sys.argv[1]).read()))) #lol

if __name__ == "__main__":
    main()