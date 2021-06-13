import unittest
import requests


class TestYaUploader(unittest.TestCase):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    token_ya = "   "  # ввод токена
    folder_name = "folder"

    def setUp(self):
        pass

    def tearDown(self):
        params = {'path': self.folder_name, 'permanently': True}
        headers = {'Authorization': self.token_ya}
        response = requests.delete(self.url, headers=headers, params=params)
        print(response)
        pass

    def test_create_folder(self):  # проверка создания папки, успешного запроса, отрицательного запроса
        params = {'path': self.folder_name}
        headers = {'Content-Type': 'application/json', 'Authorization': self.token_ya}
        response = requests.put(self.url, headers=headers, params=params)
        print(response)
        self.assertEqual(201, response.status_code)
        response = requests.get(self.url, headers=headers, params=params)
        print(response)
        self.assertEqual(200, response.status_code)
        response = requests.put(self.url, headers=headers, params=params)
        print(response)
        self.assertEqual(409, response.status_code)


if __name__ == '__main__':
    unittest.main()
