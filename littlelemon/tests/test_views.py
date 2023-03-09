from django.test import TestCase
from restaurant import models


class MenuViewTest(TestCase):

    def setUp(self):
        models.Menu.objects.create(title='Ice Cream', price=80, inventory=80)
        models.Menu.objects.create(title='Soup', price=21, inventory=100)
        models.Menu.objects.create(title='Fish', price=44, inventory=90)
        models.Menu.objects.create(title='Beer', price=20, inventory=110)
        models.Menu.objects.create(title='French Fries', price=25, inventory=60)


    def test_getall(self):
        data = [str(x) for x in list(models.Menu.objects.all())]
        expected_data = ['Ice Cream : 80.00', 'Soup : 21.00', 'Fish : 44.00', 'Beer : 20.00', 'French Fries : 25.00']

        self.assertEqual(set(data), set(expected_data))

    