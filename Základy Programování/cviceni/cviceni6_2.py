import requests

def download_rates(url):
    response = requests.get(url)
    if not response.ok:
        print("špatná url adresa")
        return
    
    rates = {}
    data = response.text
    data = data.split('\n')

    for line in data[2:]:
        fields = line.split('|')
        if len(fields) < 5:
            continue
        currency = int(fields[2])
        rates[fields[3]] = float(fields[4].replace(',', '.')) / currency

    return rates


if __name__ == "__main__":

    url = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'

    rates = download_rates(url)

    print(rates)
