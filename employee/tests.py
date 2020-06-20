from rest_framework import status
from rest_framework.test import APITestCase
from .models import EmployeeModel
from faker import Faker


class AccountTests(APITestCase):

    def generate_fake_data(self):
        """
        Generate fake data
        """
        fake = Faker()
        name = fake.name().split(" ")
        return {
            "first_name": name[0][0:5],
            "last_name": name[1],
            "email": name[0] + "@gmail.com"
        }

    def create_employee(self, data):
        """
        create a new employee
        """
        return self.client.post('/employee/', data, format='json')

    def test_create(self):
        """
        Test create api of employee
        """
        cnt = EmployeeModel.objects.count()
        data = self.generate_fake_data()
        response = self.create_employee(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(cnt+1, EmployeeModel.objects.count())
        self.assertEqual(EmployeeModel.objects.get().first_name, data["first_name"])

    def test_update(self):
        """
        Test updation api of employee
        """
        create_response = self.create_employee(self.generate_fake_data())
        create_response.data["first_name"] = create_response.data["first_name"]+"_upd"
        response = self.client.put('/employee/'+str(create_response.data["id"]), create_response.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, create_response.data)

    def test_delete(self):
        """
        Test delete api of employee
        """
        cnt = EmployeeModel.objects.count()
        create_response = self.create_employee(self.generate_fake_data())
        delete_response = self.client.delete('/employee/'+str(create_response.data["id"]), self.generate_fake_data(), format='json')
        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)
        self.assertEqual(cnt, EmployeeModel.objects.count())

    def test_edit(self):
        """
        Test edit api of employee which fetches single employee data
        """
        create_response = self.create_employee(self.generate_fake_data())
        delete_response = self.client.get('/employee/'+str(create_response.data["id"]), format='json')
        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)

    def test_list(self):
        """
        Test list api of employee
        """
        self.create_employee(self.generate_fake_data())
        response = self.client.get('/employee/', format='json')
        cnt = EmployeeModel.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(cnt, len(response.data))
