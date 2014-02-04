from carshare import ccar

__author__ = 'far'

import unittest


class TestCar(unittest.TestCase):
#    def test_f(self):
#        self.fail()

    def test_model(self):
        self.assertEqual("Golf", "Golf")

    def test_printcarname(self):
        v1 = ccar.car
        v2 = v1.printcarname(self)


        self.assertEqual("Golf", v2)




if __name__ == '__main__':
    unittest.main()
