from panama.src.session import entry

import sys


def main() -> int:
    """
    Docstring for main
    
    :return: exit code
    :rtype: int
    """

    
    entry.run()
    return 0
    

if __name__ == '__main__':
    sys.exit(main())