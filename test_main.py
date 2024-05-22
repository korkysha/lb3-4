from unittest import TestCase


class TestSimpleApp(TestCase):
    def test_sum(self):
        self.assertEqual(2 + 3, 5)
