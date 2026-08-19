import requests


def convert_currency(amount: float, source: str, target: str) -> float:
    """
    Convert currency using a Web API.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{source.upper()}"

    response = requests.get(url)
    response.raise_for_status()  # Raises an exception for HTTP errors

    data = response.json()

    rates = data.get("rates")

    if target.upper() not in rates:
        raise ValueError(f"Currency '{target}' not found.")

    exchange_rate = rates[target.upper()]
    converted_amount = amount * exchange_rate

    return converted_amount


try:
    amount = float(input("Amount: "))
    source_currency = input("From: ").strip().upper()
    target_currency = input("To: ").strip().upper()

    result = convert_currency(
        amount,
        source_currency,
        target_currency
    )

    print(
        f"\n{amount:.2f} {source_currency} = "
        f"{result:.2f} {target_currency}"
    )

except ValueError as e:
    print(f"Input Error: {e}")

except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")

except Exception as e:
    print(f"Unexpected Error: {e}")