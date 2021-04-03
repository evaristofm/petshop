from django.test import TestCase


class UrlTest(TestCase):
    
    def test_index_page(self):
        response = self.client.get("/pets/")
        self.assertEqual(response.status_code, 200)



    
