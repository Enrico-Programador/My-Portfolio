import unittest

from src.generate_page import extract_title

class TestExtractFile(unittest.TestCase):
    def test_extract_file(self):
        md = '''


# first heading

text 

'''

        print(extract_title(md))
        self.assertEqual(extract_title(md), "first heading")



if __name__ == "__main__":
    unittest.main()