import sys
from script.functions import *

if __name__ == "__main__":
    result = main(sys.argv)
    if result is not None:
        sys.exit(result)