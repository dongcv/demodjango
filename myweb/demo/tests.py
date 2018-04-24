from django.test import TestCase , SimpleTestCase
class Simpltestcase(SimpleTestCase):
    def test_home(self):
        reponse = self.client.get('/webapp/')
        self.assertEqual(reponse.status_code, 2001)


