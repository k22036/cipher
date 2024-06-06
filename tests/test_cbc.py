import unittest
from src.cbc import encrypt, decrypt

import random, string


def random_str(n):
    randlst = [random.choice(string.ascii_letters) for i in range(n)]
    return ''.join(randlst)


class TestCBC(unittest.TestCase):
    def test_encrypt_decrypt(self):
        for i in range(100):
            text = random_str(100)
            key = random.randint(1, 26)
            self.assertEqual(text, decrypt(encrypt(text, key), key))
