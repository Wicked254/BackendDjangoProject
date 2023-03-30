from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class QuestionAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_get_questions_list(self):
        # Test that a GET request to /api/questions/ returns a list of questions
        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
