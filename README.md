
```markdown
# Housing Company Management

This project is a comprehensive system for managing housing companies. It includes classes to represent companies, handle apartment sales, and manage investments, along with unit tests to ensure correct functionality.

## Components

- **HousingCompany**: A class that encapsulates basic information about a housing company, including name, address, number of customers, and number of employees.
  
- **ApartmentSale**: A subclass of `HousingCompany` that provides functionality to add apartment information and calculate installment plans for purchases.
  
- **Investment**: Another subclass of `HousingCompany` focused on managing investments and calculating annual returns.

## Files

- `README.md`: The documentation file for the project.
- `main.py`: The main application code for managing housing companies.
- `test_housing.py`: Unit tests for the housing company management system.

## Requirements

- Python 3.x
- `unittest` library (included in the standard Python library)

## Usage

1. Clone the project:
   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. Run the unit tests:
   ```bash
   python -m unittest discover
   ```

## Examples

### Create a Housing Company

```python
company = HousingCompany("TestCompany", "Berlin", 100, 50, "private")
print(company.info())
```

### Add Apartment Information

```python
apartment = ApartmentSale("CompanyX", "Berlin", 100, 50, "private")
apartment.add_apartment_info("3 Room Apartment", 150000)
```

### Calculate Installments

```python
installment_info = apartment.buy_in_installments("3 Room Apartment", 10)
print(installment_info)
```

### Calculate Annual Return on Investment

```python
investment = Investment("Invest GmbH", "Munich", 50, 20, "investment", 30000)
profit = investment.annual_return_on_investment()
print(f"Annual profit: {profit}")
```

## License

This project is licensed under the [MIT License](LICENSE).
```
