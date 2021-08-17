import unittest

from String_Calc import Calculator as Calc

class AddTests(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Calc(""), 0)
    
    def test_one_value(self):
        self.assertEqual(Calc("1"), 1)

    def test_two_values(self):
        self.assertEqual(Calc("1,2"), 3)

    def test_unkown_values(self):
        self.assertEqual(Calc("1,2,3,4"), 10)

    def test_newline_delim(self):
        self.assertEqual(Calc("1\n2,3"), 6)

    def test_dif_delim(self):
        self.assertEqual(Calc("//;\n1;2"), 3)

    def test_neg_values(self):
        self.assertEqual(Calc("-5,10,-9"), 'negatives not allowed -5 -9')

    def test_larger_1000(self):
        self.assertEqual(Calc("1001,5"), 5)
        
    def test_any_len_delim(self):
        self.assertEqual(Calc("//[***]\n1***2***3"), 6)

    def test_multi_delim(self):
        self.assertEqual(Calc("//[*][%]\n1*2%3"), 6)

    def test_mulit_len_delim(self):
        self.assertEqual(Calc("//[***][%%%]\n1***2%%%3"), 6)

if __name__== '__main__':
    unittest.main()
