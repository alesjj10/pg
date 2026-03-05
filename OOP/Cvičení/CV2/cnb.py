import requests
from datetime import datetime

CNB_URL = "https://www.cnb.cz/en/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"

def fetch_exchange_rates():
    response = requests.get(CNB_URL)
    if response.status_code == 200:
        lines = response.text.splitlines()
        date_str = lines[0].split()[0]
        date = datetime.strptime(date_str, "%d.%m.%Y").date()
        rates = []
        for line in lines[2:]:
            parts = line.split('|')
            if len(parts) == 5:
                code = parts[3]
                amount = int(parts[2])
                rate = float(parts[4].replace(',', '.'))
                rates.append((date, code, amount, rate))
        return rates
    else:
        raise Exception(f"Failed to fetch exchange rates: {response.status_code}")
    
if __name__ == "__main__":
    date, rates = fetch_exchange_rates()
    print(f"Exchange rates for {date}:")
    for code, (amount, rate) in rates.items():
        print(f"{code}: {amount} units = {rate} CZK")