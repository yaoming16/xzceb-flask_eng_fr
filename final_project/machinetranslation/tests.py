import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(englishToFrench)
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertNotEqual(englishToFrench("Hello"),None)

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(frenchToEnglish)
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertNotEqual(englishToFrench("Bonjour"),None)

unittest.main()