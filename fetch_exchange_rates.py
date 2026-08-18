import requests
import json

def fetch_exchange_rates():
    """
    Fetch exchange rates for USD from the exchangerate-api.com API
    """
    url = "https://v6.exchangerate-api.com/v6/2156687d167a7492fd4b9b9d/latest/USD"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        
        data = response.json()
        
        # Pretty print the response
        print(json.dumps(data, indent=2))
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None


if __name__ == "__main__":
    exchange_rates = fetch_exchange_rates()
    
    if exchange_rates:
        print("\n--- Exchange Rate Summary ---")
        print(f"Base Currency: {exchange_rates.get('base_code')}")
        print(f"Time Last Update UTC: {exchange_rates.get('time_last_update_utc')}")
        
        rates = exchange_rates.get('conversion_rates', {})
        print(f"\nTotal currencies available: {len(rates)}")
        
        # Display a few example rates
        print("\nSample rates (USD to):")
        for currency in list(rates.keys())[:5]:
            print(f"  {currency}: {rates[currency]}")
