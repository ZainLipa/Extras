# Program of the Day: Currency Converter

# Exchange rates (as of a specific date)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
    "AUD": 1.33,
    "CAD": 1.28
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not supported."
    
    # Perform the currency conversion
    converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
    
    return converted_amount

# Example usage: Convert USD to EUR
amount_in_usd = 100.0
from_currency = "USD"
to_currency = "EUR"
converted_amount = convert_currency(amount_in_usd, from_currency, to_currency)
print(f"{amount_in_usd} {from_currency} is equal to {converted_amount} {to_currency}.")
