#!/usr/bin/python3
import sys

def main() -> int:
    print(f"Programme: {sys.argv[0]}")
    print("Arguments:")
    for arg in sys.argv[1:]:
        print(f"  - {arg}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())