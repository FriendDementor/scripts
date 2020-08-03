import unittest
import subprocess

class TestBase64Decode(unittest.TestCase):

    def test_void(self):
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.check_output(["python3", "b64enc.py"], stderr=subprocess.STDOUT)

    def test_unique(self):
        s = 'a'
        e = b'YQ=='
        out = subprocess.check_output(["python3", "b64enc.py", s])[:-1]
        self.assertEqual(out, e)

    def test_simple(self):
        s = 'hello world'
        e = b'aGVsbG8gd29ybGQ='
        out = subprocess.check_output(["python3", "b64enc.py", s])[:-1]
        self.assertEqual(out, e)
    
    def test_large(self):
        s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque molestie maximus urna, molestie volutpat leo tincidunt sit amet.'
        e = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gUGVsbGVudGVzcXVlIG1vbGVzdGllIG1heGltdXMgdXJuYSwgbW9sZXN0aWUgdm9sdXRwYXQgbGVvIHRpbmNpZHVudCBzaXQgYW1ldC4='
        out = subprocess.check_output(["python3", "b64enc.py", s])[:-1]
        self.assertEqual(out, e)

    def test_utf8(self):
        s = "¥ · £ · € · $ · ¢ · ₡ · ₢ · ₣ · ₤ · ₥ · ₦ · ₧ · ₨ · ₩ · ₪ · ₫ · ₭ · ₮ · ₯ · ₹".encode('utf-8')
        e = b'wqUgwrcgwqMgwrcg4oKsIMK3ICQgwrcgwqIgwrcg4oKhIMK3IOKCoiDCtyDigqMgwrcg4oKkIMK3IOKCpSDCtyDigqYgwrcg4oKnIMK3IOKCqCDCtyDigqkgwrcg4oKqIMK3IOKCqyDCtyDigq0gwrcg4oKuIMK3IOKCryDCtyDigrk='
        out = subprocess.check_output(["python3", "b64enc.py", s])[:-1]
        self.assertEqual(out, e)


if __name__ == '__main__':
    unittest.main()