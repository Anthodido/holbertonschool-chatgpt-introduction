#!/usr/bin/python3
import sys

def main() -> int:
    for arg in sys.argv:
        print(arg)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())