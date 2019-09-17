import sys
import os
import _io.TextIOWrapper

contents: str = """.global main
main:
        movl    $2, %eax
        ret
"""


def compile_c(path: str) -> str:
    assembly_path: str = os.path.splitext(path)[0] + ".s"
    file: _io.TextIOWrapper
    with open(assembly_path, "w+") as file:
        file.write(contents)
        return assembly_path


if __name__ == '__main__':
    try:
        path: str = sys.argv[1]
        output: str = compile_c(path)
        print(output)
    except IndexError:
        print("You need to supply a path of the c file you are compiling.")
