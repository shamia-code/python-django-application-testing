from django.test import TestCase

def add(a,b):
    return a + b

class TestAdd(TestCase):
    def test_add_positive_numbers(self):
        self.assertEquals(add(2, 2), 4)

    def test_add_negative_numbers(self):
        self.assertEquals(add(-2, -2), -4)

    #def test_add_posititvenumbers(self):
        #self.assertEquals(add(2, 2), 5)