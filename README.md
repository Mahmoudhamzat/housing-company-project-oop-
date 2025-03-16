
```markdown
# Housing Company Management

This project is a system for managing housing companies, including classes to represent companies, apartment sales, and investments. It also includes unit tests to ensure the functionality works correctly.

## Components

- **HousingCompany**: A class representing a housing company with basic information such as name, address, number of customers, and number of employees.
- **ApartmentSale**: A subclass of `HousingCompany` that includes functions to add apartment information and calculate installments.
- **Investment**: Another subclass of `HousingCompany` that deals with investments and calculates the annual return.

## Requirements

- Python 3.x
- `unittest` library (included in Python)

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

Make sure to replace `https://github.com/username/repository.git` with the correct URL for your GitHub repository. 
