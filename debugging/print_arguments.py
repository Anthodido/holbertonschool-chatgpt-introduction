#!/usr/bin/python3
import sys

def main() -> int:
    print(sys.argv[0])
    for arg in sys.argv[1:]:
        print(arg)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())