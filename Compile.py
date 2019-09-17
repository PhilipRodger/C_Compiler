import sys

pathOut: str = 'return_2.s'
contents: str = """.global main
main:
        movl    $2, %eax
        ret
"""

def compile(path: str) -> str:
    file = open(pathOut, "w+")
    file.write(contents)
    file.close()
    return pathOut


if __name__ == '__main__':
    try:
        path: str = sys.argv[1]
        output: str = compile(path)
        print(output)
    except IndexError:
        print("You need to supply a path of the c file you are compiling.")
