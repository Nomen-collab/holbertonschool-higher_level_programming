#!/usr/bin/python3


"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))
    
    def test_single_element(self):
        """Test with a list that has one element."""
        self.assertEqual(max_integer([42]), 42)
    
    def test_multiple_elements(self):
        """Test with a list of multiple elements."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_multiple_elements_unsorted(self):
        """Test with a list of multiple elements, unsorted."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
    
    def test_equal_elements(self):
        """Test with a list of equal elements."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
    
    def test_single_negative_number(self):
        """Test with a list that has one negative number."""
        self.assertEqual(max_integer([-42]), -42)

if __name__ == '__main__':
    unittest.main()

