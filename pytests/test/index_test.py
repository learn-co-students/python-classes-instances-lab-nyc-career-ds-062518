import unittest2 as unittest
from ipynb.fs.full.index import *

class TestPythonClasses(unittest.TestCase):
    def test_class_definitions(self):
        class ExampleClass:
            pass
        self.assertEqual(type(Driver), type(ExampleClass))
        self.assertEqual(type(Passenger), type(ExampleClass))
        self.assertEqual(type(Ride), type(ExampleClass))


    def test_instances(self):
        self.assertEqual(type(meryl), type(Passenger()))
        self.assertEqual(type(daniel), type(Passenger()))
        self.assertEqual(type(flatiron_taxi), type(Driver()))
        self.assertEqual(type(ride_to_school), type(Ride()))
        self.assertEqual(type(ride_home), type(Ride()))
