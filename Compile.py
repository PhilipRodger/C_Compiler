import sys


def compile(path: str) -> str:
    return path


if __name__ == '__main__':
    try:
        path: str = sys.argv[1]
        output: str = compile(path)
        print(output)
    except IndexError:
        print("You need to supply a path of the c file you are compiling.")
