# -*- coding: utf-8 -*-
"""Unittest for a customers close to office.

Example:
        $ python invite_customers_test.py
"""
import unittest
from invite_customers import customers_invitation



OFFICE = (53.3393, -6.2576841)
CUSTOMERS_FILE = 'customers.json'



class TestStringMethods(unittest.TestCase):
    """Class of test that return the list of customers.
    """

    def test_numofcustomers(self):
        """Check number of customers is correct.
        """
        self.assertEqual(16, len(customers_invitation(customers_file=CUSTOMERS_FILE,
                                                      office_position=OFFICE)))

    def test_firstuser_id(self):
        """Check the first user_id in the list is correct.
        """
        self.assertEqual(4, customers_invitation(customers_file=CUSTOMERS_FILE,
                                                 office_position=OFFICE)[0][0])

    def test_firstname(self):
        """Check the fist name in the list is correct.
        """
        self.assertEqual('Ian Kehoe', customers_invitation(customers_file=CUSTOMERS_FILE,
                                                           office_position=OFFICE)[0][1])



if __name__ == '__main__':
    unittest.main()
