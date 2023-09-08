# Sample data
data = [
    {"Name": "AA", "Shares": 100, "Price": 9.22, "Change": -22.98},
    {"Name": "IBM", "Shares": 50, "Price": 106.28, "Change": 15.18},
    {"Name": "CAT", "Shares": 150, "Price": 35.46, "Change": -47.98},
    {"Name": "MSFT", "Shares": 200, "Price": 20.89, "Change": -30.34},
    {"Name": "GE", "Shares": 95, "Price": 13.48, "Change": -26.89},
    {"Name": "MSFT", "Shares": 50, "Price": 20.89, "Change": -44.21},
    {"Name": "IBM", "Shares": 100, "Price": 106.28, "Change": 35.84}
]

# Header for the table
header = f"{'Name': >10} {'Shares': >10} {'Price': >10} {'Change': >10}"

# Print the header
print(header)

# Print the data with formatted price including the currency symbol
for item in data:
    formatted_price = f"${item['Price']:.2f}"
    formatted_change = f"{item['Change']:.2f}"
    print(
        f"{item['Name']: >10} {item['Shares']: >10} {formatted_price: >10} {formatted_change: >10}")
