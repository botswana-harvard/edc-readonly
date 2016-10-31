from django.test import TestCase
from example.models import MyModel


class TestReadonlyAdminMixin(TestCase):

    def setUp(self):
        self.my_model = MyModel.objects.create(
            my_first_field="this is just test data 1",
            my_second_field="this is just test data 2"
        )

    def test_make_fields_readonly(self):
        print(self.my_model.__class__.__name__, '*****', self.my_model._meta.app_label)
#         for field, val in self.my_model:
#             print(field, val)
