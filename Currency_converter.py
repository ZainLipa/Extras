# Program of the Day: Currency Converter

def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

# Example usage
usd_amount = 100  # Amount in US Dollars
exchange_rate = 1.23  # Example exchange rate (USD to EUR)

eur_amount = convert_currency(usd_amount, exchange_rate)
print(f"{usd_amount} USD is equal to {eur_amount} EUR")
