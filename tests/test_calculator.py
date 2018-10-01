from .context import helpers

import unittest

class BasicTest(unittest.TestCase) :
    def addtest(self) :
        
        assert 10 == helpers.add(4,6)


if __name__ == '__main__':
    unittest.main()