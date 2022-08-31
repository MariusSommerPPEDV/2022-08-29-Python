import unittest
# Hier wird das unittest moduil importiert

# Die Testklasse selber muss vom TestCase erben
class TestRandomClass(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
