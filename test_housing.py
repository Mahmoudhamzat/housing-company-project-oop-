# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 22:46:25 2025

@author: mmmkh
"""

import unittest
from housing_company import HousingCompany, ApartmentSale, Investment

class TestHousingCompany(unittest.TestCase):
    
    def setUp(self):
        """Set up test cases with sample data."""
        self.company = HousingCompany("TestCompany", "Berlin", 100, 50, "private")
        self.apartment = ApartmentSale("CompanyX", "Berlin", 100, 50, "private")
        self.investment = Investment("Invest GmbH", "Munich", 50, 20, "investment", 30000)

    def test_company_info(self):
        """Tests the basic information of the company."""
        self.assertEqual(self.company.company_name, "TestCompany")
        self.assertEqual(self.company.company_address, "Berlin")

    def test_add_apartment(self):
        """Tests adding apartment information."""
        self.apartment.add_apartment_info("3 Room Apartment", 150000)
        self.assertIn("3 Room Apartment", self.apartment.apartment_info)

    def test_add_apartment_negative_price(self):
        """Tests adding apartment with a negative price raises an exception."""
        with self.assertRaises(ValueError):
            self.apartment.add_apartment_info("3 Room Apartment", -150000)

    def test_buy_in_installments(self):
        """Tests the installment calculation for buying an apartment."""
        self.apartment.add_apartment_info("2 Room Apartment", 120000)
        result = self.apartment.buy_in_installments("2 Room Apartment", 10)
        self.assertIn("The monthly installment for 2 Room Apartment is", result)

    def test_investment_profit(self):
        """Tests the profit calculation based on investment."""
        profit = self.investment.annual_return_on_investment()
        self.assertEqual(profit, 30000 * 0.09)

    def test_investment_negative_amount(self):
        """Tests initializing an investment with a negative amount raises an exception."""
        with self.assertRaises(ValueError):
            Investment("Invest GmbH", "Munich", 50, 20, "investment", -30000)

if __name__ == "__main__":
    unittest.main()
