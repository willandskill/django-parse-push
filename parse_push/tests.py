from django.db import IntegrityError
from django.test import TestCase
from django.utils import six


class BasicTest(TestCase):

    def setUp(self):
        print 'in setUp'

    def test_init(self):
        assert 1==1