from datetime import datetime
import unittest

# Class representing a housing company
class HousingCompany:
    def __init__(self, company_name, company_address, number_of_customers, number_of_employees, sales_log):
        self.company_name = company_name
        self.company_address = company_address
        self.number_of_customers = number_of_customers
        self.number_of_employees = number_of_employees
        self.__sales_log = sales_log  # Private attribute
        self.datetime = datetime.now()  # Timestamp of when the object was created

    def info(self):
        """Returns a string containing company information."""
        return f"Company Name: {self.company_name}, Address: {self.company_address}, Customers: {self.number_of_customers}, Employees: {self.number_of_employees}"

    def set_data(self, company_name, company_address, number_of_customers, number_of_employees, sales_log):
        """Sets the company's data and updates the timestamp."""
        self.company_name = company_name
        self.company_address = company_address
        self.number_of_customers = number_of_customers
        self.number_of_employees = number_of_employees
        self.__sales_log = sales_log
        self.datetime = datetime.now()

# Class for apartment sales inheriting from HousingCompany
class ApartmentSale(HousingCompany):
    def __init__(self, company_name, company_address, number_of_customers, number_of_employees, sales_log):
        super().__init__(company_name, company_address, number_of_customers, number_of_employees, sales_log)
        self.apartment_info = {}  # Dictionary to store apartment information

    def add_apartment_info(self, apartment, price):
        """Adds apartment information to the dictionary, ensuring price is a positive number."""
        if price < 0:
            raise ValueError("Price must be a positive number.")
        self.apartment_info[apartment] = price

    def buy_in_installments(self, apartment, installment_years):
        """Calculates the monthly installment for purchasing an apartment."""
        if apartment in self.apartment_info:
            price = self.apartment_info[apartment]
            monthly_installment = price / (installment_years * 12)
            return f"The monthly installment for {apartment} is {monthly_installment:.2f} Euros."
        else:
            return "Apartment not found."

# Class for investment inheriting from HousingCompany
class Investment(HousingCompany):
    def __init__(self, company_name, company_address, number_of_customers, number_of_employees, sales_log, investment_amount):
        super().__init__(company_name, company_address, number_of_customers, number_of_employees, sales_log)
        if investment_amount < 0:
            raise ValueError("Investment amount must be a positive number.")
        self.investment_amount = investment_amount

    def annual_return_on_investment(self):
        """Calculates the annual return based on the investment amount."""
        if self.investment_amount >= 60000:
            return_rate = 0.11
        elif self.investment_amount >= 30000:
            return_rate = 0.09
        elif self.investment_amount >= 10000:
            return_rate = 0.05
        else:
            return_rate = 0.02
        return self.investment_amount * return_rate

# Unit tests for the classes
class TestHousingCompany(unittest.TestCase):

    def test_company_info(self):
        """Tests the basic information of the company."""
        company = HousingCompany("TestCompany", "Berlin", 100, 50, "private")
        self.assertEqual(company.company_name, "TestCompany")
        self.assertEqual(company.company_address, "Berlin")

    def test_add_apartment(self):
        """Tests adding apartment information."""
        apartment = ApartmentSale("CompanyX", "Berlin", 100, 50, "private")
        apartment.add_apartment_info("3 Room Apartment", 150000)
        self.assertIn("3 Room Apartment", apartment.apartment_info)

    def test_add_apartment_negative_price(self):
        """Tests adding apartment with a negative price raises an exception."""
        apartment = ApartmentSale("CompanyX", "Berlin", 100, 50, "private")
        with self.assertRaises(ValueError):
            apartment.add_apartment_info("3 Room Apartment", -150000)

    def test_buy_in_installments(self):
        """Tests the installment calculation for buying an apartment."""
        apartment = ApartmentSale("CompanyX", "Berlin", 100, 50, "private")
        apartment.add_apartment_info("2 Room Apartment", 120000)
        result = apartment.buy_in_installments("2 Room Apartment", 10)
        self.assertIn("The monthly installment for 2 Room Apartment is", result)

    def test_investment_profit(self):
        """Tests the profit calculation based on investment."""
        invest = Investment("Invest GmbH", "Munich", 50, 20, "investment", 30000)
        profit = invest.annual_return_on_investment()
        self.assertEqual(profit, 30000 * 0.09)

    def test_investment_negative_amount(self):
        """Tests initializing an investment with a negative amount raises an exception."""
        with self.assertRaises(ValueError):
            Investment("Invest GmbH", "Munich", 50, 20, "investment", -30000)

# Run the unit tests
if __name__ == "__main__":
    unittest.main()