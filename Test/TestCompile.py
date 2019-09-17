import unittest
import os
from Src import Compile


class SimpleIntReturnCase(unittest.TestCase):
    path: str = 'return_2.c'
    input_contents: str = """int main(){
    return 2;
}"""
    expected_output_path: str = 'return_2.s'
    expected_output_contents: str = """.global main
main:
        movl    $2, %eax
        ret
"""
    returned_path: str

    def setUp(self):
        # Create simple c file
        file = open(self.path, "w+")
        file.write(self.input_contents)
        file.close()

        # Run the program on it
        self.returned_path = Compile.compile_c(self.path)

    def test_name_matches(self):
        self.assertEqual(self.returned_path, self.expected_output_path, "Should output a .s file with same name")

    def test_output_file_exists(self):
        if not os.path.exists(self.returned_path):
            self.fail(f"The path '{self.returned_path}' could not be found")
        else:
            return

    def test_output_content(self):
        output = open(self.returned_path, "r")
        contents: str = output.read()
        output.close()
        self.assertEqual(contents, self.expected_output_contents, "file contents should match")

    def tearDown(self):
        os.remove(self.path)
        if os.path.exists(self.returned_path):
            os.remove(self.returned_path)


class SimpleIntReturnCaseAlternate(SimpleIntReturnCase):
    path: str = 'return_3.c'
    input_contents: str = """int main(){
        return 3;
    }"""
    expected_output_path: str = 'return_3.s'
    expected_output_contents: str = """.global main
    main:
            movl    $3, %eax
            ret
    """


if __name__ == '__main__':
    unittest.main()
