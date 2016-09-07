from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User, Group

from example.admin import MyModelAdmin

from example.models import MyModel


class MockRequest(object):
    pass


class TestReadonlyAdminMixin(TestCase):

    def setUp(self):
        self.request = MockRequest()
        self.my_model = MyModel.objects.create(
            my_first_field="this is just test data 1",
            my_second_field="this is just test data 2"
        )
        self.site = AdminSite()

    def test_make_fields_readonly(self):
        self.request.user = User.objects.create_user('ckgathi', 'ckgathi@gmail.com', 'thabo321')
        group = Group(name="Monitors")
        group.save()                  # save this new group for this example
        self.request.user.groups.add(group)
        ma = MyModelAdmin(MyModel, self.site)
        self.assertEqual(sorted(list(ma.get_readonly_fields(self.request))), sorted(['my_first_field', 'my_second_field']))

    def test_admin_fields_not_readonly(self):
        self.request.user = User.objects.create_user('thabo', 'thabo@gmail.com', 'thabo321')
        ma = MyModelAdmin(MyModel, self.site)
        self.assertEqual(ma.get_readonly_fields(self.request), [])
