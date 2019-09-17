import unittest
import os
import Compile


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
        self.returned_path = Compile.compile(self.path)

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
        if os.path.exists(self.expected_output_path):
            os.remove(self.expected_output_path)


if __name__ == '__main__':
    unittest.main()
