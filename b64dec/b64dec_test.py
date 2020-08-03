import unittest
import subprocess

class TestBase64Decode(unittest.TestCase):

    def test_void(self):
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.check_output(["python3", "b64dec.py"], stderr=subprocess.STDOUT)

    def test_unique(self):
        s = 'YQ=='
        e = b'a'
        out = subprocess.check_output(["python3", "b64dec.py", s])[:-1]
        self.assertEqual(out, e)

    def test_simple(self):
        s = 'aGVsbG8gd29ybGQ='
        e = b'hello world'
        out = subprocess.check_output(["python3", "b64dec.py", s])[:-1]
        self.assertEqual(out, e)
    
    def test_large(self):
        s = 'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gUGVsbGVudGVzcXVlIG1vbGVzdGllIG1heGltdXMgdXJuYSwgbW9sZXN0aWUgdm9sdXRwYXQgbGVvIHRpbmNpZHVudCBzaXQgYW1ldC4='
        e = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque molestie maximus urna, molestie volutpat leo tincidunt sit amet.'
        out = subprocess.check_output(["python3", "b64dec.py", s])[:-1]
        self.assertEqual(out, e)

    def test_utf8(self):
        s = 'wqUgwrcgwqMgwrcg4oKsIMK3ICQgwrcgwqIgwrcg4oKhIMK3IOKCoiDCtyDigqMgwrcg4oKkIMK3IOKCpSDCtyDigqYgwrcg4oKnIMK3IOKCqCDCtyDigqkgwrcg4oKqIMK3IOKCqyDCtyDigq0gwrcg4oKuIMK3IOKCryDCtyDigrk='
        e = "¥ · £ · € · $ · ¢ · ₡ · ₢ · ₣ · ₤ · ₥ · ₦ · ₧ · ₨ · ₩ · ₪ · ₫ · ₭ · ₮ · ₯ · ₹".encode('utf-8')
        out = subprocess.check_output(["python3", "b64dec.py", s])[:-1]
        self.assertEqual(out, e)


if __name__ == '__main__':
    unittest.main()