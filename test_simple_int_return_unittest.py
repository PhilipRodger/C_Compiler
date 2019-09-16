import unittest
import os
import Compile


class SimpleIntReturnCase(unittest.TestCase):
    path: str = 'return_2.c'
    output_path: str = 'return_2.s'
    returned_path: str

    def setUp(self):
        # Create simple c file
        file = open(self.path, "w+")
        file.write("int main(){\r\n")
        file.write("    return 2;\r\n")
        file.write("}\r\n")
        file.close()

        # Run the program on it
        self.returned_path = Compile.compile(self.path)

    def test_name_matches(self):
        self.assertEqual(self.returned_path, self.output_path, "Should output a .s file with same name")

    def test_simple_int_return(self):
        self.assertEqual(True, False)

    def tearDown(self):
        os.remove(self.path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)


if __name__ == '__main__':
    unittest.main()
