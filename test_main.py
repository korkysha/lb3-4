from unittest import TestCase


class TestSimpleApp(TestCase):

    def test_list_contains_element(self):
        self.assertIn(3, [1, 2, 3, 4, 5])
        
        wd