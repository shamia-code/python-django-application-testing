from django.test import TestCase

from myapp.models import MyUser

class TestUserActivate(TestCase):
    """When the test is run , this setUp method is called before each one of these tests to 
    set up the common data to those test methods"""
    def setUp(self):
        self.user = MyUser.objects.create (is_active=True)

    def test_deactivate(self):
        self.user.deactivate()
        self.assertFalse(self.user.active)

    def test_deactivate_activate(self):
        self.user.deactivate()
        self.user.activate()
        self.assertTrue(self.user.active)
