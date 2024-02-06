import unittest

def sign(value):
    if value < 0:
        return -1
    else:
        return 1
    
class TestSign(unittest.TestCase):

    def test_sign_negative(self):
        self.assertEqual(sign(-3), -1)

    def test_sign_positive(self):
        self.assertEqual(sign(19), 1)

    def test_sign_zero(self):
        self.assertEqual(sign(0), 0)

    def test_sign_error(self):
        self.assertEqual(sgn(1), 1)


if __name__=='__main__':
	unittest.main()
