from django.test import SimpleTestCase
import json

class accountProfileView(SimpleTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/user/get/Yeet')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        user = content['data']['name']
        self.assertEqual(user,'Yeet')
        email = content['data']['email']
        self.assertEqual(email,'yeet@yahoo.com')

    def test_login_success(self):
        response = self.client.get('user/login/Yeet')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        success = content['success']
        self.assertEqual(success, True)
        userName = content['data']['username']
        self.assertEqual(userName, 'Yeet')
    
    def test_login_incorrect_username(self):
        response = self.client.get('user/login/eebydeeby')
        content = json.loads(response.content)
        success = content['success']
        self.assertEqual(success, False)